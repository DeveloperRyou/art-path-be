import logging

import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
def boot_server():
    logging.info("server boot ...")


@app.on_event("shutdown")
def shutdown_server():
    logging.info("server shutdown ...")


@app.get("/test")
def get_result():
    return {"test": "success"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)