from django import forms
from .models import (
    Patient, Doctor, Appointment, Billing, LabReport, 
    Staff, Bed, Medicine, Prescription, PrescriptionMedicine
)

# ========== PATIENT ==========
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'medical_history': forms.Textarea(attrs={'rows': 4}),
            'address': forms.Textarea(attrs={'rows': 3}),
        }

# ========== DOCTOR ==========
class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        widgets = {
            'qualification': forms.TextInput(attrs={'placeholder': 'MBBS, MD, etc.'}),
        }

# ========== APPOINTMENT ==========
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            'appointment_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'reason': forms.Textarea(attrs={'rows': 3}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }

# ========== BILLING ==========
class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = '__all__'
        widgets = {
            'total_amount': forms.NumberInput(attrs={'step': '0.01'}),
            'paid_amount': forms.NumberInput(attrs={'step': '0.01'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

# ========== LAB REPORT ==========
class LabReportForm(forms.ModelForm):
    class Meta:
        model = LabReport
        fields = '__all__'
        widgets = {
            'test_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'findings': forms.Textarea(attrs={'rows': 4}),
            'normal_range': forms.Textarea(attrs={'rows': 3}),
            'actual_values': forms.Textarea(attrs={'rows': 3}),
        }

# ========== STAFF ==========
class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'
        widgets = {
            'hire_date': forms.DateInput(attrs={'type': 'date'}),
            'salary': forms.NumberInput(attrs={'step': '0.01'}),
            'shift_timing': forms.TextInput(attrs={'placeholder': '9AM-5PM'}),
        }

# ========== BED ==========
class BedForm(forms.ModelForm):
    class Meta:
        model = Bed
        fields = '__all__'
        widgets = {
            'available_from': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

# ========== MEDICINE ==========
class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'
        widgets = {
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
            'price_per_unit': forms.NumberInput(attrs={'step': '0.01'}),
            'stock_quantity': forms.NumberInput(),
            'dosage': forms.TextInput(attrs={'placeholder': '1 tablet daily'}),
        }

# ========== PRESCRIPTION ==========
class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = '__all__'
        widgets = {
            'prescribed_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

# ========== PRESCRIPTION MEDICINE ==========
class PrescriptionMedicineForm(forms.ModelForm):
    class Meta:
        model = PrescriptionMedicine
        fields = '__all__'
        widgets = {
            'quantity': forms.NumberInput(),
            'instructions': forms.Textarea(attrs={'rows': 3}),
        }
