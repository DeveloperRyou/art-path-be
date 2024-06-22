import logging

import uvicorn
from fastapi import FastAPI

from src.api import record, records, routing, test, user

app = FastAPI()


@app.on_event("startup")
def boot_server():
    logging.info("server boot ...")


@app.on_event("shutdown")
def shutdown_server():
    logging.info("server shutdown ...")


app.include_router(test.router)
app.include_router(user.router, prefix="/users", tags=["User"])
app.include_router(record.router, prefix="/record", tags=["Record"])
app.include_router(records.router, prefix="/records", tags=["Records"])
app.include_router(routing.router, prefix="/routing", tags=["Routing"])


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
