from fastapi import FastAPI
from app.routes import create_user, get_user, update_user, delete_user
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi import Request
from pydantic import ValidationError

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    for err in errors:
        loc = err.get("loc")[-1]
        if loc == "phone":
            return JSONResponse(status_code=422, content={"detail": "Please enter a valid phone number."})
        elif loc == "name":
            return JSONResponse(status_code=422, content={"detail": "Please enter a valid name."})

    return JSONResponse(status_code=422, content={"detail": "Invalid input."})

# Include all routers
app.include_router(create_user.router)
app.include_router(get_user.router)
app.include_router(update_user.router)
app.include_router(delete_user.router)

 