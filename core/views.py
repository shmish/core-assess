from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, Http404, render
from django.forms import ModelForm
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy, reverse

from .models import CoreComp, BigIdeaRubric, EvidenceForm, Student, Evidence


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


def submitted(request):
    return render(request, 'core/submitted.html')
#    return HttpResponse("Thank you for submitting your evidence.")


class EvidenceCreateView(CreateView):
    model = Evidence
    form_class = EvidenceForm
    template = "create_evidence.html"

    def form_valid(self, form):
        evidence = form.save(commit=False)
        evidence.dateAdded = timezone.now()
        evidence.save()
        return super(EvidenceCreateView, self).form_valid(form)
    def get_success_url(self):
        return reverse('core:submitted')

create_evidence_view = EvidenceCreateView.as_view()


class EvidenceListView(ListView):
    model = Evidence

    def get_context_data(self, **kwargs):
        context = super(EvidenceListView, self).get_context_data(**kwargs)
        context['evindences'] = Evidence.objects.all()
        context['corecomps'] = CoreComp.objects.all()
        c = CoreComp.objects.order_by('core_comp', 'iCan')
        context['length'] = len(CoreComp.objects.all())
        context['bigideas'] = BigIdeaRubric.objects.all()
        b = BigIdeaRubric.objects.order_by('courseName', 'bigIdea')
        return context

list_evidence_view = EvidenceListView.as_view()
