from typing import Literal
from pydantic import BaseModel
class Capability(BaseModel):
    name:str; category:str; maturity:Literal[1,2,3,4,5]
class Person(BaseModel):
    id:int; name:str; role:str; team:str; location:str; skills:list[str]; capabilities:list[Capability]; summary:str
class Metadata(BaseModel):
    teams:list[str]; roles:list[str]; skills:list[str]
