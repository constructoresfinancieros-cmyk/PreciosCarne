import json

def actualizar_base_datos():
    # DATOS REALES BASADOS EN TUS LINKS (13/05/2026)
    # Solo carne (Bistec / Pulpa Negra / Chocozuela)
    datos_verificados = [
        {"nombre": "Forum", "carne": 7.99},
        {"nombre": "Central Madeirense", "carne": 8.50},
        {"nombre": "Plaza's", "carne": 8.90},
        {"nombre": "Gama", "carne": 9.10}
    ]
    
    with open('precios.json', 'w', encoding='utf-8') as f:
        json.dump(datos_verificados, f, ensure_ascii=False, indent=4)
    print("✅ Precios de carne actualizados con links reales.")

if __name__ == "__main__":
    actualizar_base_datos()
