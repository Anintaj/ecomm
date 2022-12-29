from django.contrib import admin

# Register your models here.
from . models import category,product
class catadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(category,catadmin)

class productadmin(admin.ModelAdmin):
    list_display = ['name','price','stock']
    list_editable = ['price','stock']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
admin.site.register(product,productadmin)



