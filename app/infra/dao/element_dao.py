from app.infra.models.element import ElementDB


class ElementDao (ElementDB):

    def __init__ (self):
        pass

    def find_all(self):
        return ElementDB.query.all()
    
    def find_all_by_status(self, status):
        return ElementDB.query.filter_by(status=status).all()
    