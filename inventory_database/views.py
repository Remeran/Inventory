from django.shortcuts import render
from django.views.generic.edit import FormView
from django.http import HttpResponse
from registration.views import RegistrationView 
from inventory_database.models import Asset
from inventory_database.models import Fac
from inventory_database.models import Student
from inventory_database.models import Employee
from inventory_database.models import Hardware
from inventory_database.models import Editor
from inventory_database.models import Lab_Classroom
from inventory_database.models import Software
from inventory_database.models import Assign_Software
from inventory_database.forms import FacForm, EmployeeForm, Lab_ClassroomForm, StudentForm, SoftwareForm, SearchForm, UpdateFacForm, UpdateStudentForm, EditorForm, UpdateEmployeeForm, UpdateLab_ClassroomForm, UpdateSoftwareForm, Assigned_SoftwareForm

class UserProfileRegistration(RegistrationView):
	form_class = EditorForm

def index(request):
    
	inventory_count = Fac.objects.count() + Student.objects.count()
	employee_count = Employee.objects.count()
	fac_count = Fac.objects.count()
	student_count = Student.objects.count()
	lab_classroom_count = Lab_Classroom.objects.count()
	software_count = Software.objects.count()
	editor_list = Editor.objects.all().__str__()
	context_dict = {}
	context_dict['inv_count'] = inventory_count
	context_dict['emp_count'] = employee_count
	context_dict['fac_count'] = fac_count
	context_dict['student_count'] = student_count
	context_dict['lab_classroom_count'] = lab_classroom_count
	context_dict['software_count'] = software_count
	editor_list = Editor.objects.all().__str__()
	context_dict['editors'] = editor_list

	# Return a rendered response to send to the client.
	return render(request, 'inventory_database/index.html', context=context_dict)

def about(request):

	inventory_fac = Fac.objects.all()
	inventory_student = Student.objects.all()
	context_dict = {}
	context_dict['total'] = Fac.objects.count() + Student.objects.count()
	context_dict['inventory_fac'] = inventory_fac
	context_dict['inventory_student'] = inventory_student
	editor_list = Editor.objects.all().__str__()
	context_dict['editors'] = editor_list
	
	return render(request, 'inventory_database/about.html', context=context_dict)
	
def browse_employees(request):

	employees = Employee.objects.all()
	context_dict = {}
	editor_list = Editor.objects.all().__str__()
	context_dict['editors'] = editor_list
	context_dict['employees'] = employees
	
	return render(request, 'inventory_database/browse_employees.html', context=context_dict)
	
def browse_labs_classrooms(request):

	labs_classrooms = Lab_Classroom.objects.all()
	context_dict = {}
	editor_list = Editor.objects.all().__str__()
	context_dict['editors'] = editor_list
	context_dict['labs_classrooms'] = labs_classrooms
	return render(request, 'inventory_database/browse_labs_classrooms.html', context=context_dict)
	
def browse_software(request):

	software = Software.objects.all()
	context_dict = {}
	editor_list = Editor.objects.all().__str__()
	context_dict['editors'] = editor_list
	context_dict['software'] = software
	return render(request, 'inventory_database/browse_software.html', context=context_dict)


def show_asset(request, asset_name_slug):
	context_dict = {}
	#Check to see if Faculty or Student computer was sent to view
	if Fac.objects.filter(slug__icontains = asset_name_slug):
		# If so asset is a faculty computer 
		asset = Fac.objects.get(slug=asset_name_slug)
		is_fac = True
		if asset.assignee:
			employee = Employee.objects.get(id = asset.assignee.id)
			context_dict['employee'] = employee
		context_dict['is_fac'] = is_fac
		form = UpdateFacForm(instance=asset)
		
		if Assign_Software.objects.filter(faculty_computer__slug = asset_name_slug):
			software = Assign_Software.objects.filter(faculty_computer = asset)
			context_dict['software'] = software

		if request.method == 'POST':
			form = UpdateFacForm(request.POST, instance = asset)
			context_dict['form'] = form
			context_dict['Asset'] = asset

			if form.is_valid():
				form.save()
				return render(request, 'inventory_database/asset.html', context_dict)
			else:
				print(form.errors)	
		
	else:
		#Else it is a student computer
		asset = Student.objects.get(slug=asset_name_slug)
		is_fac = False
		room = Lab_Classroom.objects.get(room = asset.room.room)
		context_dict['room'] = room
		context_dict['is_fac'] = is_fac
		form = UpdateStudentForm(instance=asset)
		
		if Assign_Software.objects.filter(student_computer__slug = asset_name_slug):
			software = Assign_Software.objects.filter(student_computer = asset)
			context_dict['software'] = software

		if request.method == 'POST':
			form = UpdateStudentForm(request.POST, instance = asset)
			asset.dec()
			context_dict['form'] = form
			context_dict['Asset'] = asset

			if form.is_valid():
				computer = form.save(commit=True)
				computer.inc()
				return render(request, 'inventory_database/asset.html', context_dict)
			else:
				print(form.errors)	
	
	editor_list = Editor.objects.all().__str__()
	context_dict['editors'] = editor_list
	context_dict['Asset'] = asset
	context_dict['form'] = form
	return render(request, 'inventory_database/asset.html', context_dict)
	


