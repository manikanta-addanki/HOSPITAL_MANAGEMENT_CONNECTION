from django.contrib import admin
from .models import Patient, Doctor, Appointment, Billing, LabReport, Staff, Bed, Medicine, Prescription, PrescriptionMedicine

# ========== Patient Admin ==========
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'gender', 'created_at']
    list_filter = ['gender', 'created_at']
    search_fields = ['first_name', 'last_name', 'phone']
    readonly_fields = ['created_at']

# ========== Doctor Admin ==========
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'specialty', 'is_available', 'consultation_fee']
    list_filter = ['specialty', 'is_available']
    search_fields = ['first_name', 'last_name', 'qualification']
    list_editable = ['is_available']

# ========== Appointment Admin ==========
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor', 'appointment_date', 'status', 'created_at']
    list_filter = ['status', 'appointment_date', 'doctor__specialty']
    search_fields = ['patient__first_name', 'patient__last_name', 'doctor__first_name']
    list_per_page = 25
    date_hierarchy = 'appointment_date'
    readonly_fields = ['created_at']

# ========== Billing Admin ==========
@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display = ['patient', 'total_amount', 'paid_amount', 'payment_status', 'billing_date']
    list_filter = ['payment_status', 'billing_date']
    search_fields = ['patient__first_name', 'patient__last_name']
    readonly_fields = ['billing_date']

# ========== Prescription Medicine Inline ==========
class PrescriptionMedicineInline(admin.TabularInline):
    model = PrescriptionMedicine
    extra = 0

# ========== Lab Report Admin ==========
@admin.register(LabReport)
class LabReportAdmin(admin.ModelAdmin):
    list_display = ['patient', 'test_type', 'test_date', 'result_status', 'doctor_reviewed']
    list_filter = ['test_type', 'result_status', 'test_date']
    search_fields = ['patient__first_name', 'patient__last_name']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'test_date'

# ========== Staff Admin ==========
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'role', 'department', 'is_active', 'employee_id']
    list_filter = ['role', 'department', 'is_active']
    search_fields = ['first_name', 'last_name', 'employee_id']
    list_editable = ['is_active']

# ========== Bed Admin ==========
@admin.register(Bed)
class BedAdmin(admin.ModelAdmin):
    list_display = ['bed_number', 'bed_type', 'room_number', 'is_occupied', 'current_patient']
    list_filter = ['bed_type', 'is_occupied']
    search_fields = ['bed_number', 'room_number', 'current_patient__first_name']
    list_editable = ['is_occupied']

# ========== Medicine Admin ==========
@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ['name', 'stock_quantity', 'price_per_unit', 'expiry_date']
    list_filter = ['expiry_date']
    search_fields = ['name', 'generic_name']
    list_editable = ['stock_quantity']

# ========== Prescription Admin ==========
@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ['appointment', 'prescribed_by', 'prescribed_date']
    list_filter = ['prescribed_date', 'prescribed_by']
    inlines = [PrescriptionMedicineInline]
    readonly_fields = ['prescribed_date']

# ========== PrescriptionMedicine Admin ==========
@admin.register(PrescriptionMedicine)
class PrescriptionMedicineAdmin(admin.ModelAdmin):
    list_display = ['prescription', 'medicine', 'quantity']
    search_fields = ['prescription__appointment__patient__first_name', 'medicine__name']
