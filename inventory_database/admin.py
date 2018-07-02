from django.contrib import admin
from inventory_database.models import Employee, Fac, Student, Lab_Classroom, Software, Editor

# Register any models here.

class FacAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}
	
class StudentAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}

class SoftwareAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}
	


class EmployeeAdmin(admin.ModelAdmin):
	list_display = ('name', 'department', 'office')

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Fac, FacAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Lab_Classroom)
admin.site.register(Software, SoftwareAdmin)
admin.site.register(Editor)


