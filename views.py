from django.shortcuts import render, get_object_or_404,redirect
from .models import employee2
from .forms import EmployeeForm
# Create your views here.

def employee_list(request):
    employees = employee2.objects.all()
    return render(request, "testapp/list.html",{'employees':employees})

def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'testapp/form.html', {'form':form})

def employee_edit(request, pk):
    emp = get_object_or_404(employee2, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=emp)
    return render(request, 'testapp/form.html',{'form':form})
def employee_delete(request, pk):
    emp = get_object_or_404(employee2, pk=pk)
    emp.delete()
    return redirect('employee_list')