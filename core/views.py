from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, Http404, render
from django.forms import ModelForm
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy, reverse
from django.core.exceptions import ObjectDoesNotExist

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

# this view gives the overall picture/grid of the student's core competencies
class EvidenceListView(ListView):
    model = Evidence
    template_name = 'core/evidence_list.html'

    def get_context_data(self, **kwargs):
        context = super(EvidenceListView, self).get_context_data(**kwargs)
        # order the core competencies by groupings as expected in curriculum
        corecomps_ordered = CoreComp.objects.order_by('core_comp', '-iCan')
        corecomps = corecomps_ordered
        context['corecomps'] = corecomps
        # order the big ideas by subject area
        bigidea_ordered = BigIdeaRubric.objects.order_by('courseName','bigIdea')
        bigideas = bigidea_ordered
        context['bigideas'] = bigideas
        evidences = Evidence.objects.all()
        # pkcore and pkbig will be used to match artifact with table cell
        # pkcore and pkbig correspond to the id of each corecompetency and bigidea
        for ev in evidences:
            ev.pkcore = ev.corecomp.pk
            ev.pkidea = ev.bigidearubric.pk
            ev.save()
        # create a list that is ordered for the corecompetencies and bigideas
        grid = []
        for big in bigideas:
            grid.append(big.bigIdea)
            for cor in corecomps:
                grid.append((cor.pk,big.pk))
        # get length of corecomps and bigideas so we can match evidence with grid
        length_core = len(CoreComp.objects.all())
        length_row = length_core + 1
        length_big = len(BigIdeaRubric.objects.all())
        # create a list that will identify if evidence has been giving for each individual cell
        tableGrid = []
        n = 0
        for big in bigideas:
            tableGrid.append(big.bigIdea)
            # every rox begins with the bigIdea, not the evidence. Skip this first column in each row
            if n%(length_core+1) ==0:
                n += 1
            for l in range(length_core):
                pkc = grid[n][0]
                pkb = grid[n][1]
                n += 1
                # check to see if there is evidence given for the table cell
                a = evidences.filter(pkcore=pkc, pkidea=pkb).count()
                if a == 0:
                    print(a)
                    tableGrid.append('No')
                else:
                    print(a)
                    tableGrid.append('Yes')

        # context['artifacts'] = Evidence.objects.values('artifact')
        # context['signifs'] = Evidence.objects.values('signif')
        # context['length_core'] = length_core
        # context['length_big'] = length_big
        context['length_row'] = length_row
        context['tableGrid'] = tableGrid
        context['evidences'] = evidences
        context['grid'] = grid
        return context

list_evidence_view = EvidenceListView.as_view()

# this view shows a student's list of artifacts and statements of significance
class SubmissionsListView(ListView):
    model = Evidence
    template_name = 'core/submissions_list.html'

    def get_context_data(self, **kwargs):
        context = super(SubmissionsListView, self).get_context_data(**kwargs)
        # order the core competencies by groupings as expected in curriculum
        corecomps_ordered = CoreComp.objects.order_by('core_comp', '-iCan')
        corecomps = corecomps_ordered
        context['corecomps'] = corecomps
        # order the big ideas by subject area
        bigidea_ordered = BigIdeaRubric.objects.order_by('courseName','bigIdea')
        bigideas = bigidea_ordered
        context['bigideas'] = bigideas
        evidences = Evidence.objects.all()
        context['artifacts'] = Evidence.objects.values('artifact')
        context['evidences'] = evidences
        return context

list_submissions_view = SubmissionsListView.as_view()
