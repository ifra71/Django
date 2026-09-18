from django.db import models


class Doctor(models.Model):

    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Nurse(models.Model):

    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Patient(models.Model):

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="doctors")
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE, related_name="nurses")

    date_admitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Hospital(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="patients"
    )
    doctor = models.ManyToManyField(Doctor)
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)

    def __str__(self):
        return f"Hospital - {self.patient.name}"


class MedicalRecord(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="medical_records"
    )
    diagnoses = models.TextField()
    prescription = models.TextField()

    def __str__(self):
        return f"Medical Record - {self.patient.name}"
