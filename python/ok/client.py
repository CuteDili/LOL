__author__ = 'chamathsilva'
import socket
import sys
import base64

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
    encoded_string = base64.b64encode(D)
    sock.send(encoded_string + '\r')
    return


def tcp_read():
    a = ' '
    b = ''
    while a != '\r':
        a = sock.recv(1)
        b = b + a

    decoded_string = b.decode('base64')
    return decoded_string

def tcp_close():
    print >>sys.stderr, 'closing socket'
    sock.close()


fileName = 'testImg.jpg'
fp = open('testImg.jpg', "rb")
data_string = fp.read()

fp.close()

print data_string[:1000]


tcp_connect('localhost', 10002)
tcp_write(fileName)
tcp_write(data_string)
print tcp_read()
tcp_close()