from base import send_resource_to_hapi_fhir

practitioner = {
    "resourceType": "Practitioner",
    "name": [{
        "family": "Pires",
        "given": ["Tobias"]
    }]
}

pr_id = send_resource_to_hapi_fhir(practitioner, "Practitioner")
print("Practitioner creado con ID:", pr_id) 
