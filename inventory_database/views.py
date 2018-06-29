from django.shortcuts import render
from django.views.generic.edit import FormView
from django.http import HttpResponse
from inventory_database.models import Asset
from inventory_database.models import Fac
from inventory_database.models import Student
from inventory_database.models import Employee
from inventory_database.models import Hardware
from inventory_database.forms import FacForm, EmployeeForm, Lab_ClassroomForm, StudentForm, SoftwareForm, SearchForm, UpdateFacForm

def index(request):
    
    inventory_count = Fac.objects.count() + Student.objects.count()
    employee_count = Employee.objects.count()
    fac_count = Fac.objects.count()
    student_count = Student.objects.count()
    context_dict = {}
    context_dict['inv_count'] = inventory_count
    context_dict['emp_count'] = employee_count
    context_dict['fac_count'] = fac_count
    context_dict['student_count'] = student_count

    # Return a rendered response to send to the client.
    return render(request, 'inventory_database/index.html', context=context_dict)

def about(request):

    inventory_fac = Fac.objects.all()
    inventory_student = Student.objects.all()
    context_dict = {}
    context_dict['inventory_fac'] = inventory_fac
    context_dict['inventory_student'] = inventory_student
    return render(request, 'inventory_database/about.html', context=context_dict)

def show_asset(request, asset_name_slug):
    context_dict = {}
    asset = Fac.objects.get(slug=asset_name_slug)
    context_dict['Asset'] = asset
	
    if request.method == 'POST':
		form = UpdateFacForm(request.POST, instance = asset)
		context_dict['form'] = form
		if form.is_valid():
			form.save(commit=True)
			return render(request, 'inventory_database/asset.html', context_dict)
		else:
			print(form.errors)
    else:
		print("Is GET")
		form = UpdateFacForm(instance=asset)
		context_dict['form'] = form
		return render(request, 'inventory_database/asset.html', context_dict)
	


def add_asset(request):
    form = FacForm()

    if request.method == 'POST':
        form = FacForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
		
            form.save(commit=True)
            # Now that the asset is saved
            # We could give a confirmation message
            # Then we can direct the user back to the index page.
            return index(request)
        else:
            # The supplied form contained errors -
            # just print them to the terminal.
            print(form.errors)

    # Will handle the bad form, new form, or no form supplied cases.
    # Render the form with error messages (if any).
    return render(request, 'inventory_database/add_asset.html', {'form': form})
	
def search(request):
	form = SearchForm()
	
	if request.method == 'POST':
		form = SearchForm(request.POST)
		context_dict = {}
		
		if form.is_valid():
			searchBy = form.cleaned_data['search_by']
			searchName = form.cleaned_data['searchName']
			searchSerial = form.cleaned_data['searchSerial']
			searchModel = form.cleaned_data['searchModel']
			searchManufacturer = form.cleaned_data['searchManufacturer']
			searchAssignee = form.cleaned_data['searchAssignee']
			searchRoom = form.cleaned_data['searchRoom']
			
			inventory_fac = Fac.objects.all()
			inventory_student = Student.objects.all()
			
			if searchBy == '1':
				search_list1 = inventory_fac.filter(name__icontains = searchName)
				search_list2 = inventory_student.filter(name__icontains = searchName) 

			elif searchBy == '2':
				search_list1 = inventory_fac.filter(serial__icontains = searchSerial)
				search_list2 = inventory_student.filter(serial__icontains = searchSerial) 
				
			elif searchBy == '3':
				search_list1 = inventory_fac.filter(model__icontains = searchModel)
				search_list2 = inventory_student.filter(model__icontains = searchModel)
				
			elif searchBy == '4':
				search_list1 = inventory_fac.filter(manufacturer__icontains = searchManufacturer)
				search_list2 = inventory_student.filter(manufacturer__icontains = searchManufacturer)
				
			elif searchBy == '5':
				search_list1 = inventory_fac.filter(assignee__name__icontains = searchAssignee)
				search_list2 = {}
			
			elif searchBy == '6':
				search_list1 = inventory_student.filter(room__room__icontains = searchRoom)
				search_list2 = {}
				
			context_dict['inventory_fac'] = search_list1
			context_dict['inventory_student'] = search_list2
			print(searchBy)
			return render(request, 'inventory_database/about.html', context_dict)
		else:
			print(form.errors)
	return render(request, 'inventory_database/search.html', {'form': form} )
	
def student_lab(request):

    inventory_student = Student.objects.all()
    context_dict = {}
    context_dict['inventory_student'] = inventory_student
    return render(request, 'inventory_database/about.html', context=context_dict)
	
def faculty_staff(request):

    inventory_fac = Fac.objects.all()
    context_dict = {}
    context_dict['inventory_fac'] = inventory_fac
    return render(request, 'inventory_database/about.html', context=context_dict)
	