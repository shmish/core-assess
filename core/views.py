from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, Http404, render
from django.forms import ModelForm
from django.views.generic.edit import CreateView

from .models import CoreComp, BigIdeaRubric, EvidenceForm, StudentForm, Student, Evidence

def index(request):
	core_comp_list = CoreComp.objects.order_by('id')[:5]
	context = {'core_comp_list': core_comp_list}
	return render(request, 'core/index.html', context)
	
def detail(request, corecomp_id):
	corecomp = get_object_or_404(CoreComp, pk=corecomp_id)
	return render(request, 'core/detail.html', {'corecomp': corecomp})
	
def results(request, evidence_id):
	response = "You're looking at the results of evidence %s."
	return HttpResponse(response % evidence_id)
	
# def CES(request, bigidearubric_id):
	# bigidearubric = get_object_or_404(BigIdeaRubric, pk=bigidearubric_id)
	# context = {'grade_level': grade_level} 
	# return render(request, 'core/CES.html', {'bigidearubric': bigidearubric})
	

# def CES(request):
	# if request.method == 'POST':
		# form = EvidenceForm(request.POST)
		# if form.is_valid():
			# emailaddress = form.cleaned_data['emailaddy']
		# return HttpResponse('/thanks/')
	# else:
		# form = EvidenceForm()
	# return render(request, 'core/CES.html', {'form': form})
	
class EvidenceView(CreateView):
	model = Evidence
	form_class = EvidenceForm
	#template_name = 'student_form.html'
	
def submitted(request, corecomp_id):
	return HttpResponse("Thank you for submitting your evidence.")