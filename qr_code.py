import qrcode

# QR code data
data = "https://youtu.be/UrsmFxEIp5k?si=xQOdOAWNC7cMQDXJ"

# QR code create
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

qr.add_data(data)
qr.make(fit=True)

# Image generate
img = qr.make_image(fill_color="black", back_color="white")

# Save image
img.save("qrcode.png")

print("QR Code Generated Successfully!")