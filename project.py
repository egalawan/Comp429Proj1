import sys
import socket
import selectors
import types
import urllib.request


# import requests


def main():
    # ip_address = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    # print(ip_address)
    # print(external_ip)
    # response = requests.get('https://api.ipify.org?format=json')
    # ip_address = response.json()['ip']

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create socket 's'
    selector = selectors.DefaultSelector()
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)  # get ip_addr
    print(ip_address)

    port = int(sys.argv[1])  # get port from terminal entry
    s.bind((ip_address, port))  # bind ip,port to socket
    s.listen()
    s.setblocking(False)
    selector.register(s, selectors.EVENT_READ,
                      data=None)  # register socket to the selector object and listen for 'EVENT_READ' events

    sockets_list = [s]
    print("Please select from the numeric options below:")
    print("help")
    print("myip")
    print("myport")
    print("connect")
    print("list")
    print("terminate")
    print("exit")
    user_input = input("")

    if user_input == 'help':
        help_opt()
    elif user_input == 'myip':
        ip_opt(ip_address)
    elif user_input == 'myport':
        my_port(port)
    elif 'connect' in user_input:
        user_input_list = user_input.split()
        client_ip = user_input_list[1]
        client_port_num = user_input_list[2]
        print(client_ip)
        print(client_port_num)
        connect(client_ip, client_port_num, ip_address, port, s, sockets_list)
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
    print(ip)


def my_port(port):
    print(port)


def connect(client_ip, client_port_num, ip_address, port, s, sockets_list):
    #  server_ip, server_port = s.getsockname()
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
                print("Connection failed")
                return


# print(f"The connection to peer {ip}  has been successfully established on port {port}")


def list_opt(socket_list):
    print('ID' + '\t''\t''IP' + '\t''\t''Port Number')
    for index, socket in enumerate(socket_list):
        ip_address = socket.getsockname()[0]
        port_number = socket.getsockname()[1]
        print(f'{index + 1:<10}{ip_address:<18}{port_number:>10}')


def terminate_opt(socket_list):
    for socket in socket_list:
        socket.close()


def send_opt():
    pass


def exit_opt():
    sys.exit()


def error_handler():
    return "Invalid input. Please enter a number"


if __name__ == '__main__':
    main()
