from django.shortcuts import render, redirect
from ..login.models import User
from .models import Wishlist
from django.db import models
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.
def home(request, id):
    user = User.objects.get(id=request.session["logged_in"])
    context = {
        "loggedin": User.objects.get(id=id),
        "wishes" : Wishlist.objects.all(),
        "unwishes": Wishlist.objects.exclude(wishmaker_id=user).exclude(wishcopier_id=user.id)
    }
    return render(request, 'gifts/index.html', context)

def create(request):
    return render(request, 'gifts/create.html')

def createwish(request):
    results = Wishlist.wishlistManager.IsValidWish(request.POST, request)
    if results[0]:
        passFlag = True
        return redirect(reverse('login_home', kwargs={'id':request.session['logged_in']}))
    else:
        passFlag = False
    	errors = results[1]
    	for error in errors:
            messages.error(request, error)
        return redirect(reverse('wishlist_create'))

def show(request, id):
	context = {
		"wish": Wishlist.objects.get(id=id),
	}
	return render(request, 'gifts/show.html', context)

def join(request):
    if request.method == 'POST':
        wishcopier_id = request.POST['wishcopier']
        item_id = request.POST['item']
        wishcopier = User.objects.get(id=wishcopier_id)
        wisheditem = Wishlist.objects.get(id=item_id)
        wisheditem.wishcopier_id.add(wishcopier)
        wisheditem.save()
        return redirect(reverse('login_home', kwargs={'id':request.session['logged_in']}))

def remove(request, id):
    if request.method == 'POST':
        this = Wishlist.objects.get(id=id)
        this.delete()
        return redirect(reverse('login_home', kwargs={'id':request.session['logged_in']}))

def unwish(request, id):
    if request.method == 'POST':
        wishcopier_id = request.POST['wishcopier']
        this = Wishlist.objects.get(id=id)
        wishcopier = User.objects.get(id=wishcopier_id)
        this.wishcopier_id.remove(wishcopier)
        return redirect(reverse('login_home', kwargs={'id':request.session['logged_in']}))
