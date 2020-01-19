from flask import Flask
from flask import request
import json 
from sqlalchemy import create_engine

import pacientes_info

app = Flask(__name__)

db_host = 'localhost'
db_name = 'pacientes'
db_user = 'clientepacientes'
db_password = 'usuario123456'
sqlEngine = create_engine('mysql+pymysql://{}:{}@{}/{}'.format(db_user, db_password, db_host, db_name), pool_recycle=3600)


@app.route("/pacientes", methods=['POST'])
def registrar_paciente():
    paciente = request.get_json()
    db = sqlEngine.connect()
    id_paciente = pacientes_info.registrar_paciente(paciente, db)
    db.close()
    return json.dumps({"id_paciente": id_paciente})

@app.route("/pacientes", methods=["GET"])
def leer_paciente():
    cedula = request.args.get('cedula')
    db = sqlEngine.connect()
    paciente = pacientes_info.consultar_paciente(cedula, db)
    db.close()
    return json.dumps(paciente)

if __name__ == "__main__":
    app.run()
    