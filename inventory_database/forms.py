from django import forms
from django.core.validators import MaxValueValidator
from inventory_database.models import Employee, Fac, Lab_Classroom, Asset, Hardware, Student, Software

class FacForm(forms.ModelForm):
	name = forms.CharField(max_length=128,
							help_text="Please enter the Asset's name.")
	serial = forms.CharField(max_length=128, help_text="Please enter Asset's Serial")
	manufacturer = forms.CharField(max_length=128, help_text="Please enter Asset's manufacturer")
	model = forms.CharField(max_length=128, help_text="Please enter Asset's Model")
	assignee = forms.ModelChoiceField(queryset=Employee.objects.all())
	
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)

	# An inline class to provide additional information on the form.
	class Meta:
		# Provide an association between the ModelForm and a model
		model = Fac
		fields = ('name', 'serial', 'manufacturer', 'model', 'assignee',)

class EmployeeForm(forms.ModelForm):
    id = forms.IntegerField(validators=[MaxValueValidator(9999999)])
    name = forms.CharField(max_length=128,
							help_text="Please enter the name of the assignee")
    title = forms.CharField(max_length=128, help_text="Please enter Employee's title")   
    department = forms.CharField(max_length=128, help_text="Please enter Employee's department")
    office = forms.CharField(max_length=128, help_text="Please enter Employee's office number")
	

    class Meta:

		model = Employee
		fields = ('id', 'name', 'title', 'department', 'office',)
		
class FacForm(forms.ModelForm):
	name = forms.CharField(max_length=128,
							help_text="Please enter the Asset's name.")
	serial = forms.CharField(max_length=128, help_text="Please enter Asset's Serial")
	manufacturer = forms.CharField(max_length=128, help_text="Please enter Asset's manufacturer")
	model = forms.CharField(max_length=128, help_text="Please enter Asset's Model")
	war_exp = forms.DateField(help_text="Please enter Warranty Expiration date")
	date_assigned = forms.DateField(help_text="Please enter assignment date")
	assignee = forms.ModelChoiceField(queryset=Employee.objects.all())
	
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

	class Meta:
		model = Lab_Classroom
		fields = ('room', 'building', 'dept',)
		
class StudentForm(forms.ModelForm):
	name = forms.CharField(max_length=128,
							help_text="Please enter the Asset's name.")
	serial = forms.CharField(max_length=128, help_text="Please enter Asset's Serial")
	manufacturer = forms.CharField(max_length=128, help_text="Please enter Asset's manufacturer")
	model = forms.CharField(max_length=128, help_text="Please enter Asset's Model")
	war_exp = forms.DateField(help_text="Please enter Warranty Expiration date")
	date_assigned = forms.DateField(help_text="Please enter assignment date")
	room = forms.ModelChoiceField(queryset=Lab_Classroom.objects.all())
	
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)

	# An inline class to provide additional information on the form.
	class Meta:
		# Provide an association between the ModelForm and a model
		model = Student
		fields = ('name', 'serial', 'manufacturer', 'model', 'war_exp', 'date_assigned', 'room',)
		
class SoftwareForm(forms.ModelForm):
	name = forms.CharField(max_length=128,
							help_text="Please enter the Asset's name.")
	developer = forms.CharField(max_length=128, help_text="Please enter the developer")
	lic_exp = forms.DateField(help_text="Please enter license expiration date")
	assigned_dept = forms.CharField(max_length=128, help_text="Please enter assigned department")
	license_type = forms.CharField(max_length=128, help_text="Please enter license type")
	license_used = forms.IntegerField()
	
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)

	# An inline class to provide additional information on the form.
	class Meta:
		# Provide an association between the ModelForm and a model
		model = Software
		fields = ('name', 'developer', 'lic_exp', 'assigned_dept', 'license_type', 'license_used',)