import qrcode
from PIL import Image , ImageDraw

print("Hey! welcome to qrcode generator .")

url = input("Enter a url :")
qr =  qrcode.QRCode(version = 1 , box_size = 10 , border = 5)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill='black',back_color='white')
img.save('qrcode.png')
