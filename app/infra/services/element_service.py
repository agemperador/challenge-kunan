
from app.infra.dao.element_dao import ElementDao
from app.infra.models.element   import ElementDB
from app.domain.models.element import element_attributes
from app.domain.validations.element_validation import validate_element_to_save

from app.utils.utils import jsonify_element
from app.adapters.database import database



element_dao = ElementDao()


class ElementService:
    """
        Modularización del service de element, donde al instanciarlo se guarda la db internamente
    """

    def __init__(self):
        self.db = database

    def get_elements(self):
        """
            Find all abstraido del orm por un dao
        """
        return element_dao.find_all()
    
    def get_elements_by_status(self,status):
        """
            Find all by status abstraido del orm por un dao
        """
        return element_dao.find_all_by_status(status=status)
    
    def create_element(self, element: ElementDB ):
        """
            create abstraido del orm
        """
        element_response = jsonify_element(element, element_attributes)

        try:
            validate_element_to_save(element)
            self.db.save_element(element)
        except ValueError as e:
            raise ValueError(e)
            
        
        return element_response
