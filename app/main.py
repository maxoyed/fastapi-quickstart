from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class HelloBody(BaseModel):
    username: str = Field(
        title="用户名",
    )


@app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}


@app.post("/hello")
async def hello(helloBody: HelloBody):
    return {"code": 0, "msg": "success", "data": f"Hello, {helloBody.username}"}
