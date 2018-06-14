from django import forms
from inventory_database.models import Employee, Fac

class FacForm(forms.ModelForm):
	name = forms.CharField(max_length=128,
							help_text="Please enter the Asset's name.")
	serial = forms.CharField(max_length=128, help_text="Please enter Asset's Serial")
	manufacturer = forms.CharField(max_length=128, help_text="Please enter Asset's manufacturer")
	model = forms.CharField(max_length=128, help_text="Please enter Asset's Model")
	employee = forms.ModelChoiceField(queryset=Employee.objects.all())
	
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)

	# An inline class to provide additional information on the form.
	class Meta:
		# Provide an association between the ModelForm and a model
		model = Fac
		fields = ('name', 'serial', 'manufacturer', 'model', 'employee',)

class EmployeeForm(forms.ModelForm):
	name = forms.CharField(max_length=128,
							help_text="Please enter the name of the employee")
	department = forms.CharField(max_length=128, help_text="Please enter Employee's department")
	office = forms.CharField(max_length=128, help_text="Please enter Employee's office number")
	

	class Meta:
		# Provide an association between the ModelForm and a model
		model = Employee

		# What fields do we want to include in our form?
		# This way we don't need every field in the model present.
		# Some fields may allow NULL values, so we may not want to include them.
		# Here, we are hiding the foreign key.
		# we can either exclude the category field from the form,
		fields = ('name', 'department', 'office',)
		# or specify the fields to include (i.e. not include the category field)
		#fields = ('title', 'url', 'views')