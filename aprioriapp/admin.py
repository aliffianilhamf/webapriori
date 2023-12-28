from django.contrib import admin
# Register your models here.

from .models import Transaksi

from import_export.admin import ImportExportModelAdmin

admin.site.register(Transaksi, ImportExportModelAdmin)