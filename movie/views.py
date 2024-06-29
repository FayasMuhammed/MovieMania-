from django.shortcuts import render,redirect
from django.views.generic import View
from movie.forms import Genre_form,Movie_form
from movie.models import Genre_model,Movie_model


class Addgenre_view(View):
    def get(self,request,*args,**kwargs):
        form=Genre_form()
        return render(request,"addgenre.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=Genre_form(request.POST)
        if form.is_valid():
            data=Genre_model.objects.create(**form.cleaned_data)
        form=Genre_form()
        return render(request,"addgenre.html",{"form":form,"data":data})
    
class Viewgenre_view(View):
    def get(self,request,*args,**kwargs):
        data=Genre_model.objects.all()
        return render(request,"viewgenre.html",{"data":data})
    
    def post(self,request,*args,**kwargs):
        data=Genre_model.objects.all()
        return render(request,"viewgenre.html",{"data":data})


class Updategenre_view(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=Genre_model.objects.get(id=id)
        form=Genre_form(instance=data)
        return render(request,"updategenre.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=Genre_model.objects.get(id=id)
        form=Genre_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
        return redirect("viewg")
    

class Deletegenre_view(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Genre_model.objects.get(id=id).delete()
        return redirect("viewg")
    

class Addmovie_view(View):
    def get(self,request,*args,**kwargs):
        form=Movie_form()
        return render(request,"addmovie.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=Movie_form(request.POST)
        if form.is_valid():
            form.save()
        form=Movie_form()
        return render(request,"addmovie.html",{"form":form})
    
class Viewmovie_view(View):
    def get(self,request,*args,**kwargs):
        data=Movie_model.objects.all()
        genre=Genre_model.objects.all()
        return render(request,"viewmovie.html",{"data":data,"genre":genre})
    
    def post(self,request,*args,**kwargs):
        data=Movie_model.objects.all()
        genre=Genre_model.objects.all()
        return render(request,"viewmovie.html",{"data":data,"genre":genre})
    

class Updatemovie_view(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=Movie_model.objects.get(id=id)
        form=Movie_form(instance=data)
        return render(request,"updatemovie.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=Movie_model.objects.get(id=id)
        form=Movie_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
        return redirect("viewm")
    

class Deletemovie_view(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Movie_model.objects.get(id=id).delete()
        return redirect("viewm")
    

class Filter_view(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=Genre_model.objects.get(id=id)
        m_data=Movie_model.objects.filter(movie_genre_id=id)
        return render(request,"filter.html",{"data":data,"m_data":m_data})
    
class Homepage_view(View):
    def get(self,request,*args,**kwargs):
        return render(request,"homepage.html")