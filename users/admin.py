from django.contrib import admin

from baskets.admin import BasketAdmin
from baskets.models import Basket
from .models import User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = Basket
    inlines = (BasketAdmin,)
