import routes
from fastapi import FastAPI
from .routes import hospital, doctor, patient, staff, departement, appointment
from fastapi.middleware.cors import CORSMiddleware

# import .routes.doctor as doctor
# import .routes.patient as patient
# import .routes.staff as staff
# import .routes.departement as department
# import .routes.appointment as appointment

appp = FastAPI()

# Configurez les paramètres CORS
origins = ["*"]

appp.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

appp.include_router(hospital.hospital_router, prefix="/hospital", tags=["hospitals"])
appp.include_router(patient.patient_router, prefix="/patient", tags=["patients"])
appp.include_router(doctor.doctor_router, prefix="/doctor", tags=["doctors"])
appp.include_router(staff.staff_router, prefix="/staff", tags=["staff"])
appp.include_router(departement.dpt_router, prefix="/departement", tags=["departments"])
appp.include_router(appointment.apt_router, prefix="/appointment", tags=["appointments"])


@appp.get("/")
async def root():
    return {"message": "Welcome to the Hospital Management API"}
