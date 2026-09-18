from datetime import date, timedelta

from django.db.models import Avg, Count
from django.db.models.functions import TruncMonth

from .models import Doctor, MedicalRecord, Nurse, Patient


def task1_query():
    return Patient.objects.filter(date_admitted__date="2026-09-18")


def query2():
    return (
        Doctor.objects.filter(
            doctors__medical_records__diagnoses__icontains="Heart Disease"
        )
        .values("name")
        .distinct()
    )


def query3():
    return Patient.objects.filter(nurse__name="Ayesha")


def query4():
    return Patient.objects.filter(name="Hamza").values("doctor__contact_number")


def query5():
    return Patient.objects.count()


def query6():
    return Patient.objects.filter(nurse__isnull=True)


def query7():
    return Nurse.objects.filter(
        nurses__medical_records__prescription__icontains="Aspirin"
    )


def query8():
    return Patient.objects.aggregate(average_age=Avg("age"))


def query9():
    return Patient.objects.latest("date_admitted")


def query10():
    return Doctor.objects.annotate(patient_count=Count("doctors")).filter(
        patient_count__gt=5
    )


def query11():
    return Patient.objects.filter(
        date_admitted__date__lt=date.today() - timedelta(days=7)
    )


def query12():
    return Nurse.objects.annotate(patient_count=Count("nurses")).values(
        "name", "patient_count"
    )


def query13():
    return Patient.objects.filter(doctor__name="Dr. Ali").values("name")


def query14():
    return Doctor.objects.filter(specialization="Cardiology")


def query15():
    return Patient.objects.filter(doctor__specialization="Cardiology").values("name")


def query16():
    return Nurse.objects.annotate(patient_count=Count("nurses")).filter(patient_count=0)


def query17():
    return MedicalRecord.objects.filter(patient__name="Hamza").latest("id")


def query18():
    return (
        Patient.objects.filter(medical_records__diagnoses__icontains="Heart Disease")
        .values("name")
        .distinct()
    )


def query19():
    return Doctor.objects.filter(doctors__age__gt=50).values("name").distinct()


def query20():
    return Patient.objects.filter(
        medical_records__prescription__icontains="Aspirin"
    ).values("name")


def query21():
    return Nurse.objects.filter(nurses__age__gt=50).values("name").distinct()


def query22():
    return MedicalRecord.objects.count()


def query23():
    return Patient.objects.filter(nurse__contact_number="03331234567").values("name")


def query24():
    return Patient.objects.annotate(doctor_count=Count("doctor")).filter(
        doctor_count__gt=1
    )


def query25():
    return Doctor.objects.filter(
        doctors__medical_records__prescription__icontains="Aspirin"
    ).values("name")


def query26():
    return Patient.objects.filter(doctor__isnull=True)


def query27():
    return Doctor.objects.filter(doctors__date_admitted__date="2026-09-18").values(
        "name"
    )


def query28():
    return (
        Patient.objects.annotate(month=TruncMonth("date_admitted"))
        .values("month")
        .annotate(patient_count=Count("id"))
    )


def query29():
    return Patient.objects.order_by("-age").first()


def query30():
    return Nurse.objects.filter(nurses__date_admitted__date="2026-09-18").values("name")


def query31():
    return Doctor.objects.filter(doctors__age=60).values("name").distinct()


def query32():
    return Doctor.objects.annotate(patient_count=Count("doctors")).values(
        "name", "patient_count"
    )


def query33():
    return Patient.objects.filter(age=40).values("name")


def query34():
    return Nurse.objects.filter(
        nurses__medical_records__diagnoses__icontains="Heart Disease"
    ).values("name")


def query35():
    return Patient.objects.filter(nurse__contact_number="03331234567").values("name")


def query36():
    return Doctor.objects.filter(doctors__isnull=True)


def query37():
    return Patient.objects.filter(
        medical_records__prescription__icontains="Paracetamol"
    ).values("name")


def query38():
    return Doctor.objects.annotate(average_age=Avg("doctors__age")).values(
        "name", "average_age"
    )


def query39():
    return (
        Doctor.objects.filter(
            doctors__medical_records__prescription__icontains="Aspirin"
        )
        .values("name")
        .distinct()
    )


def query40():
    return Patient.objects.filter(doctor__contact_number="03001234567").values("name")


def query41():
    return (
        Nurse.objects.filter(nurses__medical_records__prescription__icontains="Aspirin")
        .values("name")
        .distinct()
    )


def query42():
    return Patient.objects.filter(doctor__specialization="Cardiology").count()


def query43():
    return Patient.objects.filter(nurse__isnull=True)


def query45():
    return (
        Patient.objects.filter(
            medical_records__diagnoses__icontains="Heart Disease",
            doctor__name="Dr. Ahmed",
        )
        .values("name")
        .distinct()
    )


def query46():
    return Nurse.objects.filter(nurses__age__gt=50).values("name").distinct()


def query47():
    return (
        Doctor.objects.filter(
            doctors__medical_records__diagnoses__icontains="Heart Disease",
            doctors__age__gt=50,
        )
        .values("name")
        .distinct()
    )


def query49():
    return Patient.objects.annotate(nurse_count=Count("nurse", distinct=True)).filter(
        nurse_count__gt=1
    )


def query50():
    return (
        Doctor.objects.filter(
            doctors__medical_records__diagnoses__icontains="Heart Disease",
            doctors__age__gt=50,
        )
        .values("name")
        .distinct()
    )
