from django.shortcuts import render
from django.http import HttpResponse
from inventory_database.models import Fac
from inventory_database.models import Employee
from inventory_database.forms import FacForm

def index(request):
    
    inventory_count = Fac.objects.count()
    employee_count = Employee.objects.count()
    IT_inv_count = Fac.objects.filter(asignee__department="Information Technology").count()
    HR_inv_count = Fac.objects.filter(asignee__department="Human Resources").count()
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

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        asset = Fac.objects.get(slug=category_name_slug)

        context_dict['Asset'] = asset
    except Fac.DoesNotExist:
        context_dict['Asset'] = None

    return render(request, 'inventory_database/category.html', context_dict)

def add_category(request):
    form = FacForm()

    if request.method == 'POST':
        form = FacForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
           # Save the new category to the database.
            form.save(commit=True)
           # Now that the category is saved
            # We could give a confirmation message
            # But since the most recent category added is on the index page
            # Then we can direct the user back to the index page.
            return index(request)
        else:
            # The supplied form contained errors -
            # just print them to the terminal.
            print(form.errors)

    # Will handle the bad form, new form, or no form supplied cases.
    # Render the form with error messages (if any).
    return render(request, 'inventory_database/add_category.html', {'form': form})