from django import forms
from .models import Education, Project, AboutMe

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['institution', 'degree', 'field_of_study', 'start_year', 'end_year']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = False 




class AboutMeForm(forms.ModelForm):
    class Meta:
        model = AboutMe
        fields = ['name', 'profile_image', 'bio'] 
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }
