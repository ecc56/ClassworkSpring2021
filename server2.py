from flask import Flask, request, jsonify
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

db = list()


def init_server():
    add_patient_to_db("Ann", 101, "A")
    add_patient_to_db("Bob", 102, "B")

def add_patient_to_db(name, id, blood_type):
    new_patient = {"name": name, "id": id, 
                   "blood_type": blood_type, 
                   "test": list()}
    db.append(new_patient)
    print(db)
    logging.info(new_patient)
    return True
    
    
@app.route("/new_patient", methods=["POST"])
def post_new_patient():
    # get input data from requests
    in_data = request.get_json()
    # validate input
    validate_input, server_status = validate_new_patient_info(in_data)
    if validate_input is not True:
        return validate_input, server_status
    #define new patient dictionary
    add_patient_to_db(in_data["name"], in_data["id"],
                      in_data["blood_type"])
    # return/display results
    return "Patient added", 200
    
    
def validate_new_patient_info(in_dict):
    expected_keys = ("name, "id", "blood_type")
    expected_types = (str, int, str)
    for key, ty in zip(expected_keys, expected_types):
        if key not in in_dict.keys():
            return"{} key not found".format(key,400)
        if type(in_dict[key]) != ty:
            return "{} key has the wrong value type".format(key), 400
    return True, 200
    
    
if __name__ == '__main__':
    init_server()
    app.run()