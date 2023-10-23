from flask import Blueprint, request, make_response, jsonify
from app.infra.services.element_service import ElementService
from app.domain.models.element import element_attributes
from app.utils.utils import jsonify_array

from app.infra.dto.element_dto import ElementDto
from app.infra.mappers.element_mapper import element_db_from_dto

element_service = ElementService()

bp_element = Blueprint('routes', __name__)


@bp_element.route('/elements', methods=['GET'])
def get_elements():
    elements_db =  element_service.get_elements()

    return jsonify_array(elements_db, element_attributes)



@bp_element.route('/elements/<status>', methods=['GET'])
def get_elements_by_status(status):

    elements_db =  element_service.get_elements_by_status(status)
    return  jsonify_array(elements_db, element_attributes)

@bp_element.route('/elements', methods=['POST'])
def create_element ():

    element_dto: ElementDto =  ElementDto(**request.json)

    element_db = element_db_from_dto(element_dto)

    try:
        element_created = element_service.create_element(element_db)
    except ValueError as e:
        return  make_response(jsonify({'error': 'Bad Request', 'message':f'{e}'}), 400)
    

    return element_created
    