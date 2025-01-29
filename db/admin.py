from django.contrib import admin

# Register your models here.

from db.models import Register


class RegisterAdmin(admin.ModelAdmin):
	list_listview = ('name','email','password')
admin.site.register(Register,RegisterAdmin)