def add_asset(request):
	form = FacForm()
	context_dict = {}
	editor_list = Editor.objects.all().__str__()
	context_dict['editors'] = editor_list
	context_dict['form'] = form

	if request.method == 'POST':
		form = FacForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print(form.errors)


	return render(request, 'inventory_database/add_asset.html', context_dict)
	
def search(request):
	form = SearchForm()
	context_dict = {}
	context_dict['form'] = form
	editor_list = Editor.objects.all().__str__()
	context_dict['editors'] = editor_list
	
	if request.method == 'POST':
		form = SearchForm(request.POST)
		context_dict = {}
		editor_list = Editor.objects.all().__str__()
		context_dict['editors'] = editor_list
		
		if form.is_valid():
			searchBy = form.cleaned_data['search_by']
			searchName = form.cleaned_data['searchName']
			searchSerial = form.cleaned_data['searchSerial']
			searchModel = form.cleaned_data['searchModel']
			searchManufacturer = form.cleaned_data['searchManufacturer']
			searchAssignee = form.cleaned_data['searchAssignee']
			searchRoom = form.cleaned_data['searchRoom']
			searchDateBegin = form.cleaned_data['searchDatebegin']
			searchDateEnd = form.cleaned_data['searchDateEnd']
			searchWarrantyBegin = form.cleaned_data['searchWarrantybegin']
			searchWarrantyEnd = form.cleaned_data['searchWarrantyEnd']
			
			inventory_fac = Fac.objects.all()
			inventory_student = Student.objects.all()
			
			if searchBy == '1':
				search_list1 = inventory_fac.filter(name__icontains = searchName)
				search_list2 = inventory_student.filter(name__icontains = searchName) 
				context_dict['total'] = search_list1.count() + search_list2.count()

			elif searchBy == '2':
				search_list1 = inventory_fac.filter(serial__icontains = searchSerial)
				search_list2 = inventory_student.filter(serial__icontains = searchSerial) 
				context_dict['total'] = search_list1.count() + search_list2.count()
				
			elif searchBy == '3':
				search_list1 = inventory_fac.filter(model__icontains = searchModel)
				search_list2 = inventory_student.filter(model__icontains = searchModel)
				context_dict['total'] = search_list1.count() + search_list2.count()
				
			elif searchBy == '4':
				search_list1 = inventory_fac.filter(manufacturer__icontains = searchManufacturer)
				search_list2 = inventory_student.filter(manufacturer__icontains = searchManufacturer)
				context_dict['total'] = search_list1.count() + search_list2.count()
				
			elif searchBy == '5':
				search_list1 = inventory_fac.filter(assignee__name__icontains = searchAssignee)
				search_list2 = {}
				context_dict['total'] = search_list1.count()
			
			elif searchBy == '6':
				search_list1 = inventory_student.filter(room__room__icontains = searchRoom)
				search_list2 = {}
				context_dict['total'] = search_list1.count()
			
			elif searchBy == '7':
				search_list1 = inventory_student.filter(date_assigned__range=(searchDateBegin, searchDateEnd))
				search_list2 = inventory_fac.filter(date_assigned__range=(searchDateBegin, searchDateEnd))
				context_dict['total'] = search_list1.count() + search_list2.count()
				
			elif searchBy == '8':
				search_list1 = inventory_student.filter(war_exp__range=(searchWarrantyBegin, searchWarrantyEnd))
				search_list2 = inventory_fac.filter(war_exp__range=(searchWarrantyBegin, searchWarrantyEnd))
				context_dict['total'] = search_list1.count() + search_list2.count()
				
			context_dict['inventory_fac'] = search_list1
			context_dict['inventory_student'] = search_list2
			print(searchBy)
			return render(request, 'inventory_database/about.html', context_dict)
		else:
			print(form.errors)
	return render(request, 'inventory_database/search.html', context_dict )
	
def student_lab(request):

	inventory_student = Student.objects.all()
	context_dict = {}
	editor_list = Editor.objects.all().__str__()
	context_dict['editors'] = editor_list
	context_dict['total'] = Student.objects.count()
	context_dict['inventory_student'] = inventory_student
	return render(request, 'inventory_database/about.html', context=context_dict)
	
def faculty_staff(request):

	inventory_fac = Fac.objects.all()
	context_dict = {}
	editor_list = Editor.objects.all().__str__()
	context_dict['editors'] = editor_list
	context_dict['total'] = Fac.objects.count()
	context_dict['inventory_fac'] = inventory_fac
	return render(request, 'inventory_database/about.html', context=context_dict)


	
