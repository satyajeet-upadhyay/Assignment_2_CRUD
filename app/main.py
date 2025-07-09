from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from app.routes import create_user, get_user, update_user, delete_user, auth_check
from app.auth_middleware import users

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def handle_validation_error(request: Request, exc: RequestValidationError):
    for error in exc.errors():
        field = error.get("loc")[-1]
        if field in {"phone", "name"}:
            return JSONResponse(
                status_code=422,
                content={"detail": f"Please enter a valid {field}."}
            )
    return JSONResponse(status_code=422, content={"detail": "Invalid input."})

app.include_router(users.router)
app.include_router(create_user.router)
app.include_router(get_user.router)
app.include_router(update_user.router)
app.include_router(delete_user.router)
app.include_router(auth_check.router)


