import socket
import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_ip = input('Ingresa la IP del servidor\n')
server_port = int(input('Ingresa el puerto\n'))

server_address = (server_ip, server_port)

date_format = '%d/%m/%Y'

birth = input('Ingresa tu fecha de nacimiento con el formato DD/MM/AAAA\n')

try:
    print('Enviando {!r}'.format(birth))
    sent = sock.sendto(birth.encode('utf-8'), server_address)
    print('Esperando para recibir respuesta')

    data, server = sock.recvfrom(4096)
    print('Información recibida "{!r}"'.format(data))

finally:
    print('Cerrando socket cliente')
    sock.close()