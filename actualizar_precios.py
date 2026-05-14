import json

# Precios actuales para sincronizar la App
tiendas = [
    {"nombre": "Forum", "carne": 7.99, "pollo": 3.50, "queso": 5.20, "link": "https://forum.com.ve/"},
    {"nombre": "Central Madeirense", "carne": 8.50, "pollo": 3.80, "queso": 5.50, "link": "https://tucentralonline.com/"},
    {"nombre": "Plaza's", "carne": 8.90, "pollo": 4.10, "queso": 6.20, "link": "https://vallearriba.elplazas.com/"},
    {"nombre": "Gama", "carne": 9.10, "pollo": 3.95, "queso": 5.80, "link": "https://gamaenlinea.com/"}
]

# Escribir el archivo que la App necesita leer
with open('precios.json', 'w') as f:
    json.dump(tiendas, f)
