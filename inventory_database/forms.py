from django import forms
from registration.forms import RegistrationFormUniqueEmail
from django.core.validators import MaxValueValidator
from inventory_database.models import Employee, Fac, Lab_Classroom, Asset, Hardware, Student, Software



class EmployeeForm(forms.ModelForm):
	id = forms.IntegerField(validators=[MaxValueValidator(9999999)], help_text="(Required: please enter the user's ID number) Employee ID:")
	name = forms.CharField(max_length=128,
							help_text="Employee Name:")
	title = forms.CharField(max_length=128, help_text="Employee Title")   
	department = forms.CharField(max_length=128, help_text="Employee Department:")
	office = forms.CharField(max_length=128, help_text="Employee Office:")
	
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)
	

	class Meta:

		model = Employee
		fields = ('id', 'name', 'title', 'department', 'office',)
		
class FacForm(forms.ModelForm):
	name = forms.CharField(max_length=128,
							help_text="Computer Name:")
	serial = forms.CharField(max_length=128, help_text="Serial:")
	manufacturer = forms.CharField(max_length=128, help_text="Manufacturer:")
	model = forms.CharField(max_length=128, help_text="Model")
	war_exp = forms.DateField(widget=forms.SelectDateWidget(years=range(2000, 2050)), help_text="Warranty Expiration date:")
	date_assigned = forms.DateField(widget=forms.SelectDateWidget(years=range(2000, 2050)),help_text="Assignment date:")

	assignee = forms.ModelChoiceField(queryset=Employee.objects.all(), required=False, help_text="Assignee:")
	
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)

	# An inline class to provide additional information on the form.
	class Meta:
		# Provide an association between the ModelForm and a model
		model = Fac
		fields = ('name', 'serial', 'manufacturer', 'model', 'war_exp', 'date_assigned', 'assignee',)
		
class Lab_ClassroomForm(forms.ModelForm):
	room = forms.CharField(max_length=128, help_text="Please enter Lab/Classroom number")
	comp_count = forms.IntegerField(widget=forms.HiddenInput(), required=False)
	building = forms.CharField(max_length=128, help_text="Please enter Lab/Classroom location")
	dept = forms.CharField(max_length=128, help_text="Please enter school in charge of lab")
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)

	class Meta:
		model = Lab_Classroom
		fields = ('room', 'building', 'dept',)
		
class StudentForm(forms.ModelForm):
	name = forms.CharField(max_length=128,
							help_text="Computer Name: ")
	serial = forms.CharField(max_length=128, help_text="Serial: ")
	manufacturer = forms.CharField(max_length=128, help_text="Manufacturer: ")
	model = forms.CharField(max_length=128, help_text="Model: ")
	war_exp = forms.DateField(widget=forms.SelectDateWidget(years=range(2000, 2050)), help_text="Warranty Expiration Date: ")
	date_assigned = forms.DateField(widget=forms.SelectDateWidget(years=range(2000, 2050)), help_text="Assignment Date")
	room = forms.ModelChoiceField(queryset=Lab_Classroom.objects.all(), help_text="Room: ")
	
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)

	# An inline class to provide additional information on the form.
	class Meta:
		# Provide an association between the ModelForm and a model
		model = Student
		fields = ('name', 'serial', 'manufacturer', 'model', 'war_exp', 'date_assigned', 'room',)
		
class SoftwareForm(forms.ModelForm):
	name = forms.CharField(max_length=128,
							help_text="Name: ")
	developer = forms.CharField(max_length=128, help_text="Developer")
	lic_exp = forms.DateField(widget=forms.SelectDateWidget(years=range(2000, 2050)),help_text="License Expiration Date: ")
	assigned_dept = forms.CharField(max_length=128, help_text="Department: ")
	license_type = forms.CharField(max_length=128, help_text="Type: ")
	license_used = forms.IntegerField(help_text="Used: ")
	
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)

	# An inline class to provide additional information on the form.
	class Meta:
		# Provide an association between the ModelForm and a model
		model = Software
		fields = ('name', 'developer', 'lic_exp', 'assigned_dept', 'license_type', 'license_used',)
		
