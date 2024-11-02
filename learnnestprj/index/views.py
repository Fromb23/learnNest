from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import StudentProfile, TutorProfile
from .forms import StudentForm, TutorForm, CustomUserForm

def home(request):
    return render(request, 'index/home.html')

def admin_dashboard(request):
    students = StudentProfile.objects.all()
    tutors = TutorProfile.objects.all()
    return render(request, 'index/admin_dashboard.html', {'students': students, 'tutors': tutors})

def create_student(request):
    if request.method == 'POST':
        user_form = CustomUserForm(request.POST)
        student_form = StudentForm(request.POST)

        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save(commit=False)
            user.is_student = True
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            student_profile = student_form.save(commit=False)
            student_profile.user = user
            student_profile.save()
            return redirect('admin_dashboard')
    else:
        user_form = CustomUserForm()
        student_form = StudentForm()

    return render(request, 'index/create_student.html', {'user_form': user_form, 'student_form': student_form})

def create_tutor(request):
    if request.method == 'POST':
        user_form = CustomUserForm(request.POST)
        tutor_form = TutorForm(request.POST)
        if user_form.is_valid() and tutor_form.is_valid():
            user = user_form.save(commit=False)
            user.is_tutor = True
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            tutor_profile = tutor_form.save(commit=False)
            tutor_file.user = user
            tutor_profile.save()
            print("Tutor saved")
            return redirect('admin_dashboard')
    else:
        user_form = CustomUserForm()
        tutor_form = TutorForm()

    return render(request, 'index/create_tutor.html', {'tutor_form': tutor_form, 'user_form': user_form})

def tutor_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        tutor = authenticate(request, email=email, password=password)
        if tutor is not None:
            login(request, tutor)
            return redirect('tutor-dashboard')
        else:
            messages.error(request, 'Invalid email or password')

    return render(request, 'index/tutor_login.html')
