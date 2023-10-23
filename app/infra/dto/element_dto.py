
from dataclasses import dataclass

@dataclass
class ElementDto:
    idBulk:int
    status:int
    retries:int
    name:str