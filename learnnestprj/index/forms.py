from django import forms
from .models import CustomUser, StudentProfile, TutorProfile, Subject

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'is_student', 'is_tutor']
        widgets = {
            'password': forms.PasswordInput(),
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = [
                'student_id', 'first_name',
                'last_name', 'subjects',
                'password'
                ]

class TutorForm(forms.ModelForm):
    subj_comb = forms.ModelMultipleChoiceField(queryset=Subject.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = TutorProfile
        fields = [
                'tsc_no', 'first_name',
                'last_name', 'subj_comb',
                'email', 'password'
                ]
