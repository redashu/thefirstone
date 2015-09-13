from django.contrib import admin

from .models import Appnames,Howtouse

class Howapp(admin.StackedInline):
    model = Howtouse

class Toregister(admin.ModelAdmin):
    inlines = [Howapp,]

admin.site.register(Appnames, Toregister)
# admin.site.register(Toregister)
admin.site.register(Howtouse)

# Register your models here.
