from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.forms import model_to_dict
from app1.models import   Patient, Doctor, Appointment, Billing, LabReport, Staff, Bed, Medicine, Prescription, PrescriptionMedicine
from datetime import date
from app1.forms import PatientForm, DoctorForm, AppointmentForm, BillingForm,LabReportForm, StaffForm, BedForm, MedicineForm,PrescriptionForm, PrescriptionMedicineForm




# ========== DASHBOARD ==========
def dashboard(request):

    total_patients = Patient.objects.count()

    total_doctors = Doctor.objects.count()
    active_doctors = Doctor.objects.filter().count()
    total_appointments = Appointment.objects.count()
    todays_appointments = Appointment.objects.filter().count()
    total_beds = Bed.objects.count()
    available_beds = Bed.objects.filter(is_occupied=False).count()

    context = {
        'total_patients': total_patients,
        'total_doctors': total_doctors,
        'active_doctors': active_doctors,
        'total_appointments': total_appointments,
        'todays_appointments': todays_appointments,
        'total_beds': total_beds,
        'available_beds': available_beds,
    }

    return render(request, 'dashboard.html', context)





# ========== PATIENT ==========
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients/list.html', {'patients': patients})

def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient created successfully!')
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'patients/create.html', {'form': form})

def patient_detail(request, id):
    patient = get_object_or_404(Patient, id=id)
    return render(request, 'patients/detail.html', {'patient': patient})

def patient_update(request, id):
    patient = get_object_or_404(Patient, id=id)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient updated successfully!')
            return redirect('patient_list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patients/update.html', {'form': form})

def patient_delete(request, id):
    patient = get_object_or_404(Patient, id=id)
    if request.method == 'POST':
        patient.delete()
        messages.success(request, 'Patient deleted successfully!')
        return redirect('patient_list')
    return render(request, 'patients/delete.html', {'patient': patient})

# ========== DOCTOR ==========
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/list.html', {'doctors': doctors})

def doctor_create(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Doctor created successfully!')
            return redirect('doctor_list')
    else:
        form = DoctorForm()
    return render(request, 'doctors/create.html', {'form': form})

def doctor_update(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Doctor updated successfully!')
            return redirect('doctor_list')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'doctors/update.html', {'form': form})

def doctor_delete(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    if request.method == 'POST':
        doctor.delete()
        messages.success(request, 'Doctor deleted successfully!')
        return redirect('doctor_list')
    return render(request, 'doctors/delete.html', {'doctor': doctor})

# ========== APPOINTMENT ==========
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments/list.html', {'appointments': appointments})

def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment created successfully!')
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/create.html', {'form': form})

def appointment_update(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment updated successfully!')
            return redirect('appointment_list')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'appointments/update.html', {'form': form})

def appointment_delete(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    if request.method == 'POST':
        appointment.delete()
        messages.success(request, 'Appointment deleted successfully!')
        return redirect('appointment_list')
    return render(request, 'appointments/delete.html', {'appointment': appointment})

# ========== BILLING ==========
def billing_list(request):
    billings = Billing.objects.all()
    return render(request, 'billing/list.html', {'billings': billings})

def billing_create(request):
    if request.method == 'POST':
        form = BillingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Billing created successfully!')
            return redirect('billing_list')
    else:
        form = BillingForm()
    return render(request, 'billing/create.html', {'form': form})

# ========== LAB REPORT ==========
def labreport_list(request):
    labreports = LabReport.objects.all()
    return render(request, 'labreports/list.html', {'labreports': labreports})

def labreport_create(request):
    if request.method == 'POST':
        form = LabReportForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lab Report created successfully!')
            return redirect('labreport_list')
    else:
        form = LabReportForm()
    return render(request, 'labreports/create.html', {'form': form})

# ========== STAFF ==========
def staff_list(request):
    staff_list = Staff.objects.all()
    return render(request, 'staff/list.html', {'staff': staff_list})

def staff_create(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff created successfully!')
            return redirect('staff_list')
    else:
        form = StaffForm()
    return render(request, 'staff/create.html', {'form': form})

# ========== BED ==========
def bed_list(request):
    beds = Bed.objects.all()
    return render(request, 'beds/list.html', {'beds': beds})

def bed_create(request):
    if request.method == 'POST':
        form = BedForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bed created successfully!')
            return redirect('bed_list')
    else:
        form = BedForm()
    return render(request, 'beds/create.html', {'form': form})

# ========== MEDICINE ==========
def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, 'medicines/list.html', {'medicines': medicines})

def medicine_create(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medicine created successfully!')
            return redirect('medicine_list')
    else:
        form = MedicineForm()
    return render(request, 'medicines/create.html', {'form': form})

# ========== PRESCRIPTION ==========
def prescription_list(request):
    prescriptions = Prescription.objects.all()
    return render(request, 'prescriptions/list.html', {'prescriptions': prescriptions})

def prescription_create(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Prescription created successfully!')
            return redirect('prescription_list')
    else:
        form = PrescriptionForm()
    return render(request, 'prescriptions/create.html', {'form': form})
