#### Requirements :
```
import qrcode
import pillow
from PIL import Image , ImageDraw
```
Theory:

 * A Quick Response Code or a QR Code is a two dimensional bar code consisting of grid of tiny black squares on a white background. Due to its ability to store more information and fast readability, it gained popularity over the traditional bar codes composed of black bars and white spaces.
 * Python offers a QRCode package which makes it really easy to implement this functionality. We will begin by downloading the following python packages.
 * The QRCode function used above accepts the following parameters:
 * version: This parameter defines the size of the QR Code generated. It accepts integer values in the range of 1 to 40. The higher this value, bigger the dimension of the generated QR Code image.
 * box_size: This parameter defines the size of each box in pixels.
 * border: The border defines the thickness of the border. In this example, the value of 5 means that the border is equal to the thickness of 5 tiny black boxes.
 * The add_data method is used to pass our input text, which is the hyperlink to the article in our case. The make function with (fit=True) ensures that the entire dimension of the QR Code is utilized, even if our input data could fit into less number of boxes.
 * The last step is to convert this into an image file and store it. For this, the make_image function is used where we can specify the foreground and background color. I have used black and white respectively, but you can change them as per your preference. The save function stores the image as a .png file in the current directory.

