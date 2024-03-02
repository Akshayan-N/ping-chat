import subprocess
import time

IP = input("Enter the Target IP : ") ## Getting the IP 

def divide_string(input_string):
    return [input_string[i:i+15] for i in range(0, len(input_string), 15)]
def hex_value(string):
    return string.encode('utf-8').hex()
    
def send_meta(ip,message_count):
    subprocess.run(['ping', ip, '-p', hex_value(message_count), '-s', str(len(message_count)), '-c', '1'], stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)    
def send_message(ip,msg):
    subprocess.run(['ping', ip, '-p', hex_value(msg), '-s', str(len(msg)), '-c', '1'],stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)
def main():
    
    full_msg = input("Enter the msg : ") ## Message to be sent     
    
    full_msg = divide_string(full_msg)
    send_meta(IP,str(len(full_msg)*2))
    time.sleep(1) ##This Sleep time is needed for the receiver to get meta data and start the next capture.
    for msg in full_msg:
        send_message(IP,msg)    
    main()
main()
