from django.shortcuts import render
from django.http import HttpResponse
from inventory_database.models import Asset
from inventory_database.models import Fac
from inventory_database.models import Employee
from inventory_database.forms import FacForm, EmployeeForm, Lab_ClassroomForm, StudentForm, SoftwareForm, SearchForm

def index(request):
    
    inventory_count = Fac.objects.count()
    employee_count = Employee.objects.count()
    IT_inv_count = Fac.objects.filter(assignee__department="Information Technology").count()
    HR_inv_count = Fac.objects.filter(assignee__department="Human Resources").count()
    context_dict = {}
    context_dict['inv_count'] = inventory_count
    context_dict['emp_count'] = employee_count
    context_dict['IT_inv_count'] = IT_inv_count
    context_dict['HR_inv_count'] = HR_inv_count

    # Return a rendered response to send to the client.
    return render(request, 'inventory_database/index.html', context=context_dict)

def about(request):

    inventory = Fac.objects.all()
    context_dict = {}
    context_dict['inventory'] = inventory
    return render(request, 'inventory_database/about.html', context=context_dict)

def show_asset(request, asset_name_slug):
    context_dict = {}

    try:
        asset = Fac.objects.get(slug=asset_name_slug)

        context_dict['Asset'] = asset
    except Fac.DoesNotExist:
        context_dict['Asset'] = None

    return render(request, 'inventory_database/asset.html', context_dict)

def add_asset(request):
    form = FacForm()

    if request.method == 'POST':
        form = FacForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
		
            test = form.cleaned_data['assignee']
            print(test)
            form.save(commit=True)
            # Now that the asset is saved
            # We could give a confirmation message
            # But since the most recent asset added is on the index page
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
		
		if form.is_valid():
			searchBy = form.cleaned_data['search_by']
			searchName = form.cleaned_data['searchName']
			searchSerial = form.cleaned_data['searchSerial']
			searchModel = form.cleaned_data['searchModel']
			searchManufacturer = form.cleaned_data['searchManufacturer']
			
			inventory = Fac.objects.all()
			
			if searchBy == '1':
				search_list = inventory.filter(name__icontains = searchName)

			elif searchBy == '2':
				search_list = inventory.filter(serial__icontains = searchSerial)
				
			elif searchBy == '3':
				search_list = inventory.filter(model__icontains = searchModel)
				
			elif searchBy == '4':
				search_list = inventory.filter(manufacturer__icontains = searchManufacturer)
				
			context_dict = {'results': search_list}
			print(searchBy)
			return render(request, 'inventory_database/search_results.html', context_dict)
		else:
			print(form.errors)
	return render(request, 'inventory_database/search.html', {'form': form} )