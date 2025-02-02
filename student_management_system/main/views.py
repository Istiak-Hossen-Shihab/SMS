from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.contrib import messages

# Create your views here.
def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student Added Successfully!")
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'create.html', {'form' : form})


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students' : students})


def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully!')
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'update.html', {'form' : form})


def delete_student(request, pk):
    students = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        students.delete()
        return redirect('student_list')
    return render(request, 'delete.html', {'students' : students})

