import qrcode
import os

# URL que abre machine_detail.html; ajusta el dominio según corresponda
url = "http://localhost:5000/machines/max_muller"

# Configuración y generación del QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

# Carpeta donde se guardará el código QR
output_folder = "static/qr's"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Nombre de archivo: el mismo que el que abre (machine_detail) con extensión .png
output_path = os.path.join(output_folder, "machine_detail.png")
img.save(output_path)

print(f"Código QR guardado en: {output_path}")
