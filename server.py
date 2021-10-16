import socket
import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 15000)

date_format = '%d/%m/%Y'

print('Server {} iniciado en el puerto {}'.format(*server_address))

sock.bind(server_address)

while True:
    print('\t\nEsperando peticiones...')

    data, address = sock.recvfrom(4096)

    print('{} bytes recibidos desde {}'.format(len(data), address))
    list_data = data.decode('utf-8').split("'")
    b_date = list_data[0]
    m_date = '04/02/2020'
    
    user_date = datetime.datetime.strptime(b_date, date_format)
    principal_date = datetime.datetime.strptime(m_date, date_format)

    days = principal_date - user_date
    days_int = days.days % 3    
    

    if data:
        sent = sock.sendto(data, address)
        print('{} bytes enviados de vuelta a {}'.format(sent, address))