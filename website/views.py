from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout

class HomeView(TemplateView):
    
    def home(request):
        return render(request ,"home.html")

    def logout_view(request):
        logout(request)
        return redirect("/")

