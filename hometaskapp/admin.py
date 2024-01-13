from django.contrib import admin

from .models import Service, Order, User
from django.db.models import F


@admin.action(description='Count objects')
def count_objects(modeladmin, request, queryset):
    queryset.update(count = 10)


@admin.action(description='Up price on 100')
def up_price(modeladmin, request, queryset):
    queryset.update(price=F('price') + 100)


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_filter = ('price',)
    search_fields = ('name', 'email')
    fieldsets = (('User', {'fields': ('name', 'email', 'telephone', 'adress')}),
                 ('Order', {'fields': ('customer', 'products', 'date_ordered', 'total_price')}),
                 ('Service', {'fields': ('name', 'price', 'description', 'count', 'image')}))
    actions = (count_objects, up_price,)


admin.site.register(User, Service, Order, UserAdmin)
