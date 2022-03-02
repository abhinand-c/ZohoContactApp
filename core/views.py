from unicodedata import name
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic.base import TemplateView

from . import models, forms



def signup(request):
    next_loc = request.POST.get('next', '/')
    if(request.user.is_authenticated):
        return redirect(next_loc)
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            raw_password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            # authenticate username and password
            user = authenticate(username=email, password=raw_password)
            login(request, user)
            next_loc = request.POST.get('next', '/')
            return redirect(next_loc)
    else:
        form = forms.SignUpForm()
    return render(request, 'core/signup.html', {'form': form, 'next': next_loc, 'title': 'Sign up', })


class HomeView(TemplateView):
    template_name = "core/home.html"

    def setup(self, request, *args, **kwargs):
        setup = super(HomeView, self).setup(request, *args, **kwargs)
        self.contact_form = forms.ContactForm()
        return setup

    def get_contacts(self, user):
        return models.Contact.objects.filter(user=user).order_by("name")  

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['contact_form'] = self.contact_form
        context['contact_list'] = self.get_contacts(self.request.user)
        return context
    
    def post(self, request, *args, **kwargs):
        if 'contact-submit' in request.POST:
            form = forms.ContactForm(request.POST)
            if form.is_valid():
                model_data = form.save(commit=False)
                model_data.user = request.user
                model_data.save()
                messages.success(request, "Successfully updated form")
            else:
                messages.error(request, "Error! Form invalid, try again")
        return redirect("home")