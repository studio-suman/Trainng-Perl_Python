from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from FastApi.database import database, schemas
from FastApi.backend import models, auth

# Create tables once from a single Base (use models.Base as the source of truth)
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="My API")

# --- CORS ---
# IMPORTANT: if allow_credentials=True, do NOT use "*"
ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:5173",
    # Add your real frontend origins here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- OAuth2 ---
# This will make Swagger "Authorize" button work with /token form
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Helpers ---
def get_user(db: Session, username: str):
    return (
        db.query(models.User)
        .filter(models.User.User_Name == username)
        .first()
    )

def authenticate_user(db: Session, username: str, password: str):
    user = get_user(db, username)
    if not user or not auth.verify_password(password, user.Hashed_password):
        return False
    return user

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, auth.SECRET_KEY, algorithms=[auth.ALGORITHM])
        username: str | None = payload.get("sub")  # type: ignore
        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(username=username)
    except JWTError:
        raise credentials_exception

    user = get_user(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

# --- Auth Routes ---

@app.post("/register", status_code=status.HTTP_201_CREATED)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Optional: check unique username/email
    existing = db.query(models.User).filter(
        (models.User.User_Name == user.username) |
        (models.User.User_Email == user.useremail)
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username or email already exists")

    hashed = auth.get_password_hash(user.password)
    db_user = models.User(
        User_Name=user.username,
        User_Email=user.useremail,
        Valid=user.valid,
        Hashed_password=hashed
    )
    db.add(db_user)
    db.commit()
    return {"msg": "User created"}

# OAuth2 standard token endpoint for Swagger `Authorize` flow
@app.post("/token", response_model=schemas.Token)
def token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        # OAuth2 spec expects 400 for invalid_grant pattern
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid credentials")
    access_token = auth.create_access_token({"sub": user.User_Name})
    return {"access_token": access_token, "token_type": "bearer"}

# If you still want JSON-based login (for programmatic clients)
@app.post("/login", response_model=schemas.Token)
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = authenticate_user(db, user.username, user.password)
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = auth.create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

# --- Items ---

@app.post("/items", response_model=schemas.Item)
def create_item(
    item: schemas.ItemCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    # ensure owner is set to current user
    db_item = models.Item(**item.model_dump(), owner_id=current_user.Id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/items/", response_model=list[schemas.Item])
def read_items(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return (
        db.query(models.Item)
        .filter(models.Item.owner_id == current_user.Id)
        .all()
    )

@app.put("/items/{item_id}", response_model=schemas.Item)
def update_item(
    item_id: int,
    item: schemas.ItemCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    db_item = (
        db.query(models.Item)
        .filter(models.Item.id == item_id, models.Item.owner_id == current_user.Id)
        .first()
    )
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db_item.title = item.title  # type: ignore
    db_item.description = item.description  # type: ignore
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/items/{item_id}")
def delete_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    db_item = (
        db.query(models.Item)
        .filter(models.Item.id == item_id, models.Item.owner_id == current_user.Id)
        .first()
    )
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"detail": "Item deleted"}

# --- Movies ---

@app.get("/movies/", response_model=list[schemas.Movies])
def get_all_movies(
    genre: str | None = None,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    query = db.query(models.Movies)
    if genre:  # Only apply filter if genre is not None and not empty
        query = query.filter(models.Movies.genre == genre)
    return query.all()

