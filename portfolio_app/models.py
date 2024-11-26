from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    
    def __str__(self):
        return self.title

class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.degree} - {self.institution}"

class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profile_images', null=True, blank=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

