# Ping Chat Documentation
# What is Ping?

Ping (Packet Internet Groper) is a basic network utility used to test the reach ability of a host on an Internet Protocol (IP) network.

## How Ping Works

When you ping a device, your computer sends a small packet of data to the target device and waits for a response. If the target device is reachable and operational, it will respond to the ping request, indicating that it's present on the network and available.

## Purpose of Ping

Ping is commonly used for several purposes:

- **Testing Connectivity:** It's used to check if a particular host is reachable across an IP network.
- **Network Troubleshooting:** Ping can help diagnose network connectivity issues. If a device doesn't respond to pings, it could indicate a problem with the network connection or the device itself.
- **Measuring Round-Trip Time (RTT):** Ping measures the time it takes for a packet to travel from the source to the destination and back. This round-trip time (RTT) can be useful in evaluating network performance.

## Ping Options

Ping commands often come with various options that allow you to customize the behavior of the ping utility. Some common options include:

- `-c`: Specifies the number of ping requests to send before stopping.
- `-s`: Specifies the size of the ping packet.
- `-p`: Specifies the data sent by the ping packet.

With these above options, `-c`, `-s`, and `-p`, in the ping utility, I was able to create a peer-to-peer (P2P) chat space and modified the use of ping from its common networking utility to a command for chatting.

### How It Works

1. **Using `-c` for Chat Sessions:** By specifying the number of ping requests to send (`-c`), I designated a certain number of pings to represent a chat session. Each ping packet contained a piece of the message.

2. **Customizing Packet Size with `-s`:** The `-s` option allowed me to set the size of each ping packet. By adjusting this size, I could control the length of the messages being sent.

3. **Specifying Message with `-p`:** Using `-p`, I could specify the data to be sent within each ping packet. This allowed me to encode the messages I wanted to send in the chat.

4. **Interpreting Responses:** Instead of relying on the traditional response of ping, which indicates reach-ability and response time, I interpreted the responses from each ping packet as parts of the conversation.

### Example

Suppose I wanted to send a message "Hello, how are you?" using ping:

```bash
ping -c 1 -s `length of message` -p "Hexadecimal vallue of message" destination_IP
```


And this is the fundamental principle of ***Ping Chat*** 

## Overview

The Ping Chat system consists of two Python scripts: `sender.py` and `receiver.py`. These scripts enable communication between two peers using the ping utility, repurposed for messaging.

## Sender.py

### Purpose

The `sender.py` script serves as the client-side application responsible for sending messages to the receiver using ICMP echo requests.

### Usage

To use `sender.py`, run the script with the following command:

```bash
python sender.py
```

## Receiver.py

### Purpose

The `receiver.py` script acts as the server-side application responsible for receiving and decoding messages from the sender.

### Usage

To use `receiver.py`, run the script with the following command
```
python receiver.py
```


## Dependencies

1. python
2. TShark
3. pyshark library
4. ping utilities 
5. Network connection between the two machines 
