import qrcode

data=input('Enter the text or URL: ').strip()
filename=input('Enter the filename:').strip()
qr = qrcode.QRCode(box_size=40,border=40)
qr.add_data(data)
image=qr.make_image(fill_color='black',back_color='white')
image.save(filename)
print(f'Qr code saved in {filename}')