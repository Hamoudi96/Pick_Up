from __future__ import unicode_literals

from django.http import JsonResponse
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from . import models
from django.contrib.auth.models import User



def index(request):
    return render(request, 'index.html')

def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    
    context = {"form" : form}
    return render(request, "registration/register.html", context)

def profile(request):
    context = {}
    if request.user.is_authenticated:
        
        user_name = request.user.username
        
        player = models.Player.objects.all()
   
        all_teams = models.Team.objects.all()
        teams = []
        teams.append("Red bull")
        teams.append("Caronalas")
        
        for t in all_teams:
            team = models.TeamPlayer.objects.filter(team_id=t, player_id=player)
            for te in team :
                teams.append(te.name)
        
        all_fields = models.FieldLocation.objects.all()
        
        events_time = []
        field_address = []
        field_name = []
        for f in all_fields:
            if f.is_reserved:
                events_time.append(f.reservation_time)
                field_name = f.field_id.name
                zip = f.address_id.zip
                #zip = str(zip)
                #filed_address.append(f.address_id.street +"    " +f.address_id.city+"   " + zip+"   "+f.address_id.country) 
                
        context['user'] = user_name       
        context['teams'] = teams
        context['fields'] = zip(field_name, events_time , field_address)
    
    else:
        redirect("accounts/login/")
            
    return render(request, "profile.html",context)

def join_team(request):
    context = {}
    return render(request,"join_team.html", context)

def create_team(request):
    context = {}
    return render(request,"create_team.html", context)

def field_location(request):
    context = {}
    return render(request,"field_location.html", context)

def create_field(request):
    context = {}
    return render(request,"create_field.html", context)

def logout(request):
    context = {}
    return render(request,"logout.html", context)

def health(request):
    state = {"status": "UP"}
    return JsonResponse(state)


def handler404(request):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)

