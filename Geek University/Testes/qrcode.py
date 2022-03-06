import qrcode

imagem = qrcode.make("https://www.youtube.com/c/%C3%80BeiradaQuadra")
imagem.save("qrcodeteste.jpg")