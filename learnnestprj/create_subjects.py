import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learnnestprj.settings')
django.setup()

from index.models import Subject

# Create subjects
subjects = ["Mathematics", "Science", "History", "ICT"]
for subject_name in subjects:
    Subject.objects.create(name=subject_name)

print("Subjects created successfully!")
