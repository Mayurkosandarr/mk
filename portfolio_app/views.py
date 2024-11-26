from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Education, AboutMe
from .forms import EducationForm, ProjectForm, AboutMeForm
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

def index(request):
    projects = Project.objects.all()
    education = Education.objects.all()
    about_me = AboutMe.objects.first() 
    
    return render(request, 'portfolio_app/index.html', {
        'projects': projects,
        'education': education,
        'about_me': about_me,
    })

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'portfolio_app/project_list.html', {'projects': projects})

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'portfolio_app/project_form.html'
    success_url = reverse_lazy('project_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['image'].required = False
        return form

    def form_valid(self, form):
        if not form.cleaned_data.get('image'):
            form.instance.image = self.object.image if hasattr(self, 'object') else None
        return super().form_valid(form)

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'portfolio_app/project_form.html'
    success_url = reverse_lazy('project_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['image'].required = False
        return form

    def form_valid(self, form):
        if not form.cleaned_data.get('image'):
            form.instance.image = self.object.image
        return super().form_valid(form)

def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'portfolio_app/project_form.html', {'form': form})

def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    return redirect('project_list')

def aboutme_update(request):
    try:
        aboutme = AboutMe.objects.get(pk=1)
    except AboutMe.DoesNotExist:
        aboutme = AboutMe.objects.create(name='Your Name')

    if request.method == 'POST':
        form = AboutMeForm(request.POST, request.FILES, instance=aboutme)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        form = AboutMeForm(instance=aboutme)

    return render(request, 'portfolio_app/aboutme_form.html', {'form': form})

def education_list(request):
    education = Education.objects.all()
    return render(request, 'portfolio_app/education_list.html', {'education': education})
