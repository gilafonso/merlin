from django.contrib import admin
from .models import Noticias, downloadableFiles, GSMModels

admin.site.register(Noticias)
admin.site.register(GSMModels)
admin.site.register(downloadableFiles)
