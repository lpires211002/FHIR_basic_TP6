from careteam import create_careteam_resource
from base import send_resource_to_hapi_fhir, get_resource_from_hapi_fhir

if __name__ == "__main__":
    
    # Parámetros del CareTeam
    name = "Equipo de Atención Primaria"
    subject_id = "52704718"   # ID del paciente ya creado
    category_text = "Primary Care"

#52740885
    participants = [
        {
            "role": "Médico tratante",
            "member": "Practitioner/52704791",
            "period_start": "2024-01-01"
        },
        {
            "role": "Enfermero",
            "member": "Practitioner/52740885",
            "period_start": "2024-06-01"
        }
        
    ]

    # Crear CareTeam
    careteam = create_careteam_resource(
        name=name,
        subject_id=subject_id,
        category_text=category_text,
        participants=participants
    )

    # Enviar a HAPI FHIR
    careteam_id = send_resource_to_hapi_fhir(careteam, 'CareTeam')

    # Ver el recurso creado
    if careteam_id:
        
        get_resource_from_hapi_fhir(careteam_id, 'CareTeam')
