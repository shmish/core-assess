from django.contrib import admin

# Register your models here.
from .models import BigIdeaRubric, CoreComp, Evidence, Student

admin.site.register(BigIdeaRubric)
admin.site.register(CoreComp)
admin.site.register(Evidence)
admin.site.register(Student)
