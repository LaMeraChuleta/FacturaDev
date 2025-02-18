from django.contrib import admin
from .models import Producto
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.formats.base_formats import XLSX

class ProductoResource(resources.ModelResource):
    class Meta:
        model = Producto
        fields = ('descripcion', 'unidad', 'precio_unitario', 'detalles','impuesto','codigoo')
        import_id_fields = ['descripcion']  # Usa otro campo único en lugar de 'id'

class ProductoAdmin(ImportExportModelAdmin):
    list_display=('descripcion','unidad','precio_unitario')
    resource_class = ProductoResource

admin.site.register(Producto,ProductoAdmin)
