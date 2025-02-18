import os
import django
import pandas as pd

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'factura.settings')  # Reemplaza 'nombre_del_proyecto' con el nombre de tu proyecto
django.setup()

from sistema.models import Producto  # Cambia 'sistema' por el nombre de tu app

# Ruta del archivo Excel
excel_file = 'C:\\Users\\Luis\\Desktop\\venta.xlsx'  # Cambia esto por la ruta de tu archivo
df = pd.read_excel(excel_file)

# Validar que las columnas necesarias estén en el archivo
if not all(column in df.columns for column in ['descripcion', 'cantidad']):
    print("El archivo Excel debe tener las columnas 'descripcion' y 'cantidad'.")
else:
    # Procesar cada fila del archivo
    for _, row in df.iterrows():
        descripcion = row['descripcion']
        cantidad = row['cantidad']

        try:
            # Buscar el producto en la base de datos
            producto = Producto.objects.get(descripcion=descripcion)
            subtotal = producto.precio_unitario * cantidad
            impuestos = subtotal * (producto.impuesto / 100)
            total = subtotal + impuestos

            # Mostrar los resultados en la terminal
            print(f"Producto: {producto.descripcion}")
            print(f"Cantidad: {cantidad}")
            print(f"Código: {producto.codigoo}")
            print(f"Subtotal: ${subtotal:.2f}")
            print(f"Impuestos: ${impuestos:.2f}")
            print(f"Total: ${total:.2f}\n")
        except Producto.DoesNotExist:
            print(f"El producto '{descripcion}' no se encontró en la base de datos.")
