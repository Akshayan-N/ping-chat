import subprocess
import rsa
import time

IP = publicKey = privateKey = None 

def send_privateKey():
    print("-----------Key Generated and ready to send. Make Sure to run recevier.py before send key---------------")
    input("Press [ENTER] to send : ")
    cipher = caesar_cipher(privateKey.save_pkcs1().decode('utf-8'), 3)
    send_message(cipher)
    print("Key Sent\n")

def encrypt_text(string):
    return rsa.encrypt(string.encode(),publicKey)

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

def divide_string(input_string):
    return [input_string[i:i+15] for i in range(0, len(input_string), 15)]

def hex_value(string):
    return string.encode('utf-8').hex()
    
def send_meta(ip,message_count):
    subprocess.run(['ping', ip, '-p', hex_value(message_count), '-s', str(len(message_count)), '-c', '1'], stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)    
def send_message(message = None):
    if message == None:
        message = input("Enter the message : ")
    divided_message = divide_string(message)
    message_count = len(divided_message) * 2
    send_meta(IP,str(message_count))

    time.sleep(0.8)

    for current_message in divided_message:
        subprocess.run(['ping', IP, '-p', hex_value(current_message), '-s', str(len(current_message)), '-c', '1'],stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)
    
def chat():
    message = input("Enter the message : ")
    encrypted_message = repr(encrypt_text(message))
    send_message(encrypted_message)
    chat()

def main():
    global IP ,publicKey , privateKey
    IP = input("Enter the Target IP : ") ##Getting the IP 
    publicKey , privateKey = rsa.newkeys(1024) ## Generating key

    ##Sending Key to Receiver
    send_privateKey()
    chat()
main()