from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RegularExpression(BaseModel):
    regex: str

regex = None

@app.post("/api/regex")
def create_regex(data: RegularExpression):
    result = list(data.regex)
    response = {"regex": data.regex, "result": result}
    global regex
    regex = result
    return response

@app.get("/api/regex")
def get_regex():
    return {"regex": regex}
