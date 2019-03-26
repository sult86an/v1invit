from django.views import generic
from django.views.generic import View
from .models import Initi,  Reports, Comment, MainStage
from pmanager.models import Leaders
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse, reverse_lazy, resolve
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.conf import settings
from global_login_required import login_not_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import RedirectView
from django.shortcuts import get_object_or_404, render
from urllib.parse import urlparse
from .forms import UserForm, UpdateForm, InitiativeForm, InitiativeUpdateForm
from django.contrib.auth.models import User


@login_not_required
def index(request):
    return render(request, 'initiatives/index.html')


@login_not_required
def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        if user.is_staff:
            login(request, user)
            return HttpResponseRedirect(reverse('initiatives:home'))
        else:
            return render(request, 'initiatives/index.html', {})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(index))


class IndexView(generic.ListView):
    template_name = 'initiatives/home.html'
    context_object_name = 'initi_num'

    def get_queryset(self):
        return Initi.objects.all()

    def report_ratio(self):
        report = Reports.objects.all()
        return report


class ProgressView(generic.ListView):
    template_name = 'initiatives/home.html'
    context_object_name = 'rpr'

    def get_queryset(self):
        return MainStage.objects.all()


class LeadersView(generic.ListView):
    template_name = 'initiatives/leaders.html'
    context_object_name = 'leaders'

    def get_queryset(self):
        return User.objects.filter(is_staff=False)


class InitiativesView(generic.ListView):
    template_name = 'initiatives/all_initiatives.html'
    context_object_name = 'all_mub'

    def get_queryset(self):
        return Initi.objects.all()


class WeekReportView(generic.DetailView):
    template_name = 'initiatives/weekly_report.html'
    model = Initi


class ListWeek(generic.ListView):
    template_name = 'initiatives/weekly_report.html'
    context_object_name = 'report'

    def get_queryset(self):
        return Reports.objects.all()


class DetailView(generic.DetailView):
    template_name = 'initiatives/detail.html'
    model = Reports

    def get_queryset(self):
        return Reports.objects.all()


class EnquiryView(View):
    template_name = 'initiatives/enquiry.html'

    def get(self, request):
        return render(request, self.template_name)


class CommentCreate(CreateView):
    model = Comment
    fields = ['report', 'is_read', 'grade', 'comment']
    success_url = '/admin/initiatives/'


class UserFormView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'initiatives/add-user.html'
    success_url = reverse_lazy('initiatives:leaders')


class UserUpdate(UpdateView):
    model = User
    form_class = UpdateForm
    template_name = 'initiatives/user_update_form.html'
    success_url = reverse_lazy('initiatives:leaders')


class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy('initiatives:leaders')


class InitiativeFormView(CreateView):
    model = Initi
    form_class = InitiativeForm
    template_name = 'initiatives/add-initiatives.html'
    success_url = reverse_lazy('initiatives:initiatives')

    def get_queryset(self):
        return Initi.objects.filter(leader__is_staff=False)


class InitiativeUpdateView(UpdateView):
    model = Initi
    form_class = InitiativeUpdateForm
    template_name = 'initiatives/update-initiatives.html'
    success_url = reverse_lazy('initiatives:initiatives')

    def get_queryset(self):
        return Initi.objects.all()


class InitiativeDelete(DeleteView):
    model = Initi
    success_url = reverse_lazy('initiatives:initiatives')
