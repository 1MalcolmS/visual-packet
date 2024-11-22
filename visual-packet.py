import scapy

#tcp strings

tcp_fields = {}


S_PORT = "-S_PORT-"
D_PORT = "-D_PORT-"
SEQUENCE_NUMBER = "-SEQUENCE_NUMBER-"
ACKNOWLEDGEMENT_NUMBER = "-ACKNOWLEDGEMENT_NUMBER-"
O = "-O-"
R = "-R-"
FLAGS = "-FLAGS-"
WINDOW = "-WINDOW-"
CHECKSUM = "-CHECKSUM-"
URGENT = "-URGENT-"
TCP_OPTIONS = "-TCP_OPTIONS-"
TCP_DATA = "-TCP_DATA-"
def clear_tcp():
    globals()["S_PORT"] = "-S_PORT-"
    globals()["D_PORT"] = "-D_PORT-"
    globals()["SEQUENCE_NUMBER"] = "-SEQUENCE_NUMBER-"
    globals()["ACKNOWLEDGEMENT_NUMBER"] = "-ACKNOWLEDGEMENT_NUMBER-"
    globals()["O"] = "-O-"
    globals()["R"] = "-R-"
    globals()["FLAGS"] = "-FLAGS-"
    globals()["WINDOW"] = "-WINDOW-"
    globals()["CHECKSUM"] = "-CHECKSUM-"
    globals()["URGENT"] = "-URGENT-"
    globals()["TCP_OPTIONS"] = "-TCP_OPTIONS-"
    globals()["TCP_DATA"] = "-TCP_DATA-"

#ip strings
V = "-V-"
HL = "-HL-"
TOS = "-TOS-"
LENGTH = "-LENGTH-"
ID = "-ID-"
F = "-F-"
F_OFFSET = "-F_OFFSET-"
TTL = "-TTL-"
PRO = "-PRO-"
H_CHECKSUM = "-H_CHECKSUM-"
SOURCE_ADDRESS = "-SOURCE_ADDRESS-"
DEST_ADDRESS = "-DEST_ADDRESS-"
IP_OPTIONS = "-IP_OPTIONS-"
IP_DATA = "-IP_DATA-"
def clear_ip():
    V = "-V-"
    HL = "-HL-"
    TOS = "-TOS-"
    LENGTH = "-LENGTH-"
    ID = "-ID-"
    F = "-F-"
    F_OFFSET = "-F_OFFSET-"
    TTL = "-TTL-"
    PRO = "-PRO-"
    H_CHECKSUM = "-H_CHECKSUM-"
    SOURCE_ADDRESS = "-SOURCE_ADDRESS-"
    DEST_ADDRESS = "-DEST_ADDRESS-"
    IP_OPTIONS = "-IP_OPTIONS-"
    IP_DATA = "-IP_DATA-"



def print_TCP():
    print(f"|---------------------------------|")
    print(f"|    {S_PORT}    |     {D_PORT}   |")   
    print(f"|---------------------------------|")
    print(f"|        {SEQUENCE_NUMBER}        |")
    print(f"|---------------------------------|")
    print(f"|     {ACKNOWLEDGEMENT_NUMBER}    |")
    print(f"|---------------------------------|")
    print(f"|{O} |{R}|{FLAGS}|    {WINDOW}    |")
    print(f"|---------------------------------|")
    print(f"|   {CHECKSUM}   |    {URGENT}    |")
    print(f"|---------------------------------|")
    print(f"|          {TCP_OPTIONS}          |")
    print(f"|---------------------------------|")
    print(f"|            {TCP_DATA}           |")
    print(f"|---------------------------------|\n\n\n")

def print_IP():
    print(f"|---------------------------------|")
    print(f"|{V}|{HL}| {TOS} |    {LENGTH}    |")
    print(f"|---------------------------------|")
    print(f"|      {ID}      |{F}| {F_OFFSET} |")
    print(f"|---------------------------------|")
    print(f"|  {TTL} | {PRO} |  {H_CHECKSUM}  |")
    print(f"|---------------------------------|")
    print(f"|        {SOURCE_ADDRESS}         |")
    print(f"|---------------------------------|")
    print(f"|         {DEST_ADDRESS}          |")
    print(f"|---------------------------------|")
    print(f"|          {IP_OPTIONS}           |")
    print(f"|---------------------------------|")
    print(f"|            {IP_DATA}            |")
    print(f"|---------------------------------|")

def tcp_options(command, location, entry):
    if command == "set":
        set_entry(location, entry)
    elif command == "clear":
        clear_tcp()
    elif command == "default":
        print("default")
    elif command == "N":
        print_TCP()

def ip_options(command, location, entry):
    if command == "set":
        set_entry(location, entry)
    elif command == "clear":
        clear_ip()
    elif command == "default":
        print("default")
    elif command == "N":
        print_IP()

def set_entry(location, entry):
    to_be_set = location
    globals()[to_be_set] = entry
    
        
def default_tcp():
    #set default options
    pass
def default_ip():
    #set default options
    pass




while True:
    input1 = input()
    
    input_list = input1.split(" ")
    while len(input_list) < 4:
        input_list.append("N")
        
    if input_list[0] == "exit":
        break
    elif input_list[0] == "tcp":
        tcp_options(input_list[1], input_list[2], input_list[3])
    elif input_list[0] == "ip":
        ip_options(input_list[1], input_list[2], input_list[3])




    

          
