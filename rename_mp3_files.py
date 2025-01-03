import os

# Directorio donde se encuentran los archivos
ruta = "/Users/juanarcila/Desktop/oscar"  # Cambia esto a la ruta de tu carpeta

# Obtén y ordena la lista de archivos
archivos = os.listdir(ruta)
archivos.sort()  # Orden alfabético

# Nombres nuevos para renombrar
nuevos_nombres = [
  "Hno. Oscar Rojas - Enseñanza - El Señor Jesús como mediador del nuevo pacto - 6 de noviembre de 2024 5pm",
  
]

# Renombrar archivos
for i, archivo in enumerate(archivos):
    if archivo.endswith(".mp3"):  # Asegúrate de que sea un archivo MP3
        ruta_completa = os.path.join(ruta, archivo)
        nuevo_nombre = os.path.join(ruta, nuevos_nombres[i] + ".mp3")
        os.rename(ruta_completa, nuevo_nombre)
        print(f"Renombrado: {archivo} -> {nuevos_nombres[i]}.mp3")

print("\nRenombrado completado.")
