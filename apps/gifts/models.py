from __future__ import unicode_literals
from ..login.models import User
from django.db import models
from django.contrib import messages

# Create your models here.
class WishlistManager(models.Manager):
    def IsValidWish(self, userInfo, request):
        passFlag = True
        errors = []
        if len(userInfo['item']) < 1:
            errors.append('Item cannot be left blank.')
            passFlag = False
        if len(userInfo['item']) < 3:
            errors.append('Item must contain at least 3 characters.')
            passFlag = False

        if passFlag:
            loggedin = request.session['logged_in']
            wishmaker = User.objects.get(id=loggedin)
            # wishcopier = User.objects.get(id=logged_in)
            wishlist = self.create(item = userInfo['item'], wishmaker_id = wishmaker)
        return [passFlag, errors]

class Wishlist(models.Model):
    item = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    wishmaker_id = models.ForeignKey(User, related_name="wishmaker")
    wishcopier_id = models.ManyToManyField(User, related_name="wishcopier")
    wishlistManager = WishlistManager()
    objects = models.Manager()
