from patient import create_patient_resource
from base import send_resource_to_hapi_fhir, get_resource_from_hapi_fhir, get_resource_from_hapi_fhir_documento

if __name__ == "__main__":
    # Parámetros del paciente (se puede dejar algunos vacíos)
    family_name = "Doe"
    given_name = "John"
    birth_date = "1990-01-01"
    gender = "male"
    phone = None 
    documento = "12345678"


    # Crear y enviar el recurso de paciente
    patient = create_patient_resource(family_name, given_name, birth_date, gender, phone)
    patient_id = send_resource_to_hapi_fhir(patient, 'Patient')

    # Ver el recurso de paciente creado
    if patient_id:
        print("Obteniendo el recurso de paciente creado:")
        get_resource_from_hapi_fhir(patient_id,'Patient')

    if documento:
        print("Obteniendo el recurso de paciente por documento:")
        get_resource_from_hapi_fhir_documento(documento,'Patient')