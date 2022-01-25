"""dosing.py
    Example program of calculating first-day dose of medicine for pediatric
        patients.
    NOTE:  This is a programming example, and should not be used for any
             type of medical treatment or diagnostics.
"""


def get_user_input_of_diagnosis():
    print("Day One Dosing Guidelines")
    print("")
    print("Choose diagnosis:")
    print("1 - Acute otitis media")
    print("2 - Acute bacterial sinusitis")
    print("3 - Community-acquired pneumonia")
    print("4 - Pharyngitis/tonsilitis")
    entry = input("Enter a number: ")
    return entry

    
def check_diagnosis_input(entry):
    try:
        diagnosis = int(entry)
    except ValueError:
        print("Must enter a number.")
        return False
    if diagnosis < 1 or diagnosis > 4:
        print("Entry must be between 1 and 4.")
        return False
    return diagnosis

    
def get_patient_weight():
    print("PATIENT WEIGHT")
    print("Enter patient weight followed by units of kg or lb.")
    print("Examples:  65.3 lb      21.0 kg")
    weight_input = input("Enter weight: ")
    return weight_input
    
    
def convert_lbs_to_kgs(weight_lbs):
    weight_kgs = weight_lbs / 2.205
    return weight_kgs


def parse_weight_input(weight_input):
    weight_data = weight_input.split(" ")
    weight = float(weight_data[0])
    units = weight_data[1]
    if units == "lb":
        weight - convert_lbs_to_kgs(weight)
    return weight


def analysis(weight, diagnosis):
    dosages_mg_per_kg = [30, 10, 10, 12]
    dosage_mg_per_kg = dosages_mg_per_kg[diagnosis-1]
    dosage_mg_first_day = weight * dosage_mg_per_kg
    return dosage_mg_first_day

    
def output(weight, dosage_mg_first_day):
    print("CORRECT DOSAGE")
    print("For a patient weighing {:.1f} kg,".format(weight))
    print("  the correct dosage is {:.1f} mg the first day"
          .format(dosage_mg_first_day))


def program_driver():
    good_entry = False
    while not good_entry:
        diagnosis_entry = get_user_input_of_diagnosis()
        diagnosis = check_diagnosis_input(diagnosis_entry)
        if diagnosis != False:
            good_entry = True
    weight_input = get_patient_weight()
    weight = parse_weight_input(weight_input)
    dosage_first_day_mg = analysis(weight, diagnosis)
    output(weight, dosage_first_day_mg)


if __name__ == '__main__':
    program_driver()