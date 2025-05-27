from fastapi import FastAPI, HTTPException
from models import ExecuteRequest
from fastapi.responses import JSONResponse
from run_workflow import execute_workflow

app = FastAPI()


@app.post("/execute")
async def chat(request: ExecuteRequest):
    try:
        response = await execute_workflow(user_id=request.user_id, tenant_id=request.tenant_id,session_id= request.session_id, query=request.message, api_key=request.api_key)
        if not isinstance(response, list):
            return JSONResponse(
                content=[{"source": response.source, "content": response.content}],
                status_code=200,
                media_type="application/json"
            )
        return response
    except Exception as e:
        error_message = {
            "type": "error",
            "content": f"Error: {str(e)}",
            "source": "system"
        }
        raise HTTPException(status_code=500, detail=error_message) from e


# Example usage
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)