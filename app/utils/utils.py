

def jsonify_element(element, element_attributes):
    """
        Función que permite convertir un objeto en json
    """
    return { key: element.__dict__[key] for key in element_attributes}

def jsonify_array(element, element_attributes):
    """
        Función que permite aplicar la conversión jsonify_element a un array
    """
    return [ jsonify_element(element, element_attributes) for element in element]