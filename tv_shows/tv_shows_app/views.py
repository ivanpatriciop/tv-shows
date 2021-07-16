from django.core.checks import messages
from django.db import reset_queries
from django.db.models.expressions import Value
from tv_shows_app.models import Show
from django.shortcuts import redirect, render
from .models import Network, Show, ShowManager
from django.contrib import messages


def index(request):
    return redirect('/shows')

def main(request):
    context ={
        "all_shows": Show.objects.all().order_by("id")
    }
    return render(request, "index.html", context)


def new(request):
   
    context ={
        "all_networks": Network.objects.all()
    }
        
    return render(request, "create.html", context)

def create(request):
    if request.method == "POST":
        
        errors = Show.objects.basic_validator(request.POST)
        
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/new')
        else:        
            new_show = Show.objects.create(
                title=request.POST['title'],
                release_date=request.POST['release_date'],
                description=request.POST['description'],
                network= Network.objects.get(id = int(request.POST['network_dropdown'])),
                    
            )
    return redirect(f'/shows/{new_show.id}')

def edit(request, show_id):
    
    context ={
        "one_show": Show.objects.get(id=show_id),
        "one_show_created_at": str(Show.objects.get(id=show_id).release_date),
        "all_networks": Network.objects.all()
    }
    return render(request, "update.html", context)

def update(request,show_id):
    if request.method == "POST":
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) >0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f"/shows/{show_id}/edit")
        else:
            updated_show = Show.objects.get(id = show_id)
            updated_show.title = request.POST['title']
            updated_show.release_date = request.POST['release_date']
            updated_show.description = request.POST['description']
            updated_show.network = Network.objects.get(id = int(request.POST['network_dropdown']))
            
            updated_show.save()
    
    return redirect(f'/shows/{updated_show.id}')

def read(request, show_id):
    context = {
        "show_id": show_id,
        "one_show": Show.objects.get(id= show_id)
    }
    return render(request, "readOne.html", context)
   

def destroy(request, show_id):
    
    show_destroy = Show.objects.get(id = show_id)
    show_destroy.delete()
        
    return redirect('/shows')
    
