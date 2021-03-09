from django.shortcuts import render, redirect
from .models import *
from .forms import ContactForm
from django.views.generic import ListView,DetailView
from siteblog.settings import EMAIL_HOST_USER
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError


def index(request):
    return render(request, 'chigarova/main_page.html')


def tarifs(request):
    return render(request,'chigarova/tarifs.html')

def linklist(request):
    link = Useful_link.objects.all()
    return render(request,'chigarova/linklist.html', {'link' : link})

def contacts(request):
    return render(request,'chigarova/contacts.html')

def yandex(request):
    return render(request,'chigarova/yandex.html')


class HomeLink(ListView):
    model = Useful_link
    template_name = 'chigarova/linklist.html'
    context_object_name = 'link'
    #extra_context = {'title' : 'Главная'}
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context
    def get_queryset(self):
        return Useful_link.objects.filter()

class DocView(ListView):
   model = Category
   template_name = 'chigarova/category.html'
   context_object_name = 'doc'
   allow_empty = False
   def get_context_data(self, *,object_list=None,**kwargs ):
       context = super().get_context_data(**kwargs)
       context['title'] = 'Нотариальные действия'
       return context



class DocByCategory(ListView):
    model = Context
    template_name = 'chigarova/actions.html'
    context_object_name = 'doc'
    def get_queryset(self):
        return Context.objects.filter(category_id=self.kwargs['category_id'])
    allow_empty=False

    def get_context_data(self, *,object_list=None,**kwargs ):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

class GetByDoc(DetailView):
    model = Context
    template_name = 'chigarova/docone.html'
    context_object_name = 'doc'

    def get_queryset(self):
        return Context.objects.filter(pk=self.kwargs['pk'],category_id=self.kwargs['category_id'])
    allow_empty=False
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Список документов"
        return context


def contactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        #Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            subject = form.cleaned_data['name']
            sender = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail("Отправитель письма: "+ str(subject) ,"Почта для ответа: " + str(sender) +  "\nОтправленое сообщение: "+message, EMAIL_HOST_USER,['svyaz_obratnaya@inbox.ru'])
            except BadHeaderError: #Защита от уязвимости
                return HttpResponse('Invalid header found')
            #Переходим на другую страницу, если сообщение отправлено
            return render(request, 'chigarova/feedback.html')
    else:
        #Заполняем форму
        form = ContactForm()
    #Отправляем форму на страницу
    return render(request, 'chigarova/feedback.html', {'form':form})

