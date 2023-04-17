from django.contrib import admin
from .models import User, Contributor
admin.site.register([User, Contributor])
# Register your models here.
