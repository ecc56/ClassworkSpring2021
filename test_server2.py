from server2 import init_server

init_server()

def test_add_patient_to_db():
    from server2 import add_patient_to_db
    from server2 import db
    name = "Emma Cooper"
    id = 100
    blood_type = "O+"
    answer = add_patient_to_db(name, id, blood_type)
    answer.delete() # put this line before the assert line
    # last_patient_in_db = db[-1]
    # expected = {}
    assert answer.id_no == id
    
def test_add_patient_test_data():
    from server2 import add_patient_test_data
    from server 2 import add_patient_to_db
    name = "Emma Cooper"
    id = 100
    blood_type = "O+"
    added_patient = add_patient_to_db(name, id, blood_type)
    out_data = {"id":8, 
                "test_name": "LDL,
                "test_result": 100}
    answer = add_patient_test_data(out_data)
    expected = ("LDL", 100)
    assert answer.test[-1] == expected
 


# def test_get_patient_from_db():
    # from server2 import get_patient_from_db
    # from server2 import db
    # test_patient = {}
    # db.append(test_patient)
    # answer = get_patient_from_db(200)
    # assert answer == test_patient

# def test_get_patient_from_db_missing():
    # from server2 import get_patient_from_db
    # from server2 import db
    # test_patient = {}
    # db.append(test_patient)