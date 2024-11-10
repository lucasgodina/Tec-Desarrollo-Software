import barcode
from barcode.writer import ImageWriter
from PIL import Image


def get_valid_barcode():
    while True:
        barcode_number = input("Ingrese un número de barras válido: ")
        if barcode_number.isdigit() and len(barcode_number) in [8, 12, 13]:
            return barcode_number
        else:
            print("Número de barras no válido. Intente nuevamente.")


barcode_number = get_valid_barcode()

barcode_class = barcode.get_barcode_class("ean13")
ean = barcode_class(barcode_number, writer=ImageWriter())
filename = ean.save("barcode")

# Open and display the barcode image
image = Image.open(f"{filename}")
image.show()
