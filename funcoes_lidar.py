import math
import serial

def iniciando_lidar():
    ser = serial.Serial('COM10', 115200)	#Configurando e abrindo a porta
    return ser

def verificando_quantidade_dados(ser, contador):
    contador += 1
    # Lendo cada linha enviada pelo Serial
    line = ser.readline()

    line = line.decode()
    line = line.split(',')
    # print(line)
    ponto = line[2].split('.')
    ang = float(line[0])
    dist = float(line[1])
    hall = float(ponto[0])
    # print(hall)

    if ang < 13 and contador > 2:
        print(contador)
        contador = 0

def coletando_dados_lidar(ser):
    imagem_com_angulo = []
    imagem_com_radianos = []
    for i in range(27):
        # Lendo cada linha enviada pelo Serial
        line = ser.readline()


        line = line.decode()
        line = line.split(',')
        #print(line)
        ponto = line[2].split('.')
        ang = float(line[0])
        dist = float(line[1])
        hall = float(ponto[0])
        #print(hall)

        rad = (ang * math.pi) / 180

        imagem_com_angulo.append([dist, ang])
        imagem_com_radianos.append([dist, rad])

    return imagem_com_radianos, imagem_com_angulo

