from django.contrib import admin

from .models import Service, Order, User
from django.db.models import F

#
@admin.action(description='Count objects')
def count_objects(modeladmin, request, queryset):
    queryset.update(count = 10)


@admin.action(description='Up price on 100')
def up_price(modeladmin, request, queryset):
    queryset.update(price=F('price') + 100)


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_filter = ('name',)
    search_fields = ('name', 'email', 'telephone')
    fieldsets = (('User', {'fields': ('name', 'email', 'telephone', 'adress')}),)


class UserService(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    list_filter = ('price',)
    search_fields = ('name', 'price')
    fieldsets = (('Service', {'fields': ('name', 'price', 'description', 'count', 'image')}),)
    actions = (count_objects, up_price,)


admin.site.register(User, UserAdmin)
admin.site.register(Service, UserService)