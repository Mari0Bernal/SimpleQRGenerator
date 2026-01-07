# 📷 Generador de Códigos QR en Python

Este proyecto es un script sencillo en Python que permite generar códigos QR a partir de texto o enlaces ingresados por el usuario y guardarlos como una imagen.

## 🧠 ¿Qué hace?

El programa solicita al usuario:

- El contenido que se desea codificar
- El nombre del archivo de salida

Luego genera un código QR en formato de imagen (`.png`).

## 🛠️ Requisitos

- Python 3.x
- Librería `qrcode`

Instala la dependencia con:

```
pip install qrcode
```

## ▶️ Cómo usarlo

Ejecuta el archivo:

```
python qr.py
```

Ingresa:

- El texto o enlace que deseas convertir en QR
- El nombre del archivo de imagen (ej. qr.png)
- El código QR se guardará en la misma carpeta del proyecto.

## 📌 Ejemplo de uso

```
Enter the data to encode in the QR code: https://google.com

Enter the filename to save the QR code image (e.g., 'qrcode.png'): google_qr.png
```

Salida:

```
QR code saved as google_qr.png
```
