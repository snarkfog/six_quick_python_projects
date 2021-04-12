from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open("D:/Python/PycharmProjects/six_quick_python_projects/06_qrcode_with_python/img/qrcode.png")
result = decode(img)
print(result)
