from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import json
from src.utils import validate_input, format_input_for_syntax_tree, get_postfix, format_dfa_for_ui
from src.syntax_tree import SyntaxTree
from src.dfa import DFA

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

@app.post("/api/dfa")
def create_dfa(data: RegularExpression):
    try:
        validate_input(data.regex)
        infix = format_input_for_syntax_tree(data.regex)
        s = SyntaxTree()
        s.build_tree(get_postfix(infix))
        syntax_tree = s.get_tree()
        d = DFA(syntax_tree, sorted(n.number for n in s.root.firstpos))
        d.build_dfa()
        result = format_dfa_for_ui(d.states, d.start_state, d.alphabet, d.accepting_states, d.tran)
        result_json = json.loads(json.dumps(result, default=str))
        response = {"regex": data.regex, "result": result_json}
        return response

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))




        