from django.contrib import admin

from advertisements.models import Advertisement


# Register your models here.
@admin.register(Advertisement)  # указывает для какого класса наша админка
class AdvertisementAdmin(admin.ModelAdmin):  # обязательно наследуемся от admin.ModelAdmin
    pass
