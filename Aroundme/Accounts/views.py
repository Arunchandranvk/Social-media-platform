from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,CreateView,FormView
from .forms import *
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate,login,logout 
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.

# def signin_required(fn):
#     def wrapper(request,*args,**kwargs):
#         if request.user.is_authenticated:
#             return fn(request,*args,**kwargs)
#     return wrapper   





class MainHome(TemplateView):
     template_name="Mainhome.html"
    

# class LogView(View):
#     def get(self,request,*args,**kwargs):
#         user=request.user
#         f=Log()
#         return render(request,"login.html",{"form":f,"name":user})
#     def post(self,request,*args,**kwargs):
#         form_data=Log(data=request.POST)
#         if form_data.is_valid():
#             un=form_data.cleaned_data.get("username")
#             ps=form_data.cleaned_data.get("password1")
#             user=authenticate(request,username=un,password=ps)
#             if user:
#                   login(request,user)
#                   messages.success(request,"Login Successfull")
#                   return redirect("h")
#             else:
#                    messages.error(request,"Login Failed!! Username or Password incorrect ")
#                    return redirect("mh")
#         else:
#                messages.error(request,"Login Failed!! ")
#                return render(request,"login.html",{"form":form_data})

class LogView(FormView):
     template_name="login.html"
     form_class=Log
     def post(self,request,*args,**kwargs):
        form_data=Log(data=request.POST)
        if form_data.is_valid():
            un=form_data.cleaned_data.get("username")
            ps=form_data.cleaned_data.get("password1")
            user=authenticate(request,username=un,password=ps)
            if user:
                  login(request,user)
                  messages.success(request,"Login Successfull")
                  return redirect("h")
            else:
                   messages.error(request,"Login Failed!! Username or Password incorrect ")
                   return render(request,"login.html",{"form":form_data})
        else:
               messages.error(request,"Login Failed!! ")
               return render(request,"login.html",{"form":form_data})

# class RegView(View):
#      def get(self,request,*args,**kwargs):
#           r=Reg()
#           return render(request,"reg.html",{"form":r})
#      def post(self,request,*args,**kwargs):
#           form_data=Reg(data=request.POST)
#           if form_data.is_valid():
#                form_data.save()
#                messages.success(request,"Registration Successfull")
#                return redirect("mh") 
#           else:
#                messages.error(request,"Registration UnSuccessfull")
#                return render(request,"reg.html",{"form":form_data})     

class RegView(CreateView):
     form_class=Reg
     template_name="reg.html"
     model=User
     success_url=reverse_lazy("mh")
     def form_valid(self,form):
        mail=form.cleaned_data.get("email")
        send_mail(
            "Around Me Registration",
            "Welcome to Around Me !",
            "arunchandranvk84@gmail.com",
            [mail]
        )
        messages.success(self.request,"Registration Completed !")
        self.object=form.save()
        return super().form_valid(form)
        

class LogOut(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")