from django.contrib import admin
from .models import Input, Output, HanjaWord, HanjaChar

# Register your models here.
admin.site.register(Input)
admin.site.register(Output)
admin.site.register(HanjaWord)
admin.site.register(HanjaChar)