from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    address = models.TextField()
    emergency_contact = models.CharField(max_length=50)
    medical_history = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Doctor(models.Model):
    SPECIALTY_CHOICES = [
        ('GP', 'General Practitioner'),
        ('CAR', 'Cardiologist'),
        ('DER', 'Dermatologist'),
        ('PED', 'Pediatrician'),
        ('SUR', 'Surgeon'),
    ]

   
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    specialty = models.CharField(max_length=10, choices=SPECIALTY_CHOICES)
    phone = models.CharField(max_length=15)
    qualification = models.CharField(max_length=100)
    experience_years = models.IntegerField(default=0)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} - {self.get_specialty_display()}"


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('SCHEDULED', 'Scheduled'),
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
        ('COMPLETED', 'Completed'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateTimeField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='SCHEDULED')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['patient', 'doctor', 'appointment_date'], name='unique_appointment')
        ]

    def __str__(self):
        return f"{self.patient} with Dr. {self.doctor} on {self.appointment_date}"


class Billing(models.Model):
    PAYMENT_STATUS = [
        ('PENDING', 'Pending'),
        ('PAID', 'Paid'),
        ('PARTIAL', 'Partial'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='billings')
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, null=True, blank=True, related_name='billings')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS, default='PENDING')
    billing_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Billing for {self.patient} - ₹{self.total_amount}"


class LabReport(models.Model):
    TEST_TYPES = [
        ('BLOOD', 'Blood Test'),
        ('URINE', 'Urine Test'),
        ('XRAY', 'X-Ray'),
        ('MRI', 'MRI'),
        ('CTSCAN', 'CT Scan'),
        ('ULTRASOUND', 'Ultrasound'),
        ('PATHOLOGY', 'Pathology'),
    ]

    RESULT_STATUS = [
        ('PENDING', 'Pending'),
        ('NORMAL', 'Normal'),
        ('ABNORMAL', 'Abnormal'),
        ('CRITICAL', 'Critical'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='lab_reports')
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, null=True, blank=True, related_name='lab_reports')
    test_type = models.CharField(max_length=20, choices=TEST_TYPES)
    test_date = models.DateTimeField()
    result_status = models.CharField(max_length=15, choices=RESULT_STATUS, default='PENDING')
    report_file = models.FileField(upload_to='lab_reports/', blank=True)
    findings = models.TextField()
    normal_range = models.TextField(blank=True)
    actual_values = models.TextField()
    doctor_reviewed = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviewed_reports')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient} - {self.get_test_type_display()} ({self.test_date})"


class Staff(models.Model):
    ROLE_CHOICES = [
        ('NURSE', 'Nurse'),
        ('RECEPTIONIST', 'Receptionist'),
        ('LAB_TECH', 'Lab Technician'),
        ('PHARMACIST', 'Pharmacist'),
        ('ADMIN', 'Administrator'),
    ]

    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=50)
    employee_id = models.CharField(max_length=20, unique=True)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    shift_timing = models.CharField(max_length=50)  # "9AM-5PM", "Night Shift"
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.get_role_display()}"


class Bed(models.Model):
    BED_TYPES = [
        ('GENERAL', 'General Ward'),
        ('ICU', 'ICU'),
        ('PRIVATE', 'Private Room'),
        ('EMERGENCY', 'Emergency'),
    ]

    bed_number = models.CharField(max_length=10, unique=True)
    bed_type = models.CharField(max_length=20, choices=BED_TYPES)
    room_number = models.CharField(max_length=10)
    is_occupied = models.BooleanField(default=False)
    current_patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True, blank=True, related_name='current_bed')
    assigned_staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_beds')
    available_from = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Bed {self.bed_number} - {self.get_bed_type_display()}"


class Medicine(models.Model):
    name = models.CharField(max_length=100)
    generic_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    price_per_unit = models.DecimalField(max_digits=8, decimal_places=2)
    stock_quantity = models.IntegerField(default=0)
    expiry_date = models.DateField()
    manufacturer = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.generic_name})"


class Prescription(models.Model):
    lab_report = models.ForeignKey(LabReport, on_delete=models.CASCADE, null=True, blank=True, related_name='prescriptions')
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='prescriptions')
    medicines = models.ManyToManyField(Medicine, through='PrescriptionMedicine')
    prescribed_by = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='prescriptions')
    prescribed_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription for {self.appointment.patient} by Dr. {self.prescribed_by}"


class PrescriptionMedicine(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, related_name='prescription_medicines')
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='prescriptions')
    quantity = models.IntegerField()
    instructions = models.TextField(blank=True)

    def __str__(self):
        return f"{self.quantity} x {self.medicine.name}"
