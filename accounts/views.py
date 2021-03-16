from django.shortcuts import get_object_or_404, redirect, render
from .models import Profile
from .forms import UserForm , UserCreateForm, LoginForm
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from main.models import Property, Property_book
from django_filters.views import View 
# Create your views here.

def signup(request):
    if request.method == 'POST':
        signup_form = UserCreateForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            # return redirect(reverse('login'))
            username = signup_form.cleaned_data['username']
            password = signup_form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect(reverse('home:index'))
    
    else:
        signup_form = UserCreateForm()

    return render(request,'registration/signup.html',{'signup_form':signup_form})



class LoginView(View):
    template_name = 'accounts/login.html'
    form_class = LoginForm
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form =self.form_class(request.POST)
        user = authenticate(username =request.POST['username'],password=request.POST['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            form=self.form_class(None)
            return render(request, self.template_name,{'form':form})
def logout_view(request):
    logout(request)
    return redirect('/')