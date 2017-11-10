from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Context
from django.shortcuts import get_object_or_404, Http404, render, get_list_or_404
from django.forms import ModelForm
from django.views.generic.edit import CreateView, FormView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
import json

from .models import Classroom, Student, ClassroomForm, StudentFilter, DeleteForm
# from .models import RandomForm, AttendForm


def index(request):
    nickname_list = Classroom.objects.order_by('nickname')
    context = {'nickname_list': nickname_list}
    return render(request, 'classroom/index.html', context)

def submitted(request):
    return render(request, 'classroom/submitted.html')

class ClassroomCreateView(CreateView):
    model = Classroom
    form_class = ClassroomForm

    def get_success_url(self):
        return reverse('classroom:block')

create_classroom_view = ClassroomCreateView.as_view()

class BlockDeleteView(DeleteView):
    model = Classroom
    slug_field = 'id'
    success_url = ('classroom/classup')
    template_name = 'classroom/delete.html'

delete_block_view = BlockDeleteView.as_view()

def adjust(request):
    classroom = Classroom.objects.all().first()
    if request.method == 'POST':
        form = DeleteForm(request.POST)
        if form.is_valid():
            return render(request, 'classroom/adjust.html', {'form':form,'classroom':classroom})
    else:
        form = DeleteForm()

    return render(request, 'classroom/adjust.html', {'form': form,'classroom': classroom})

def randomize(request):
    classblock = request.GET.get('class_block')
    students = Student.objects.all().filter(classroom__course_block=classblock)
    print (classblock)
    print (Student.objects.filter(classroom__course_block=classblock))
    return render(request, 'classroom/block_list.html', {'students': students})

def block(request):
    classroom = Classroom.objects.all().order_by('course_block')
    classblock = request.GET.get('class_block')
    cblock = Classroom.objects.all().filter(course_block=classblock)
    cblocknum = cblock.count()
    students = Student.objects.all().filter(classroom__course_block=classblock)
    nicknames = [s.nickname for s in students]
    student_names = json.dumps(list(nicknames))
    context = {'students': students}
    context['classroom'] = classroom
    context['cblock'] = cblock
    context['student_names'] = student_names
    context['cblocknum'] = cblocknum
    # context['cblock'] = cblock
    # context['cblocknum'] = cblocknum
    template = loader.get_template('classroom/block_list.html')
    # context ={ 'classroom' : classroom, }
    print (student_names)

    # return render(request, 'classroom/block_list.html', {'classroom': classroom, 'cblock': cblock, 'cblocknum': cblocknum, 'students': students})
    return render(request, 'classroom/block_list.html', context)

def student_list(request):
    s = StudentFilter(request.GET, queryset=Student.objects.all())
    # f = AttendFilter(request.GET, queryset=Student.objects.all())
    return render(request, 'classroom/student_list.html', {'filter': s})
    # return render(request, 'classroom/student_list.html', {'filter2': f})

# class AttendFormView(FormView):
#     model = Classroom
#     form_class = AttendForm
#     template_name = 'classroom/attend_form.html'
#
#     def form_valid(self, form):
#         return super(AttendFormView, self).form_valid(form)
#
#     def get_success_url(self):
#         # return reverse('classroom:random', kwargs={'pk': self.kwargs['pk']})
#         return reverse('classroom:random', kwargs={'pk': self.kwargs['pk']})
# form_attendance_view = AttendFormView.as_view()

class ClassroomDetailView(DetailView):
    model = Classroom
    template_name = 'classroom/random_list.html'

    def get_context_data(self, **kwargs):
        class_pk = self.kwargs['pk']
        context = super(ClassroomDetailView, self).get_context_data(**kwargs)
        students = Student.objects.filter(pk = 'class_pk')
        context['students'] = students
        return context

detail_classroom_view = ClassroomDetailView.as_view()