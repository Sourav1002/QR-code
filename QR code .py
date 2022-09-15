import qrcode

qr=qrcode.make("https://www.linkedin.com/in/sourav-ramalingam/")
qr.save("QR.png")