def show_employee(request, employee_id_slug):
	context_dict = {}
	employee = Employee.objects.get(slug = employee_id_slug)
	editor_list = Editor.objects.all().__str__()
	form = UpdateEmployeeForm(instance=employee)
	context_dict['employee'] = employee
	context_dict['editors'] = editor_list
	
	if request.method == 'POST':
		form = UpdateEmployeeForm(request.POST, instance=employee)
		context_dict['form'] = form
		
		if form.is_valid():
			form.save(commit=True)
			return render(request, 'inventory_database/employee.html', context_dict)
	context_dict['form'] = form
	return render(request, 'inventory_database/employee.html', context_dict)
	
def show_room(request, room_name_slug):
	context_dict = {}
	room = Lab_Classroom.objects.get(slug = room_name_slug)
	editor_list = Editor.objects.all().__str__()
	form = UpdateLab_ClassroomForm(instance=room)
	context_dict['room'] = room
	context_dict['editors'] = editor_list
	
	if request.method == 'POST':
		form = UpdateLab_ClassroomForm(request.POST, instance=room)
		context_dict['form'] = form
		
		if form.is_valid():
			form.save(commit=True)
			return render(request, 'inventory_database/room.html', context_dict)
	context_dict['form'] = form
	return render(request, 'inventory_database/room.html', context_dict)
	
def show_software(request, software_slug):
	context_dict = {}
	software = Software.objects.get(slug = software_slug)
	software_list = Assign_Software.objects.filter(software = software)
	print(software_list)
	editor_list = Editor.objects.all().__str__()
	form = UpdateSoftwareForm(instance=software)
	context_dict['software'] = software
	context_dict['software_list'] = software_list
	context_dict['editors'] = editor_list
	
	if request.method == 'POST':
		form = UpdateSoftwareForm(request.POST, instance=software)
		context_dict['form'] = form
		
		if form.is_valid():
			form.save(commit=True)
			return render(request, 'inventory_database/software.html', context_dict)
	context_dict['form'] = form
	return render(request, 'inventory_database/software.html', context_dict)
	
def add_employee(request):
	form = EmployeeForm()
	context_dict = {}
	editor_list = Editor.objects.all().__str__()
	context_dict['editors'] = editor_list
	context_dict['form'] = form

	if request.method == 'POST':
		form = EmployeeForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print(form.errors)

	return render(request, 'inventory_database/add_employee.html', context_dict)
	
def add_student(request):
	form = StudentForm()
	context_dict = {}
	editor_list = Editor.objects.all().__str__()
	context_dict['editors'] = editor_list
	context_dict['form'] = form

	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			computer = form.save(commit=False)
			computer.inc()
			computer.save()
			return index(request)
		else:
			print(form.errors)


	return render(request, 'inventory_database/add_student.html', context_dict)
	
def add_software(request):
	form = SoftwareForm()
	context_dict = {}
	editor_list = Editor.objects.all().__str__()
	context_dict['editors'] = editor_list
	context_dict['form'] = form

	if request.method == 'POST':
		form = SoftwareForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print(form.errors)


	return render(request, 'inventory_database/add_software.html', context_dict)
	
def add_lab_classroom(request):
	form = Lab_ClassroomForm()
	context_dict = {}
	editor_list = Editor.objects.all().__str__()
	context_dict['editors'] = editor_list
	context_dict['form'] = form

	if request.method == 'POST':
		form = Lab_ClassroomForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print(form.errors)
	return render(request, 'inventory_database/add_lab_classroom.html', context_dict)
	

def delete_asset(request, asset_name_slug):
	context_dict = {}
	if Fac.objects.filter(slug__icontains = asset_name_slug):
		asset = Fac.objects.get(slug=asset_name_slug)
		context_dict['asset'] = asset
		asset.delete()
	elif Student.objects.filter(slug__icontains = asset_name_slug):
		asset = Student.objects.get(slug=asset_name_slug)
		context_dict['asset'] = asset
		asset.dec()
		asset.delete()
		
	elif Employee.objects.filter(slug__icontains = asset_name_slug):
		asset = Employee.objects.get(slug=asset_name_slug)
		context_dict['asset'] = asset
		asset.delete()

	return render(request, 'inventory_database/delete_asset.html', context_dict)	
	
def delete_software(request, id):
	context_dict = {}
	if Assign_Software.objects.filter(id__icontains = id):
		software = Assign_Software.objects.get(id=id)
		context_dict['software'] = software
		software.dec()
		software.delete()

	return render(request, 'inventory_database/delete_asset.html', context_dict)	
	
def assign_software(request):
	form = Assigned_SoftwareForm()
	context_dict = {}
	editor_list = Editor.objects.all().__str__()
	context_dict['editors'] = editor_list
	context_dict['form'] = form

	if request.method == 'POST':
		form = Assigned_SoftwareForm(request.POST)
		if form.is_valid():
			software = form.save(commit=False)
			software.inc()
			software.save()
			return index(request)
		else:
			print(form.errors)
	return render(request, 'inventory_database/assign_software.html', context_dict)