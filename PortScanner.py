import socket, threading
from queue import Queue
from os import system, name 

queue = Queue()
open_ports = []

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 

def scan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        return True
    except:
        return False

def fill_queue(ports):
    for port in ports:
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if scan(port):
            open_ports.append(port)

def pprint():
    print("+----------------------+")
    print("|     Port Scanner     |")
    print("|          By          |")
    print("|        Jasper        |")
    print("|  Github.com/j4asper  |")
    print("+----------------------+")
    print("Port Scanning is ILLEGAL, only use this if you have permission to do so!")
    print()

pprint()
target = input("Target IP: ")
print(f"Target IP set to: {target}")
print()

print("Now choose which ports will be scanned. All ports between start and end will be scanned.")
start_port = input("Start Port: ")
end_port = input("End Port: ")
print()
fill_queue(range(int(start_port), int(end_port)))

thread_list = []

for t in range(15000):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()
print("The port scanner has been started...")

for thread in thread_list:
    thread.join()

clear()
pprint()

print(f"Target IP: {target}")
print()
print(f"Scanning ports: {start_port} - {end_port}")
print()

if len(open_ports) == 0:
    print("No open ports was found.")
else:
    print("Open ports: ", open_ports)
print()
input("Press ENTER to close this window.")