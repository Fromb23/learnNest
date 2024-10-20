from django import forms
from .models import Student, Tutor

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
                'student_id', 'first_name',
                'last_name', 'subjects',
                'password'
                ]

class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = [
                'tsc_no', 'first_name',
                'last_name', 'subj_comb',
                'email', 'password'
                ]
