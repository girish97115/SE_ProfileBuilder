from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models
from taggit_autosuggest.managers import TaggableManager

User = get_user_model()


# Create your models here.


class FacultyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='staff_pics')
    about = RichTextField(max_length=10000)
    articles = RichTextField(max_length=10000, blank=True)
    projects = RichTextField(max_length=10000, blank=True)
    bookmark = models.ManyToManyField(User, related_query_name='bookmark', blank=True)
    is_favourite = models.BooleanField(default=False)
    interests = TaggableManager()

    def __str__(self):
        return f'{self.user.username} Profile'


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='student_pics')
    about = models.CharField(max_length=10000)

    def __str__(self):
        return f'{self.user.username} Profile'


class Appointment(models.Model):
    faculty = models.ForeignKey(FacultyProfile, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    date = models.DateField()
    reason_reject = models.CharField(max_length=1024, null=True)
    accepted = models.IntegerField(default=-1)
