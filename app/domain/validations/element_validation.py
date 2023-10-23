from app.domain.models.element import IElement


def validate_element_to_save(element: IElement):
    """
        Validaciones del core para la creacion de un element
    """
    error = {
        'active':False,
        "message":''
    }
    if element.name =='':
        error['active']=True
        error['message'] += "El nombre no puede estar vacio - "
    if element.idBulk <0: 
        error['active']=True
        error['message'] += "El idBulk no puede ser menor a 0 - "
    if element.status <0 or element.status > 99:
        error['active']=True
        error['message'] += "El status tiene que estar entre 0 y 99 - "
    if element.retries <0: 
        error['active']=True
        error['message'] += "retries debe ser mayor a 0 "
    
    if error['active']:
        raise ValueError (error['message'])

    return True