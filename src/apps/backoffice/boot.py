import uvicorn
from fastapi import FastAPI


def boot():
    app: FastAPI = FastAPI()
    uvicorn.run(app, host="0.0.0.0", port=8000)
