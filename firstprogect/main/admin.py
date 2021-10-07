from django.contrib import admin
from .models import Client
from .models import Client_road
from .models import Client_contact

admin.site.register(Client)
admin.site.register(Client_road)
admin.site.register(Client_contact)