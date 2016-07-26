from django.contrib import admin
from .models import *


admin.site.register(Pais)
admin.site.register(Ciudad)
admin.site.register(TipoPersona)
admin.site.register(UniqueId)

admin.site.register(TipoRelacion)
admin.site.register(Relacion)


from import_export import resources

class PersonaResource(resources.ModelResource):

    class Meta:
        model = Persona

from import_export.admin import ImportExportModelAdmin

class PersonaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

admin.site.register(Persona, PersonaAdmin)
