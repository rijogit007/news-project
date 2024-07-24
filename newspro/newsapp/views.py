
from django.views import View
from django.shortcuts import render,redirect
from newspro.forms import UserregisterForm, UserLoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from .models import Category, NewsArticle
from django.contrib import messages

class Home(TemplateView):    
    template_name="home.html" 

class Userregistrationview(View):
    def get(self,request):
        form= UserregisterForm()
        return render(request,'register.html',{'form':form})
    

    def post(self,request):
        data = UserregisterForm(request.POST)
        if data.is_valid():
            # data.save()
            formdata=data.cleaned_data
            User.objects.create_user(**formdata)
            return render(request,'home.html')
        
                
              
         
        
class UserLoginview(View):
    def get(self,request):
        form= UserLoginForm()
        return render(request,'login.html',{'form':form})
    

    def post(self,request):
        # data = UserregisterForm(request.POST)
        uname=request.POST.get("username")
        psw=request.POST.get("password")
        user=authenticate(request,username=uname,password=psw)
        
        if user:
              login(request,user)
              messages.success(request,'login sucessful')
              return redirect('category_list')
        else:
              messages.error(request,'invalid credentials')
              return redirect('home_view')



class Logout(View):
    
    def get(self,request):
        logout(request)
        return redirect('home_view')



class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'

class NewsListView(ListView):
    model = NewsArticle
    template_name = 'news_list.html'
    context_object_name = 'articles'
    paginate_by = 10  # Number of articles per page

    def get_queryset(self):
        category_id = self.kwargs['pk']
        return NewsArticle.objects.filter(category_id=category_id)

class NewsDetailView(DetailView):
    model = NewsArticle
    template_name = 'news_detail.html'
    context_object_name = 'article'