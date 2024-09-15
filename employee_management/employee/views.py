from django.shortcuts import render, redirect, get_object_or_404
from .models import Employees
from django.core.paginator import Paginator
from .forms import EmployeeForm
from PIL import Image

# Create your views here.

def employee_list(request):
    employees = Employees.objects.all()

    full_name = request.GET.get('full_name', '')
    email = request.GET.get('email', '')
    mobile = request.GET.get('mobile', '')
    date_of_birth = request.GET.get('date_of_birth', '')

    if full_name:
        employees = employees.filter(full_name__icontains=full_name)
    elif email:
        employees = employees.filter(email__icontains=email)
    elif mobile:
        employees = employees.filter(mobile__icontains=mobile)
    elif date_of_birth:
        employees = employees.filter(date_of_birth=date_of_birth)
    
    paginator = Paginator(employees, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'full_name': full_name,
        'email': email,
        'mobile': mobile,
        'date_of_birth': date_of_birth,
    }

    return render(request, 'employees/employee_list.html', context)


def add_employee(request):
    form = EmployeeForm()
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        
        if form.is_valid():
            employee = form.save(commit=False)
            
            if employee.photos:
                img = Image.open(employee.photos)
                img = img.resize((300, 300))
                img.save(employee.photos.path)
                
            employee.save()
            return redirect('employee_list')
            
    return render(request, 'employees/add_employee.html', {'form': form})


def edit_employee(request, employee_id):
    form = EmployeeForm()
    employee = get_object_or_404(Employees, id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        
        if form.is_valid():
            employee = form.save(commit=False)

            if 'photos' in request.FILES:
                img = Image.open(employee.photos)
                img = img.resize((300, 300))
                img.save(employee.photos.path)
                
            employee.save()
            return redirect('employee_list')
        
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'employees/edit_employee.html', {'form': form, 'employee':employee})


def delete_employee(request, employee_id):
    employee = get_object_or_404(Employees, id=employee_id)
    
    if request.method == 'POST':
        employee.delete()
        
        return redirect('employee_list')
    
    return render(request, 'employees/delete_employee.html', {'employee': employee})