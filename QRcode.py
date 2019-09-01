import qrcode

#shortcut method
#qr=qrcode.make("hello world")
#qr.save(qrimage.png)

def QR_print(text):
    qr=qrcode.QRCode(

    version=1,
    box_size=15,
    border=5,

    )

    data=text
    qr.add_data(data)
    qr.make(fit=True) # it will fit the image
    img=qr.make_image(fil='black',back_color='white')
    img.save("QR.png")
