from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,CreateView,FormView,UpdateView,DeleteView
from django.utils.decorators import method_decorator
from django.contrib import messages
from .forms import *
from django.urls import reverse_lazy
from .models import *
from django.contrib.auth import authenticate,login,logout
# from django.conf import   

# Create your views here.

def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
    return wrapper   


class Home(CreateView):
      template_name="Home.html"
      form_class=PostForm
      model=Posts
      success_url=reverse_lazy("h")
      def form_valid(self, form): 
            form.instance.user=self.request.user
            self.object=form.save()
            messages.success(self.request,"Post Added!!")
            return super().form_valid(form)            
      def get_context_data(self, **kwargs):
            context=super().get_context_data(**kwargs)
            context["data"]=Posts.objects.all().order_by("-datetime")
            context["cform"]=CommentForm()
            context["cdata"]=Comments.objects.all()
         
            return context
def addcomment(request,*args,**kwargs):
      if request.method=="POST":
            pid=kwargs.get("pid")
            post=Posts.objects.get(id=pid)
            user=request.user
            cmnt=request.POST.get("comment")
            Comments.objects.create(comment=cmnt,user=user,post=post)
            return redirect("h")

def addlike(request,*args,**kwargs):
            pid=kwargs.get("pid")
            post=Posts.objects.get(id=pid)
            user=request.user
            post.likes.add(user)
            post.save()
            return redirect("h")



# @method_decorator(signin_required,name="dispatch")



class PostView(TemplateView):
      template_name="posts.html"
      def get_context_data(self, **kwargs):
            context=super().get_context_data(**kwargs)
            context["data"]=Posts.objects.filter(user=self.request.user).order_by("-datetime")
            return context

class ProfileView(TemplateView):
        template_name="profile.html"


class BioView(CreateView):
     form_class=BioForm
     template_name="bio_user.html"
     model=Bio
     success_url=reverse_lazy("profile")
     def form_valid(self,form):
           form.instance.user=self.request.user
           self.object= form.save()
           messages.success(self.request,"Bio Added!!!")
           return super().form_valid(form)
     

           
     


class BioUpdateView(UpdateView):
      form_class=BioForm
      model=Bio
      template_name="bio_update.html"
      success_url=reverse_lazy("profile")
      pk_url_kwargs="pk"


class EditPassView(FormView):
     template_name="changepassword.html"
     form_class=ChangePassForm
     def post(self,request,*args,**kwargs):
        form_data=ChangePassForm(data=request.POST)
        if form_data.is_valid():
            cp=form_data.cleaned_data.get("c_pass")
            new=form_data.cleaned_data.get("new_pass")
            confirm=form_data.cleaned_data.get("con_pass")
            user=authenticate(request,username=request.user.username,password=cp)
            if user:               
                  if new==confirm:
                        user.set_password(new)
                        user.save()
                        messages.success(request,"password changed")
                        logout(request)
                        return redirect("signin")
                  else:
                       messages.error(request,"Password Mismatchs!!!")
                       return redirect("cpass")
            else:
                 messages.error(request,"Password Incorrect!!!")
                 return redirect("cpass")
        else:
               return render(request,"changepassword.html",{"form":form_data})
        

class EditPost(UpdateView):
     template_name="editpost.html"
     form_class=PostForm
     model=Posts
     success_url=reverse_lazy("post")
     pk_url_kwarg="pk"

# class PostDelView(View):
#      def get(self,request,*args,**kwargs):    
#         id=kwargs.get("pk")
#         post=Posts.objects.get(id=id)
#         post.delete()
#         messages.success(request,"Post Deleted")
#         return redirect('post')              
     
class PostDelView(DeleteView):
          model=Posts
          template_name="deletepost.html"
          success_url=reverse_lazy("post")