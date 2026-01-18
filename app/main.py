from contextlib import asynccontextmanager
import logging

from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError

from app.db.setup import setup_db
logger = logging.getLogger(__name__)
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.user import router as user_router
from settings import BASE_DIR, config

@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_db()
    yield


app = FastAPI(title='FitTracker Auth Service', lifespan=lifespan)

app.include_router(user_router)

app.mount("/login/static", StaticFiles(directory=BASE_DIR / 'frontend/dist', html=True), name='static')

@app.get("/login/{full_path:path}")
async def catch_all(full_path: str):
    return FileResponse(BASE_DIR / 'frontend/dist/index.html')

@app.get("/login/{full_path:path}")
async def login_catch_all(full_path: str):
    return FileResponse(BASE_DIR / "frontend/dist/index.html")

@app.get("/")
def read_root():
    return {"message": "Welcome to the FitTracker Auth Service"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
    allow_credentials=True,
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    content = jsonable_encoder({"detail": exc.errors(), "body": exc.body})
    logger.error(content)
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=content
    )
        

if __name__ == "__main__":
    logger.info("Starting FitTracker Auth Service...")
    uvicorn.run(app, host=config.host, port=config.port)