from pdf2image import convert_from_path

def convert_pdf_to_jpg():
    img = convert_from_path("teste.pdf", dpi=200)

    # for imgs in img:     
    img.save("teste.png", "PNG")


if __name__ == "__main__":
    convert_pdf_to_jpg()