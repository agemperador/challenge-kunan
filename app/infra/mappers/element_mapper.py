
from app.infra.dto.element_dto import ElementDto
from app.infra.models.element import ElementDB


def element_db_from_dto(dto : ElementDto):
    return ElementDB(
        idBulk=dto.idBulk,
        status=dto.status,
        retries=dto.retries,
        name=dto.name
        )