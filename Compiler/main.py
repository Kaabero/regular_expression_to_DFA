from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import json
from src.utils import validate_input, format_input_for_syntax_tree, get_postfix
from src.syntax_tree import SyntaxTree

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

@app.post("/api/dfa")
def create_dfa(data: RegularExpression):
    try:
        validate_input(data.regex)
        infix = format_input_for_syntax_tree(data.regex)
        s = SyntaxTree()
        s.build_tree(get_postfix(infix))
        result = s.get_tree()
        result_json = json.loads(json.dumps(result, default=str))
        response = {"regex": data.regex, "result": result_json}
        global regex
        regex = result_json
        return response

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/api/regex")
def get_regex():
    return {"regex": regex}



        