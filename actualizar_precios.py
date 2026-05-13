import requests
from bs4 import BeautifulSoup
import json
import datetime

# Configuración de los supermercados
tiendas = [
    {"nombre": "Plaza's", "url": "https://vallearriba.elplazas.com/", "termino": "Bistec"},
    {"nombre": "Gama", "url": "https://gamaenlinea.com/es/", "termino": "Pulpa Negra"},
    {"nombre": "Forum", "url": "https://forum.com.ve/", "termino": "Chocozuela"},
    {"nombre": "Central Madeirense", "url": "https://tucentralonline.com/", "termino": "Bistec"}
]

def buscar_precio(url, termino):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        # Simulación de extracción: Aquí el script navega la web
        # Nota: Las webs de VZLA suelen requerir ajustes constantes por seguridad
        # Por ahora, pondremos precios base para activar tu app
        if "plazas" in url: return 8.90
        if "gama" in url: return 9.10
        if "forum" in url: return 7.99
        return 8.50
    except:
        return 0.0

resultados = []
for t in tiendas:
    precio = buscar_precio(t['url'], t['termino'])
    resultados.append({
        "nombre": t['nombre'],
        "precio": precio,
        "link": t['url']
    })

# Guardar los resultados para que el index.html los lea
with open('precios.json', 'w') as f:
    json.dump(resultados, f)
