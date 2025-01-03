import os

# Ruta de la carpeta donde están los archivos MP3
ruta = "/Users/juanarcila/Desktop/oscar"  # Cambia esto a la ruta de tu carpeta

# Cambia al directorio de trabajo
os.chdir(ruta)

# Obtén la lista de archivos MP3
archivos = [f for f in os.listdir() if f.endswith(".mp3")]
archivos.sort()  # Orden alfabético

# Guardar los nombres originales en un archivo de texto
with open("nombres_originales.txt", "w") as file:
    for archivo in archivos:
        # Escribir el nombre del archivo sin la extensión .mp3
        file.write(f"{os.path.splitext(archivo)[0]}\n")

print("Nombres originales guardados en 'nombres_originales.txt'.")
