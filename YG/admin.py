from django.contrib import admin
from .models import *
from .models import GraphicSoftware
from .models import Card
# Register your models here.

@admin.register(Card)
class ImageAdmin(admin.ModelAdmin):
 list_display = ['image',]


admin.site.register(StudentUser)
admin.site.register(GraphicSoftware)
# admin.site.register(Card)
admin.site.register(Feedback)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)