class SearchForm(forms.ModelForm):
	search_by = forms.ChoiceField(choices=Asset.SEARCH_CHOICES, 
								 help_text="Search By: ")
	searchName = forms.CharField(required=False, max_length=128,
							 help_text="Search (leave blank to browse by category):")
							 
	searchSerial = forms.CharField(required=False, max_length=128,
							 help_text="Search by Serial:")
							 
	searchModel = forms.CharField(required=False, max_length=128,
							 help_text="Search by Model:")
							 
	searchManufacturer = forms.CharField(required=False, max_length=128,
							 help_text="Search by manufacturer:")
							 
	searchAssignee = forms.CharField(required=False, max_length=128,
							 help_text="Search by Assignee:")
							 
	searchRoom = forms.CharField(required=False, max_length=128,
							 help_text="Search by Room:")
							 
	searchDatebegin = forms.DateField(widget=forms.SelectDateWidget(years=range(2000, 2050)), required=False,
							 help_text="Date Starting: ")
							 
	searchDateEnd = forms.DateField(widget=forms.SelectDateWidget(years=range(2000, 2050)), required=False,
							 help_text="Date End: ")
	searchWarrantybegin = forms.DateField(widget=forms.SelectDateWidget(years=range(2000, 2050)), required=False,
							 help_text="Date Starting: ")
							 
	searchWarrantyEnd = forms.DateField(widget=forms.SelectDateWidget(years=range(2000, 2050)), required=False,
							 help_text="Date End: ")
	
	class Meta:
		model = Asset
		fields = ('search_by','searchName', 'searchSerial', 'searchModel', 'searchManufacturer', 'searchAssignee', 'searchRoom', 'searchDatebegin', 'searchDateEnd', 'searchWarrantybegin', 'searchWarrantyEnd',  )

class UpdateFacForm(forms.ModelForm):
	serial = forms.CharField(max_length=128, help_text="Serial")
	manufacturer = forms.CharField(max_length=128, help_text="Manufacturer")
	model = forms.CharField(max_length=128, help_text="Model")
	war_exp = forms.DateField(widget=forms.SelectDateWidget(), help_text="Warranty Expiration date")
	date_assigned = forms.DateField(widget=forms.SelectDateWidget(years=range(2000, 2050)),help_text="Assignment date:")
	assignee = forms.ModelChoiceField(queryset=Employee.objects.all(), required=False, help_text="Assignee")
	# An inline class to provide additional information on the form.
	class Meta:
		# Provide an association between the ModelForm and a model
		model = Fac
		fields = ('assignee', 'date_assigned', 'war_exp', 'model', 'manufacturer', 'serial')
		
class UpdateStudentForm(forms.ModelForm):
	serial = forms.CharField(max_length=128, help_text="Please enter Asset's Serial")
	manufacturer = forms.CharField(max_length=128, help_text="Please enter Asset's manufacturer")
	model = forms.CharField(max_length=128, help_text="Please enter Asset's Model")
	war_exp = forms.DateField(widget=forms.SelectDateWidget(years=range(2000, 2050)), help_text="Please enter Warranty Expiration date")
	date_assigned = forms.DateField(widget=forms.SelectDateWidget(years=range(2000, 2050)),help_text="Assignment date:")
	room = forms.ModelChoiceField(queryset=Lab_Classroom.objects.all(), help_text="Location")
	# An inline class to provide additional information on the form.
	class Meta:
		# Provide an association between the ModelForm and a model
		model = Fac
		fields = ('assignee', 'room', 'war_exp', 'model', 'manufacturer', 'serial')
		
class EditorForm(RegistrationFormUniqueEmail):
    is_editor = forms.BooleanField(initial=False, help_text="Check to add user to Editors")
	
class UpdateEmployeeForm(forms.ModelForm):
    id = forms.IntegerField(validators=[MaxValueValidator(9999999)])
    title = forms.CharField(max_length=128, help_text="Please enter Employee's title")   
    department = forms.CharField(max_length=128, help_text="Please enter Employee's department")
    office = forms.CharField(max_length=128, help_text="Please enter Employee's office number")
	

    class Meta:

		model = Employee
		fields = ('id', 'title', 'department', 'office',)
		
class UpdateLab_ClassroomForm(forms.ModelForm):
	building = forms.CharField(max_length=128, help_text="Please enter Lab/Classroom location")
	dept = forms.CharField(max_length=128, help_text="Please enter school in charge of lab")

	class Meta:
		model = Lab_Classroom
		fields = ('building', 'dept',)