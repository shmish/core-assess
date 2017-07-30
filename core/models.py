from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.forms import ModelForm
from django import forms


# Teachers or admin create a list of "I can statements" for each core competency
class CoreComp(models.Model):
    CORE_COMP = (
        ('CT', 'Critical Thinking'),
        ('CR', 'Creative Thinking'),
        ('SR', 'Social Responsibility'),
        ('CO', 'Communication'),
        ('PA', 'Personal Awareness'),
        ('CI', 'Cultural Identity'),
    )
    iCan = models.CharField(max_length=100)
    core_comp = models.CharField(max_length=2, choices=CORE_COMP)

    def __str__(self):
        return self.get_core_comp_display() + ':' + ' ' + self.iCan


# Teachers or admin enter course details and curriculum Big Ideas
class BigIdeaRubric(models.Model):
    COURSE_NAME = (
        ('MA', 'Mathematics'),
        ('AR', 'Arts Eduction'),
        ('EN', 'English Language Arts'),
        ('SC', 'Science'),
        ('SS', 'Social Studies'),
    )
    GRADE_LEVEL = (
        (8, '8'),
        (9, '9'),
    )
    gradeLevel = models.IntegerField(choices=GRADE_LEVEL, default=8)
    courseName = models.CharField(max_length=2, choices=COURSE_NAME)
    bigIdea = models.CharField(max_length=200)

    def __str__(self):
        return self.get_courseName_display() + ':' + ' ' + self.bigIdea


# Students can self-enrol their own details
class Student(models.Model):
    emailaddy = models.CharField(max_length=50)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    SIN = models.IntegerField(default=1)

    def __str__(self):
        return self.last_name


# This is the self-assessment. Students choose grade, course, "I can" statement
# Students write a description of their artifact, and the significance of their artifact in relation to the CC
class Evidence(models.Model):
    corecomp = models.ForeignKey(CoreComp, on_delete=models.CASCADE)
    bigidearubric = models.ForeignKey(BigIdeaRubric, on_delete=models.CASCADE)
    #	student = models.ForeignKey(Student, on_delete=models.CASCADE)
    pkcore = models.IntegerField(default=1)
    pkidea = models.IntegerField(default=1)
    done = models.BooleanField(default=True)
    artifact = models.CharField(max_length=200)
    signif = models.CharField(max_length=200)
    dateAdded = models.DateTimeField('date added', blank=True)

def __str__(self):
    return self.artifact


class EvidenceForm(ModelForm):
    class Meta:
        model = Evidence
        fields = ['bigidearubric', 'corecomp', 'artifact', 'signif']

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
