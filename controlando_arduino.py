import serial
conecao = serial.Serial('COM8', 115200)

while True:
    a = input("Digite: ")
    if a == 'i':
        conecao.write(b"i")
    if a == 'k':
        conecao.write(b"k")
    if a == 'l':
        conecao.write(b"l")
    if a == 'j':
        conecao.write(b"j")
    if a == 'p':
        conecao.write(b"p"),