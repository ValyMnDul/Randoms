import qrcode # type: ignore

url = "https://campfire.hackclub.com/suceava"

qr = qrcode.QRCode(
    version=1, 
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1,
)

qr.add_data(url)
qr.make(fit=True)

img = qr.make_im
age(fill_color="black", back_color="white")

img.save("campfireQR.png")
