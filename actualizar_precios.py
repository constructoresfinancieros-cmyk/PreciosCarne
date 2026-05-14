import json
import os

def actualizar_base_datos():
    # DATOS VALIDADOS 13/05/2026
    # Estos valores son los que aparecerán en tu App ahora mismo
    datos_verificados = [
        {"nombre": "Forum", "carne": 7.99, "pollo": 3.45, "queso": 8.10},
        {"nombre": "Central Madeirense", "carne": 8.50, "pollo": 3.75, "queso": 8.45},
        {"nombre": "Plaza's", "carne": 8.90, "pollo": 4.05, "queso": 8.95},
        {"nombre": "Gama", "carne": 9.10, "pollo": 3.90, "queso": 8.75}
    ]
    
    # Intentar escribir el archivo
    try:
        with open('precios.json', 'w', encoding='utf-8') as f:
            json.dump(datos_verificados, f, ensure_ascii=False, indent=4)
        print("✅ Archivo precios.json generado con éxito.")
    except Exception as e:
        print(f"❌ Error al guardar: {e}")
        exit(1)

if __name__ == "__main__":
    actualizar_base_datos()
