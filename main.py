from flask import Flask

from  app.infra.controllers.element_controller import bp_element
from  app.adapters.database import database


app = Flask(__name__)
app.config[database.db_key] = database.db_url

app.register_blueprint(bp_element)

database.init_app(app)

# endpoint para verificar que la app esta levantada
@app.route('/')
def ping():
    return "OK"

# incializa la aplicación 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
