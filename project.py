import sys
import socket
import urllib.request


def main():
    if len(sys.argv) < 2:
        print("Please provide a port number as a command-line argument")
        return

    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    print("External IP address:", external_ip)

    port = sys.argv[1]
    print("Please select from the numeric options below:")
    print("1 - help: Display information about the available user interface options or command manual")
    print("2 - myip: Display IP address")
    print("3 - myport: Display port number")
    print("4 - connect: Connect to another peer")
    print("5 - list: List connected peers")
    print("6 - terminate: Terminate connection to a peer")
    print("7 - send: Send messages to peers")
    print("8 - exit: Exit the program")
    user_input = input("")

    try:
        user_input = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a number")
        return

    if user_input == 1:
        help_opt()
    elif user_input == 2:
        ip_opt()
    elif user_input == 3:
        my_port(port)
    elif user_input == 4:
        connect_opt()
    elif user_input == 5:
        list_opt()
    elif user_input == 6:
        terminate_opt()
    elif user_input == 7:
        send_opt()
    elif user_input == 8:
        exit_opt()


def help_opt():
    """Display information about the available user interface options or command manual"""
    print("Help text goes here")


def ip_opt():
    """Display the IP address of the current machine"""
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print("IP address:", ip_address)


def my_port(port):
    """Display the port number passed as a command-line argument"""
    print("Port number:", port)


def connect_opt():
    """Connect to another peer"""
    print("Connect function goes here")


def list_opt():
    """List connected peers"""
    print("List function goes here")


def terminate_opt():
    """Terminate connection to a peer"""
    print("Terminate function goes here")


def send_opt():
    """Send messages to peers"""
    print("Send function goes here")


def exit_opt():
    """Exit the program"""
    print("Exiting...")
    sys.exit(0)


if __name__ == '__main__':
    main()
