from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from app_autosalon.models import Auto, Country, Mark, Transmission, BodyType, Color, Galery


class GaleryInLine(admin.TabularInline):
    fk_name = 'auto'
    model = Galery


class AutoAdmin(SummernoteModelAdmin):
    list_display = ['id', 'mark', 'model', 'price']
    inlines = [GaleryInLine,]
    list_display_links = ['mark']
    list_filter = ['mark', 'price']
    search_fields = ['model', 'color', 'country']


admin.site.register(Auto, AutoAdmin)
admin.site.register(Country)
admin.site.register(Mark)
admin.site.register(Transmission)
admin.site.register(BodyType)
admin.site.register(Color)
admin.site.register(Galery)


