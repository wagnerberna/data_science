from barcode import EAN13
from barcode.writer import ImageWriter # para salvar em png

number_convert = "000001000685"
bar_code = EAN13(number_convert, writer=ImageWriter())
bar_code.save("codigo_barras")