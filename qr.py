import qrcode

def generateQR(data, imgName):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(imgName)
    print(f"QR code saved as {imgName}")

data = input("Enter the data to encode in the QR code: ")
imgName = input("Enter the filename to save the QR code image (e.g., 'qrcode.png'): ")

generateQR(data, imgName)