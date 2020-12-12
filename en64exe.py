import base64

#ENCODE
with open("old-cpu.exe", "rb") as img_file:
    my_string = base64.b64encode(img_file.read())
    text_file = open("baseX.txt", "wb")
    n = text_file.write(my_string)
    text_file.close()

