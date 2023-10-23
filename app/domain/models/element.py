
element_attributes = ["idBulk","retries", "status","name"]

class IElement():

    idBulk:int
    retries:int
    status:int
    name:str

class Element(IElement):
    def __init__(self,idBulk, retries, status, name):

        self.idBulk = idBulk
        self.retries = retries
        self.status = status
        self.name = name
        