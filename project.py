import sys
from socket import *
import selectors
import types
import urllib.request


def main():
    server_socket = socket(AF_INET, SOCK_STREAM)  # create socket 's'
    selector = selectors.DefaultSelector()
    hostname = gethostname()
    ip_address = gethostbyname(hostname)  # get ip_addr

    port = int(sys.argv[1])  # get port from terminal entry
    server_socket.bind((ip_address, port))  # bind ip,port to socket
    server_socket.listen()
    server_socket.setblocking(False)
    selector.register(server_socket, selectors.EVENT_READ, data=None)  # register socket to the selector object and listen for 'EVENT_READ' events

    sockets_list = [server_socket]
    while True:
        user_input = ""
        print("\nChat Application Menu")
        print("----------------------")
        print("help")
        print("myip")
        print("myport")
        print("connect")
        print("list")
        print("send")
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
    
        elif user_input.startswith('terminate'):
            id = int(user_input.split()[1]) - 1
            print(id)
            terminate_opt(sockets_list, id)
            print(sockets_list)

        elif user_input.startswith('send'):
            id = int(user_input.split()[1]) - 1
            msg = user_input.split()[2]
            print(id)
            print(msg)
            send_opt(server_socket, sockets_list, id, msg)
        elif user_input == 'exit':
            exit_opt()
        else:
            print("INVALID INPUT, please try again")

def help_opt():
    user_input = ''
    print("How to Use Our Functions")
    print("-------------------------")
    print("myip - prints out the user's IP address")
    print("myport - prints out the user's port number")
    print("connect <destination> <port number> - connects to the specified destination and port number users must put IP Address and port number for the function to work")
    print("list - prints out the list of connections in the current port")
    print("terminate - closes the current socket and terminates the chat")
    print("exit - quits out of the program")
    print("Type 1 to go back to the main menu")

    user_input = input()
    if user_input == "1":
        print("GOING BACK")
    else:
        print("Invalid input. Please enter 1 to return to the main menu.")
        help_opt()


def ip_opt(ip):
    print(f"The Local Ip is: {ip}")


def my_port(port):
    print(f"Your Port number is: {port}")


def connect(client_ip, client_port_num, ip_address, port, server_socket, sockets_list):
    #  server_ip, server_port = s.getsockname()
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.setblocking(False)
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
                print(f"The connection to {client_ip} is successfully established")
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


def terminate_opt(sockets_list,id): # user_input = 'terminate idNum' <---this is the format of the user input
         # get socket ID from user input
        print(sockets_list)
        socket_to_terminate = sockets_list[id]  # get the socket object
        socket_to_terminate.close()  # close the socket
        sockets_list.remove(socket_to_terminate)  # remove the socket from the list
        #print(sockets_list)
        #print(f"Socket {id + 1} has been terminated")
        return
        
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
