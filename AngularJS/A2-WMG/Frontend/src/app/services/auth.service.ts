import { Injectable } from '@angular/core';
import { AngularFireAuth } from '@angular/fire/compat/auth'
import { AngularFirestore, AngularFirestoreCollection } from '@angular/fire/compat/firestore';
import { Observable } from 'rxjs';
import IUser from 'src/app/models/user.models';
import { map } from "rxjs/operators";

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private userCollection: AngularFirestoreCollection<IUser>
  public isAuthenticated$: Observable<boolean>




  constructor(
    private auth: AngularFireAuth,
    private db: AngularFirestore
  ) { 
    this.userCollection = db.collection("users")
    this.isAuthenticated$ = auth.user.pipe(
      map( user => !!user)
    )
  }

  getUserState() {
    return this.auth.authState
  }

  public async createUser(userData: IUser) {

    if(!userData.password) {
      throw new Error("Password Not Provided!");
    }

    const userCred = await this.auth.createUserWithEmailAndPassword(
      userData.email as string, userData.password as string
    )

    if(!userCred.user) {
      throw new Error("User Can't be Found");
    }  

    await this.userCollection.doc(userCred.user.uid).set({
        name: userData.name,
        email: userData.email,
        age: userData.age,
        phoneNumber: userData.phoneNumber
      }
    )
      await userCred.user.updateProfile({
        displayName: userData.name,
      })

  }


  logout(){
    this.auth.signOut()
  }
}


