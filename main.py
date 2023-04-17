from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Msg(BaseModel):
    msg: str


@app.get("/")
async def root():
    return {"message": "Hey there! Visit '/docs' endpoint to see the interactive Swagger UI and test the APIs out there! "}


@app.post("/reverse")
async def reverse_a_string(inp: Msg):
    return {"message": inp.msg[::-1]}