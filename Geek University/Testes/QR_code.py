"""
Para importar QR Code
https://www.youtube.com/watch?v=NvPYD4BQ_xc

"""

import qrcode

imagem = qrcode.make("https://www.youtube.com/c/%C3%80BeiradaQuadra")
imagem.save("abeiradaquadra.jpg")