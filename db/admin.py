from django.contrib import admin

# Register your models here.

from db.models import Register


class RegisterAdmin(admin.ModelAdmin):
	list_listview = ('name','email','password')
admin.site.register(Register,RegisterAdmin)

from db.models import Contact
class ContactAdmin(admin.ModelAdmin):
	list_listview = ('cname','cnumber','cemail','cservice','ccomment')
admin.site.register(Contact,ContactAdmin)