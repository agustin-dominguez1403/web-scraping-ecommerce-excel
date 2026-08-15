import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

print("=== EXTRACCIÓN DEL CATÁLOGO DE LIBROS (3 PÁGINAS) ===\n")

titulos = []
precios = []
disponibilidades = []

# Recorremos de la página 1 a la 3
for pagina in range(1, 4):
    url = f"http://books.toscrape.com/catalogue/page-{pagina}.html"
    print(f"📄 Descargando página {pagina}...")
    
    respuesta = requests.get(url)
    soup = BeautifulSoup(respuesta.text, "html.parser")
    
    libros = soup.find_all("article", class_="product_pod")
    
    for libro in libros:
        # Título
        titulo = libro.find("h3").find("a")["title"]
        
        # Precio limpio en float
        precio_texto = libro.find("p", class_="price_color").text
        precio_limpio = float(precio_texto.replace("Â£", "").replace("£", ""))
        
        # Stock
        stock = libro.find("p", class_="instock availability").text.strip()
        
        titulos.append(titulo)
        precios.append(precio_limpio)
        disponibilidades.append(stock)
        
    time.sleep(1)  # Pausa de cortesía entre páginas

# Creamos la tabla organizada con Pandas
df = pd.DataFrame({
    "Título del Libro": titulos,
    "Precio (£)": precios,
    "Disponibilidad": disponibilidades
})

# Exportamos a Excel
archivo_salida = "catalogo_libros.xlsx"
df.to_excel(archivo_salida, index=False)

print(f"\n✅ ¡Proyecto completado con éxito!")
print(f"Se extrajeron {len(df)} libros en total.")
print(f"Archivo generado: '{archivo_salida}'")