from django.contrib import admin
# Register your models here.
from .models import Players, Legends, Womens

admin.site.register(Players)
admin.site.register(Legends)
admin.site.register(Womens)
