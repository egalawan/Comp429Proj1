import sys
from socket import *
import selectors
import types
import urllib.request
# import requests

def main():
    server_socket = socket(AF_INET, SOCK_STREAM)  # create socket 's'
    selector = selectors.DefaultSelector()
    hostname = gethostname()
    ip_address = gethostbyname(hostname)  # get ip_addr
    print(ip_address)

    port = int(sys.argv[1])  # get port from terminal entry
    server_socket.bind((ip_address, port))  # bind ip,port to socket
    server_socket.listen()
    server_socket.setblocking(False)
    selector.register(server_socket, selectors.EVENT_READ, data=None)  # register socket to the selector object and listen for 'EVENT_READ' events

    sockets_list = [server_socket]
    while True:
        user_input = ""
        print("Chat Application Menu")
        print("----------------------")
        print("help")
        print("myip")
        print("myport")
        print("connect <destination> <port number>")
        print("list")
        print("terminate")
        print("exit")
        print("Please type in one of the following Options: ")
        user_input = input()

        if user_input == 'help':
            help_opt()
        elif user_input == 'myip':
            ip_opt(ip_address)
        elif user_input == 'myport':
            my_port(port)
        #because when using connect, needs ip and port number as well
        elif 'connect' in user_input:
            if len(user_input) >= 3: 
                user_input_list = user_input.split()
                client_ip = user_input_list[1]
                client_port_num = user_input_list[2]
                connect(client_ip, client_port_num, ip_address, port, server_socket, sockets_list)
            else:
                print("Wrong input, Try Again")
        elif user_input == 'list':
            list_opt(sockets_list)
        elif user_input == 'terminate':
            terminate_opt(sockets_list)
        elif user_input == 'send':
            send_opt()
        elif user_input == 'exit':
            exit_opt()


def help_opt():
    pass


def ip_opt(ip):
    print(f"The Local Ip{ip}")


def my_port(port):
    print(port)


def connect(client_ip, client_port_num, ip_address, port, server_socket, sockets_list):
    #  server_ip, server_port = s.getsockname()
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.setblocking(False)

    #   client_socket.setblocking(False)
    # sel = selectors.DefaultSelector()

    # sel.register(s, selectors.EVENT_READ, data=None)

    try:
        client_socket.connect((client_ip, int(client_port_num)))
    except BlockingIOError:
        pass
    selector = selectors.DefaultSelector()
    selector.register(client_socket, selectors.EVENT_WRITE, data=None)

    while True:
        events = selector.select(timeout=1)
        for key, mask in events:
            if mask & selectors.EVENT_WRITE:
                selector.unregister(client_socket)
                sockets_list.append(client_socket)
                print(f"Connected to {client_ip}:{client_port_num}")
                return
            else:
                error_handler(1)
                return


# print(f"The connection to peer {ip}  has been successfully established on port {port}")
def list_opt(socket_list):
    print('id: \t''IP address: \t\tPort No.')

    for i, each_socket in enumerate(socket_list):
        ip_address = each_socket.getsockname()[0]
        laddr_port_number = each_socket.getsockname()[1]
        try:
            raddr_port_number = each_socket.getpeername()[1]
        except OSError:
            raddr_port_number = "N/A"


        port_number = laddr_port_number if raddr_port_number == "N/A" else raddr_port_number
        print(f"{i + 1}:\t{ip_address:<18}{port_number:>10}")


def terminate_opt(socket_list):
    for socket in socket_list:
        socket.close()


def send_opt():
    pass


def exit_opt():
    False
    sys.exit()
    


def error_handler(number):
    if number == 1:
        print("Connection Error")
        return exit_opt()



if __name__ == '__main__':
    main()
