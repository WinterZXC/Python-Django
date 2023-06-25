from django.shortcuts import render, get_object_or_404, redirect
from .models import Companies, Users, Capital, CapitalFormSet, CapitalFormCreateSet
from django.db.models import Q
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.forms import formset_factory
from django.views.generic import DetailView
from django.views.generic.edit import (
    CreateView, UpdateView
)
# Create your views here.


def detail_page(request, id):
    companies = get_object_or_404(Companies, pk=id)
    users = Users.objects.select_related().all()
    capital = Capital.objects.select_related().all()
    return render(request, 'main/companies_detail.html', {'companies': companies, 'users': users, 'capital': capital})



def index(request):
    companies = Companies.objects.select_related().all()
    users = Users.objects.select_related().all()
    capital = Capital.objects.select_related().all()

    return render(request, 'main/index.html', {'companies': companies, 'users': users, 'capital': capital})

def search_name(request):
    capital = Capital.objects.select_related().all()
    companies = Companies.objects.select_related().all()

    if request.method == 'GET':
        search_query = request.GET.get('search_name', None)
        if search_query:

            users = Users.objects.filter(Q(name__icontains=search_query) | Q(personal_code__icontains=search_query) | Q(surname__icontains=search_query))
    return render(request, 'main/search_name.html', {'companies': companies,  'users': users, 'capital': capital})

def search_companie(request):
    capital = Capital.objects.select_related().all()
    users = Users.objects.select_related().all()

    if request.method == 'GET':
        search_query = request.GET.get('search_companie', None)
        if search_query:
            companies = Companies.objects.filter(Q(name__icontains=search_query) | Q(reg_number__icontains=search_query) )

    return render(request, 'main/index.html', {'companies': companies,  'users': users, 'capital': capital})

def create(request):
    users = Users.objects.select_related().all()
    companies = Companies.objects.select_related().all()
    capital = Capital.objects.select_related().all()
    id = Companies.objects.order_by('-id')[:1]

    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('regNumber') and request.POST.get('date') and request.POST.get('capital'):
            post = Companies()
            post.name = request.POST.get('name')
            post.reg_number = request.POST.get('regNumber')
            post.date = request.POST.get('date')
            post.capital = request.POST.get('capital')
            post.save()
            return render(request, 'main/index.html', {'companies': companies, 'users': users, 'capital': capital})
    else:
        return render(request, 'main/create_companie.html', {'companies': companies, 'users': users})

class CapitalAddView(TemplateView):
    template_name = 'main/add_partners.html'
    def get(self, *args, **kwargs):
        id = self.kwargs['id']
        companies = get_object_or_404(Companies, pk=id)
        formset = CapitalFormSet(queryset=Capital.objects.none())
        return self.render_to_response({'capital_formset': formset, 'companies': companies})
    def post(self, *args, **kwargs):

        formset = CapitalFormSet(data=self.request.POST)
        if formset.is_valid():



            formset.save()

            companieId = self.request.POST.get('id')
            count = self.request.POST.get('form-TOTAL_FORMS')
            ids = Capital.objects.order_by('-id')[:int(count)]
            for y in ids:
                obj = Capital.objects.get(id=y.id)
                obj.companies_id_id = companieId
                obj.save()

            post = Companies.objects.get(id=companieId)
            post.capital = self.request.POST.get('newCapital')
            post.save()



            return redirect(reverse_lazy("main"))

        return self.render_to_response({'capital_formset': formset})

class CapitalCreateView(TemplateView):
    template_name = 'main/create_companie.html'
    def get(self, *args, **kwargs):
        id = Companies.objects.order_by('-id')[:1]
        formset = CapitalFormCreateSet(queryset=Capital.objects.none())
        return self.render_to_response({'capital_formset': formset,'id':id})
    def post(self, *args, **kwargs):

        formset = CapitalFormCreateSet(data=self.request.POST)
        if formset.is_valid():
            post = Companies()
            post.name = self.request.POST.get('name')
            post.reg_number = self.request.POST.get('regNumber')
            post.date = self.request.POST.get('date')
            post.capital = self.request.POST.get('capital')
            post.save()


            formset.save()

            companieId = self.request.POST.get('id')
            count = self.request.POST.get('form-TOTAL_FORMS')
            ids = Capital.objects.order_by('-id')[:int(count)]
            for y in ids:
                obj = Capital.objects.get(id=y.id)
                obj.companies_id_id = companieId
                obj.save()



            return redirect(reverse_lazy("main"))

        return self.render_to_response({'capital_formset': formset})

