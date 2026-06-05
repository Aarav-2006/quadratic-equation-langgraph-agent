from typing import TypedDict
from config import llm
class QuadraticState(TypedDict):
    equation:str

    a:float
    b:float
    c:float 
    discriminant:float 
    result:str
    explanation:str