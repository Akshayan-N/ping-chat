import subprocess
import pyshark

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
def main():
    #create a empty file 
    subprocess.run(["tshark","-w" ,FILE_PATH, "-c", "0"],stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)
    message_count = get_meta()
    get_message(message_count)
    
    ip,name,message = extract_and_convert_data()
    if message != '':
        print(f"{name}({ip}) : {message}")
    main()

##outside main ( GOBAL )
IP = input("Enter the IP of Sender : ")
Name = input("Sender's name : ")
print('''
Choose the interface of Sender 
 1.lo, 
 2.wlan0, 
 3.eth0
 
 ''')
interface = input("Enter your choice : ")
if interface == '1' :
    interface = "lo"
elif interface == '2': 
    interface = 'wlan0'
elif interface == '3':
    interface = "eth0"
else:
    print("Wrong Input. Exiting .")
    exit()
FILE_PATH = "/tmp/file1.pcapng"

main()