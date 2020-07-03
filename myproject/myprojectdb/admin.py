from django.contrib import admin
from .models import Program,Subprogram,Course

# Register your models here.
admin.site.register(Program)
admin.site.register(Subprogram)
admin.site.register(Course)