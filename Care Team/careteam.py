from fhir.resources.careteam import CareTeam
from fhir.resources.humanname import HumanName
from fhir.resources.reference import Reference
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.coding import Coding
from fhir.resources.period import Period

def create_careteam_resource(name=None, subject_id=None, status="active", category_text=None, participants=None):
    """
    Crea un recurso FHIR CareTeam.

    Params:
        name (str): Nombre del equipo
        subject_id (str): ID del paciente asociado (Patient/{id})
        status (str): Estado del CareTeam (active, proposed, etc.)
        category_text (str): Texto de categoría
        participants (list): Lista de diccionarios con info de cada miembro. Ej:
            [
                {
                    "role": "primary care physician",
                    "member": "Practitioner/123",
                    "period_start": "2020-01-01",
                    "period_end": None
                }
            ]
    """

    careteam = CareTeam()

    # Nombre del equipo
    if name:
        careteam.name = name

    # Estado del equipo
    careteam.status = status

    # Paciente asociado
    if subject_id:
        careteam.subject = Reference(reference=f"Patient/{subject_id}")

    # Categoría opcional
    if category_text:
        careteam.category = [
            CodeableConcept(
                text=category_text
            )
        ]

    # Participantes del equipo
    if participants:
        careteam.participant = []
        for p in participants:
            participant_entry = {
                "role": [
                    CodeableConcept(
                        coding=[Coding(code="member")],
                        text=p.get("role")
                    )
                ],
                "member": Reference(reference=p.get("member"))
            }

            # Período opcional
            if p.get("period_start") or p.get("period_end"):
                participant_entry["period"] = Period(
                    start=p.get("period_start"),
                    end=p.get("period_end")
                )

            careteam.participant.append(participant_entry)

    return careteam
