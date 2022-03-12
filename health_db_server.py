import logging
from flask import Flask, request, jsonify

# Define variable to contain Flask class for server
app = Flask(__name__)

# Create list for database to contain patient data
db = []


def init_server():
    """ Initializes server conditions

    This function initializes the server log and can be used for any other
    tasks that you would like to run upon initial server start-up.  For
    example, it currently adds two patients to the database so that there is
    content in the database for testing.  Also, in the future, when an external
    database is utilized, the connection to that external database can be
    established here.

    Note:  As currently written, this function does not need a unit test as
    it does not do any data manipulation itself.
    """
    add_patient_to_db("Ann Ables", 101, "A+")
    add_patient_to_db("Bob Boyles", 202, "B-")
    logging.basicConfig(filename="health_db_server.log", level=logging.DEBUG)


@app.route("/new_patient", methods=["POST"])
def new_patient_handler():
    """Handles requests to the /new_patient route for adding a new patient to
    server database

    The /new_patient route is a POST request that should receive a JSON-encoded
    string with the following format:

    {"name": str, "id": int, "blood_type": str}

    The function then calls a driver function that implements the functionality
    of this route and receives an "answer" and "status_code" from this
    driver function.  Finally, it returns the "answer" using jsonify and the
    status_code.

    Note: This function only does the three things that a flask handler should
    do.  1. Get data from the request. 2. Call other functions to do the
    work. 3. Return the results.  Therefore, it does not need a unit test.

    Returns:
        str, int: message including patient data if successfully added to the
                  database or error message if not, followed by a status code
    """
    # Get the data from the request
    in_data = request.get_json()
    # Call OTHER function to do the request
    answer, status_code = new_patient_driver(in_data)
    # Provide a response
    return jsonify(answer), status_code


def new_patient_driver(in_data):
    """Implements /new_patient route for adding a new patient to server
    database

    The flask handler function for the /new_patient route calls this function
    to implement the functionality.  It receives as a parameter a dictionary
    that should contain the needed information in the following format:

    {"name": str, "id": int, "blood_type": str}

    The function first calls a validation function to ensure that the needed
    keys and data types exist in the dictionary, then calls a function to
    add the patient data to the database.  The function then returns to the
    caller either a status code of 200 and the patient info if it was
    successfully added, or a status code of 400 and an error message if there
    was a validation problem.

    Args:
        in_data (any type): the input data received by the route.  Ideally,
        it is a dictionary.

    Returns:
        str, int: message including patient data if successfully added to the
                  database or error message if not, followed by a status code
    """

    answer, status_code = validate_new_patient_input(in_data)
    if status_code != 200:
        return answer, status_code
    add_patient_to_db(in_data["name"], in_data["id"], in_data["blood_type"])
    print(db)
    return True, 200


def validate_new_patient_input(in_data):
    """Validates that input data to the /new_patient route contains a
    dictionary with the correct keys and data types

    The /new_patient route for this server is a POST request that should
    receive a JSON-encoded string which contains dictionaries.  To avoid server
    errors, this function checks that the input data is a dictionary, that it
    has the specified keys, and specified data types.

    Args:
        in_data (any type): the input data that has been deserialized from a
        JSON string.  Ideally, it is a dictionary.

    Returns:
        str or bool , int: returns True, 200 if data validation is successful.
            Returns an error message string and 400 if data validation is
            unsuccessful.
    """
    if type(in_data) is not dict:
        return "The input was not a dictionary.", 400
    expected_keys = ["name", "id", "blood_type"]
    expected_types = [str, int, str]
    for key, expected_type in zip(expected_keys, expected_types):
        if key not in in_data:
            error_message = "Key {} is missing".format(key)
            return error_message, 400
        if type(in_data[key]) is not expected_type:
            error_message = "Value of key {} is not of type {}"\
                .format(key, expected_type)
            return error_message, 400
    return True, 200


def add_patient_to_db(patient_name, id_no, blood_type):
    """Creates new patient database entry

    This function receives information about the patient, creates a new
    dictionary containing the patient information, and appends the diction to
    the database list.

    The dictionary for each patient will have the following format:
        {"name": <name_string>,
         "id": <id_int>,
         "blood_type": <string>,
         "tests": <dictionary>}

    Args:
        patient_name (str): name of patient
        id_no (int):  patient id number, usually a medical record number
        blood_type (str):  patient blood type, ex. "AB+"

    Returns:
        bool: True indicating that the patient was successfully saved to the
            database
    """

    new_patient = {"name": patient_name, "id": id_no,
                   "blood_type": blood_type, "tests": {}}
    db.append(new_patient)
    return True


@app.route("/get_results/<patient_id>", methods=["GET"])
def get_results_handler(patient_id):
    """ GET route to obtain database entry for a patient by id number

    This function implements a GET route with a variable URL.  The desired
    patient id number is included as part of the URL.  The function calls
    another function to implement the functionality and receives an
    answer and status code from that function, which it then returns.

    Args:
        patient_id (str): the patient id taken from the variable URL

    Returns:
        str, int: An error message if patient_id was invalid or a results
        string containing the patient data, plus a status code.
    """
    answer, status_code = get_results_driver(patient_id)
    return answer, status_code


def get_results_driver(patient_id):
    """ Implements the /get_results route to obtain database entry for a
    patient by id number

    This function implements the /get_results route.  The desired patient id
    number, which was part of the variable URL, is sent to this function as
    an argument.  The function then calls a validation function to ensure that
    the given id is an integer.  If the validation passes, the function calls
    another function to retrieve the test results for that patient id.  The
    answer and status code from that function are returned.

    Args:
        patient_id (str): the patient id taken from the variable URL
    Returns:
        str, int: An error message if patient_id was invalid or a results
        string containing the patient data, plus a status code.
    """

    answer, status_code = validate_convert_patient_id(patient_id)
    if status_code != 200:
        return answer, status_code
    answer, status_code = get_patient_tests_from_database(answer)
    return answer, status_code


def validate_convert_patient_id(patient_id):
    """Convert the patient id is an integer if possible

    The patient_id, received as a string, is checked to see if it contains an
    integer.  If it does, the string is converted to an integer and is returned
    with a status code of 200.  If the string does not an integer, an error
    message is returned with a status code of 400.

    Args:
        patient_id (str): the patient id string taken from the variable URL

    Returns:
        int or string, int: the patient id as an integer or an error
        message string; status code
    """
    try:
        patient_id_int = int(patient_id)
    except ValueError:
        return "Patient_id was not an integer", 400
    return patient_id_int, 200


def get_patient_tests_from_database(patient_id):
    """Retrieves test results for a patient from the database

    The database list of dictionaries is searched for the dictionary with
    the correct patient_id in the "id" key-value pair.  When found, the
    "test" value is returned with a 200 status code.  If the patient id is not
    found, an error message string and a 400 status code are returned

    Args:
        patient_id (int): the patient id to find in the database

    Returns:
        dict or string, int: A dictionary of test results if the patient id is
        found, otherwise an error string; status code

    """
    for patient in db:
        if patient["id"] == int(patient_id):
            return patient["tests"], 200
    return "Patient_id {} was not found".format(patient_id), 400


if __name__ == '__main__':
    init_server()
    app.run()
