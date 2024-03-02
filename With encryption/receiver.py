import subprocess
import pyshark
import rsa
# import time 

IP = Name = interface = privateKey = None
FILE_PATH = "/tmp/ping-chat.pcapng"

def decrypt_message(enc_message):
    return rsa.decrypt(eval(enc_message),privateKey).decode()

def get_privateKey():
    print("Waiting for private key .... \n ")
    message_count = get_meta()
    get_message(message_count)

    global privateKey
    cipher = extract_and_convert_data()[2]
    privateKey = rsa.PrivateKey.load_pkcs1(caesar_cipher(cipher, -3).encode('utf-8'))
    print("Received Private Key \n")

def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            encrypted_text += char
    return encrypted_text    

def extract_and_convert_data():
    ip = name = None
    ascii_text = ""
    capture = pyshark.FileCapture(FILE_PATH) 
    for packet in capture:
        if packet.highest_layer != "ICMP":
            continue

        icmp_data = packet.ICMP
        if str(icmp_data.type) != '8':
            continue
        ip_data = packet.IP
        if str(ip_data.src) != IP:
            ip = str(ip_data.src)
            name = "You"
        else:
            ip = IP
            name = Name
        hex_string = data_bytes = str(icmp_data.data)
        try:
            # Convert the hex string to bytes
            bytes_data = bytes.fromhex(hex_string)
            # Decode the bytes using the ASCII encoding
            ascii_text += bytes_data.decode("ascii")
            
        except UnicodeDecodeError:
            print("\nError decoding hex string. The data may not be valid ASCII.\n")
    capture.close()
    return ip,name,ascii_text
    
def get_meta():
    subprocess.run(["tshark", "-i", interface, "-J", "icmp", "-w" ,FILE_PATH, "-f", f"host {IP}", "-c", "1"],stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)
    meta = extract_and_convert_data()[2]
    return meta
def get_message(count):
    subprocess.run(["tshark", "-i", interface, "-J", "icmp", "-w" ,FILE_PATH, "-f", f"host {IP}", "-c", count],stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)

def start_chat():
    message_count = get_meta()
    get_message(message_count)
    ip,name,encrpted_message = extract_and_convert_data()
    message = decrypt_message(encrpted_message)
    if message != '':
        print(f"{name}({ip}) : {message}")
    start_chat()

def create_File():
    #create a empty file 
    subprocess.run(["tshark","-w" ,FILE_PATH, "-c", "0"],stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)

def choice_interface():
    print('''
Choose the interface of Sender 
 1.lo    (Local Host)
 2.wlan0 (Wireless Network)
 3.eth0  (Ethernet)
 
 ''')
    choice = input("Enter your choice : ")
    if choice == '1' :
        choice = "lo"
    elif choice == '2': 
        choice = 'wlan0'
    elif choice == '3':
        choice = "eth0"
    else:
        print("Wrong Input. Choice Again .")
        choice_interface()
    return choice

def main():
    global IP,Name,interface
    IP = input("Enter the IP of Sender : ")
    Name = input("Sender's name : ")
    interface = choice_interface()

    create_File()
    privateKey = get_privateKey(),-3

    start_chat()

main()