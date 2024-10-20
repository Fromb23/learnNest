from django.shortcuts import render, redirect
from .models import Student, Tutor
from .forms import StudentForm, TutorForm

def home(request):
    return render(request, 'index/home.html')

def admin_dashboard(request):
    students = Student.objects.all()
    tutors = Tutor.objects.all()
    return render(request, 'index/admin_dashboard.html', {'students': students, 'tutors': tutors})

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('admin_dashboard')
    else:
        form = StudentForm()

    return render(request, 'index/create_student.html', {'form': form})

def create_tutor(request):
    if request.method == 'POST':
        form = TutorForm(request.POST)
        if form.is_valid():
            tutor = form.save()
            return redirect('admin_dashboard')
    else:
        form = TutorForm()

    return render(request, 'index/create_tutor.html', {'form': form})
