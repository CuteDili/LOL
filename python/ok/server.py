__author__ = 'chamathsilva'
import socket
import sys
import base64


def tcp_connect(host_ip, port):
    global sock
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = (host_ip, port)

    print >>sys.stderr, 'starting up on %s port %s' % server_address

    sock.bind(server_address)


def tcp_write(D):
    encoded_string = base64.b64encode(D)
    connection.send(encoded_string + '\r')
    return


def tcp_read():
    a = ' '
    b = ''
    while a != '\r':
        a = connection.recv(1)
        b = b + a

    decoded_string = b.decode('base64')
    return decoded_string


def listen():
    # Listen for incoming connections
    sock.listen(1)
    global connection

    while True:
        # Wait for a connection
        print >>sys.stderr, 'waiting for a connection'
        #print('waiting for a connection', file=sys.stderr)

        connection, client_address = sock.accept()

        try:
            print >>sys.stderr, 'connection from', client_address
            file_name = tcp_read()
            data_string =  tcp_read()

            file_name =  'uploded/'+file_name
            #print file_name

            nf = open(file_name, 'w')
            nf.write(data_string)
            nf.close()

            result = ashanFunction(file_name)
            tcp_write(result)


        finally:
            # Clean up the connection
            connection.close()






def ashanFunction(fileName):
    if fileName[0] == 'a':
        return "Defected"
    else:
        return "Not Defected"







tcp_connect('localhost', 10002)
listen()