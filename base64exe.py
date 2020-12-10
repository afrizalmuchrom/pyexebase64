import base64

#DECODE
with open("ome2.png", "wb") as fh:
    text_file = open("baseX.txt","rb")
    fh.write(base64.decodebytes(text_file.read()))

#ENCODE
# with open("ome1.png", "rb") as img_file:
#     my_string = base64.b64encode(img_file.read())
#     text_file = open("baseX.txt", "wb")
#     n = text_file.write(my_string)
#     text_file.close()