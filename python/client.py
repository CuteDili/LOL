__author__ = 'chamathsilva'
import socket
import sys

def tcp_connect(host_ip, port):
    global sock

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = (host_ip, port)

    print >>sys.stderr, 'connecting to %s port %s' % server_address
    #print('connecting to', server_address[0], 'port', server_address[1], file=sys.stderr)

    sock.connect(server_address)


def tcp_write(D):
    sock.send(D + '\r')
    return


def tcp_read():
    a = ' '
    b = ''
    while a != '\r':
        a = sock.recv(1)
        b = b + a
    return b

def tcp_close():
    print >>sys.stderr, 'closing socket'
    sock.close()




tcp_connect('localhost', 10002)
tcp_write('aFile Name')
tcp_write('Data String')
print tcp_read()
tcp_close()