from django.contrib import admin

# Register your models here.
from cw21.models import Person, ContactInfo, Group, Hobbie

admin.site.register(Person)
admin.site.register(ContactInfo)
admin.site.register(Group)
admin.site.register(Hobbie)
