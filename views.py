from django.shortcuts import render
from .models import Student

def student_list(request):
    students = Student.objects.all()  
    return render(request, 'student_list.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']

        Student.objects.create(
            name=name,
            email=email,
            age=age
        )
        return redirect('student_list')

    return render(request, 'add_student.html')

def edit_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == 'POST':
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.age = request.POST['age']
        student.save()
        return redirect('student_list')

    return render(request, 'edit_student.html', {'student': student})


def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student_list')
# Create your views here.
