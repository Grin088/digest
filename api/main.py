from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import ORJSONResponse
from api.routers import users, digests, subscriptions, posts
from api.services.exceptions.object_exceptions import DataBaseObjectException
from api.logger.logger_main import logger

app = FastAPI()


# app.include_router(users.router)
app.include_router(subscriptions.router)
app.include_router(posts.router)
app.include_router(digests.router)


@app.exception_handler(DataBaseObjectException)
async def data_base_object_exc(request: Request, exc: DataBaseObjectException):
    """Handle exceptions are raised in DataBaseObjectException"""
    return ORJSONResponse(
        status_code=exc.status_code, content=exc.content, headers=exc.headers
    )


@app.exception_handler(Exception)
async def server_errors(request: Request, exc: Exception):
    """Handle server errors"""
    if not isinstance(exc, HTTPException):
        logger.error(msg=exc, exc_info=True)
        return ORJSONResponse(status_code=500, content={500: "INTERNAL_SERVER_ERROR"})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000, reload=True)
