import requests
import json

def send_resource_to_hapi_fhir(resource, resource_type):
    url = f"http://hapi.fhir.org/baseR4/{resource_type}"
    headers = {"Content-Type": "application/fhir+json"}

    # Si es dict → serializar manualmente
    if isinstance(resource, dict):
        resource_json = json.dumps(resource)
    else:
        resource_json = resource.json()

    response = requests.post(url, headers=headers, data=resource_json)

    if response.status_code == 201:
        print("Recurso creado exitosamente")
        return response.json()['id']
    else:
        print(f"Error al crear el recurso: {response.status_code}")
        print(response.json())
        return None


# Buscar el recurso por ID
def get_resource_from_hapi_fhir(resource_id, resource_type):
    url = f"http://hapi.fhir.org/baseR4/{resource_type}/{resource_id}"
    response = requests.get(url, headers={"Accept": "application/fhir+json"})

    if response.status_code == 200:
        resource = response.json()
        print(resource)
    else:
        print(f"Error al obtener el recurso: {response.status_code}")
        try:
            print(response.json())
        except:
            print("Respuesta no JSON:", response.text)

    return None


# Buscar por identificador (útil para Patient, Practitioner, Organization...)
def get_resource_from_hapi_fhir_documento(documento, resource_type):
    url = f"http://hapi.fhir.org/baseR4/{resource_type}?identifier={documento}"
    response = requests.get(url, headers={"Accept": "application/fhir+json"})

    if response.status_code == 200:
        resource = response.json()
        print(resource)
    else:
        print(f"Error al obtener el recurso: {response.status_code}")
        try:
            print(response.json())
        except:
            print("Respuesta no JSON:", response.text)

    return None


# Búsqueda genérica por parámetros (opcional pero útil)
def search_resources(params, resource_type):
    """
    params = {"patient": "123", "status": "active"}  -> genera ?patient=123&status=active
    """
    query = "&".join([f"{k}={v}" for k, v in params.items()])
    url = f"http://hapi.fhir.org/baseR4/{resource_type}?{query}"

    response = requests.get(url, headers={"Accept": "application/fhir+json"})

    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        print(f"Error en la búsqueda: {response.status_code}")
        try:
            print(response.json())
        except:
            print("Respuesta no JSON:", response.text)
        return None
