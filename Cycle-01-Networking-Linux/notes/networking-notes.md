# 1. Introduction to Computer Networking

## What is Computer Networking

Computer Networking is the **interconnection of multiple computing devices** (computers, servers, phones, routers, etc.) that communicate with each other to **share data, resources, and services**.

A network allows devices to exchange information through **communication channels** using standard protocols.

### Example

- Internet
- Office networks
- Home Wi-Fi networks
- Data center networks

---

## Why Computer Networks are Important

Computer networks exist mainly to **enable communication and resource sharing**.

### 1. Resource Sharing

Devices in a network can share resources such as:

- printers
- storage
- internet connection
- applications

Example:

Multiple computers in an office using the **same printer**.

---

### 2. Communication

Networks allow users to communicate quickly using:

- email
- messaging
- video calls
- VoIP

---

### 3. Data Sharing

Files can be shared between devices without physical transfer.

Example:

- shared drives
- cloud storage

---

### 4. Centralized Management

Administrators can control systems from a central location.

Example:

- managing user accounts
- installing software remotely

---

### 5. Remote Access

Users can access systems from different locations.

Example:

- employees working from home through VPN.

---

## Disadvantages of Networking

### 1. Security Risks

Networks can be attacked by hackers if not secured properly.

Example:

- malware
- phishing
- data theft

---

### 2. High Setup Cost

Building a network requires:

- cables
- routers
- switches
- servers

---

### 3. Maintenance

Networks require monitoring, updates, and troubleshooting.

---

### 4. Network Failure Impact

If the network fails, many systems may stop working.

Example:

If an office network goes down, employees may lose access to shared files.

---

# 2. Basic Components of a Network

Every network is made of **hardware, software, and communication channels**.

---

# 2.1 Host (End Device)

A **host** is any device connected to a network that can **send or receive data**.

### Examples

- Computers
- Smartphones
- Servers
- Smart TVs
- IoT devices

### Purpose

Hosts are the **actual users of the network**.

They generate and consume data.

---

# 2.2 Server

A **server** is a powerful computer that provides services to other computers in the network.

### Examples of Server Types

### Web Server

Hosts websites.

Example software:

- Apache
- Nginx

### File Server

Stores and shares files.

### Database Server

Stores structured data.

Example:

- MySQL
- PostgreSQL

### Mail Server

Handles email sending and receiving.

---

# 2.3 Client

A **client** is a device that **requests services from a server**.

Example:

Your browser → requests webpage → web server sends webpage.

---

# 2.4 Network Interface Card (NIC)

A **NIC** is hardware that allows a device to connect to a network.

Without NIC, a computer cannot communicate with a network.

### Types of NIC

### 1. Wired NIC

Uses Ethernet cable.

Advantages:

- faster
- stable
- less interference

---

### 2. Wireless NIC

Uses Wi-Fi signals.

Advantages:

- mobility
- no cables

Disadvantages:

- slower than wired
- signal interference

---

# 2.5 Transmission Media

Transmission media is the **path through which data travels**.

Two main categories exist.

---

# Guided Media (Wired Communication)

Data travels through **physical cables**.

---

### Twisted Pair Cable

Two copper wires twisted together.

Types:

### UTP (Unshielded Twisted Pair)

Most common Ethernet cable.

Examples:

- Cat5
- Cat6

Used in:

- LAN networks

Advantages:

- cheap
- flexible

Disadvantages:

- interference

---

### STP (Shielded Twisted Pair)

Has additional shielding.

Advantages:

- less interference

Disadvantages:

- expensive

---

### Coaxial Cable

Cable with central conductor and insulation.

Used in:

- cable TV
- early networks

Advantages:

- better shielding

---

### Fiber Optic Cable

Uses **light signals instead of electrical signals**.

Advantages:

- extremely fast
- long distance communication
- immune to interference

Used in:

- internet backbone
- data centers

# Unguided Media (Wireless Communication)

Data travels through **air using electromagnetic waves**.

---

### Radio Waves

Used in:

- WiFi
- Bluetooth

Advantages:

- mobility

---

### Microwave

Used for:

- satellite communication
- point-to-point links

---

### Infrared

Used in:

- short-range communication
- remote controls

---

# 3. Networking Devices

Networking devices are hardware used to **connect and manage networks**.

---

# Hub

A hub is a **basic networking device** that connects multiple computers.

### How it Works

When data arrives, the hub **broadcasts it to all connected devices**.

Example:

Computer A sends data → hub sends to B, C, D.

### Problem

All devices receive unnecessary data.

### Result

- slower network
- collisions

Because of these problems, hubs are now mostly obsolete.

---

# Switch

A switch is an improved version of a hub.

### How it Works

A switch sends data **only to the intended device** using MAC addresses.

Example:

Computer A → switch → only computer B receives the data.

### Advantages

- faster
- efficient
- less network congestion

Switch operates at **OSI Layer 2 (Data Link Layer)**.

---

# Router

A router connects **different networks together**.

Example:

Your home network → internet.

### Function

Routers determine the **best path for data packets**.

### How routers work

Routers maintain a **routing table** containing information about network paths.

---

# Modem

A modem converts signals between:

Digital signals (computers)

Analog signals (telephone lines)

Example:

DSL modem connecting your home to ISP.

---

# Access Point

A wireless access point allows devices to **connect to a wired network using Wi-Fi**.

Example:

Office WiFi network.

---

# 4. Types of Networks

Networks are categorized by **geographical size and coverage area**.

---

# PAN (Personal Area Network)

Smallest network type.

### Coverage

Few meters.

### Example

Bluetooth connection between phone and smartwatch.

### Purpose

Connect personal devices.

---

# LAN (Local Area Network)

Network within a **small geographic area**.

### Coverage

Building or campus.

### Examples

- school network
- office network
- home network

### Characteristics

- high speed
- privately owned

---

# MAN (Metropolitan Area Network)

Network that covers a **city or metropolitan area**.

Example:

city-wide internet network.

---

# WAN (Wide Area Network)

Network covering **large geographical areas**.

Example:

The Internet.

WAN connects multiple LANs together.

---

# 5. Network Topologies

Network topology describes **how devices are physically or logically connected**.

Understanding topology helps with:

- troubleshooting
- designing networks
- improving performance

---

# Bus Topology

All devices share a **single communication cable**.

### Advantages

- cheap
- simple

### Disadvantages

- if cable fails → entire network fails
- collisions increase with more devices

---

# Star Topology

All devices connect to a **central switch or hub**.

### Advantages

- easy to manage
- easy troubleshooting

### Disadvantages

- central device failure stops network

---

# Ring Topology

Devices form a **circular connection**.

Data travels in one direction.

### Advantage

No collisions.

### Disadvantage

One device failure can break network.

---

# Mesh Topology

Each device connects to **multiple other devices**.

### Advantages

- highly reliable
- fault tolerant

### Disadvantages

- very expensive
- complex

---

# Hybrid Topology

Combination of multiple topologies.

Example:

Star + Mesh.

Used in large networks.

---

# 6. OSI Model

The **OSI (Open Systems Interconnection) Model** is a conceptual framework used to understand how networking systems communicate.

It divides networking into **7 layers**, each responsible for specific tasks.

---

# Layer 7 – Application Layer

This is the **layer closest to the user**.

Applications interact with the network here.

Examples:

- HTTP
- FTP
- SMTP
- DNS

---

# Layer 6 – Presentation Layer

Responsible for:

- data translation
- encryption
- compression

Example:

SSL encryption.

---

# Layer 5 – Session Layer

Maintains **communication sessions between devices**.

Example:

Maintains session during video call.

---

# Layer 4 – Transport Layer

Responsible for **reliable communication**.

Functions:

- segmentation
- error detection
- flow control

Protocols:

- TCP
- UDP

---

# Layer 3 – Network Layer

Responsible for **logical addressing and routing**.

Main protocol:

- IP

Devices:

- routers

---

# Layer 2 – Data Link Layer

Responsible for:

- MAC addressing
- frame transmission
- error detection

Device:

- switch

---

# Layer 1 – Physical Layer

Deals with:

- cables
- electrical signals
- hardware transmission

---

# 7. TCP/IP Model

The TCP/IP model is the **practical networking model used by the internet**.

It has **4 layers**.

---

# Application Layer

Handles communication with software applications.

Protocols:

- HTTP
- FTP
- DNS
- SMTP

---

# Transport Layer

Provides communication between devices.

Protocols:

- TCP
- UDP

---

# Internet Layer

Responsible for addressing and routing.

Protocol:

- IP

---

# Network Access Layer

Handles hardware communication.

Includes:

- Ethernet
- WiFi

---

# 8. IP Addressing

An **IP address** uniquely identifies a device on a network.

Without IP addressing, devices cannot locate each other.

Example:

```
192.168.1.10
```

---

# IPv4

IPv4 uses **32 bits**.

Format:

```
192.168.0.1
```

Total addresses:

≈ 4.3 billion.

Due to address exhaustion, IPv6 was introduced.

---

# IPv6

IPv6 uses **128 bits**.

Example:

```
2001:0db8:85a3:0000:0000:8a2e:0370:7334
```

Advantages:

- massive address space
- improved routing
- built-in security

---

# 9. MAC Address

A MAC address is a **hardware address assigned to network interface cards**.

Example:

```
00:1A:2B:3C:4D:5E
```

### Purpose

Used for **local network communication**.

IP address identifies device globally.

MAC address identifies device locally.

---

# 10. DNS (Domain Name System)

DNS converts **human-readable domain names into IP addresses**.

Example:

```
google.com → 142.250.183.14
```

Without DNS, users would need to remember IP addresses.

---

# 11. DHCP

DHCP automatically assigns network configuration.

Assigned information:

- IP address
- subnet mask
- gateway
- DNS

Process:

```
DORA

Discover
Offer
Request
Acknowledge
```

---

# 12. TCP vs UDP

Both are **transport layer protocols**.

---

# TCP (Transmission Control Protocol)

Connection-oriented protocol.

### Features

- reliable
- ordered delivery
- error correction

Used in:

- web browsing
- email
- file transfer

---

# UDP (User Datagram Protocol)

Connectionless protocol.

### Features

- faster
- no error correction

Used in:

- video streaming
- gaming
- DNS

---

# 13. Ports

A **port** identifies a specific service on a device.

Example:

```
192.168.1.5:80
```

Common ports:

HTTP → 80

HTTPS → 443

FTP → 21

SSH → 22

DNS → 53

---

# 14. Routing

Routing is the process of **finding the best path for data packets**.

Routers use **routing algorithms** to decide paths.

---

# Types of Routing

---

# Static Routing

Routes are manually configured.

Advantages:

- simple
- secure

Disadvantages:

- not scalable

---

# Dynamic Routing

Routers automatically update routes.

Protocols:

- RIP
- OSPF
- BGP

Used in large networks.

---

# 15. NAT

Network Address Translation converts **private IP → public IP**.

Purpose:

- conserve IPv4 addresses
- allow private networks to access internet.

---

# 16. Firewall

A firewall monitors and controls network traffic.

Purpose:

- block malicious traffic
- protect systems

Types:

Packet filtering firewall

Stateful firewall

Application firewall

---

# 17. VPN

A VPN creates a **secure encrypted tunnel over the internet**.

Benefits:

- privacy
- secure communication
- remote access

Protocols:

OpenVPN

IPSec

WireGuard

---

# 18. Network Attacks

---

# Packet Sniffing

Capturing network packets.

Tools:

- Wireshark
- tcpdump

---

# Man-in-the-Middle Attack

Attacker intercepts communication between two parties.

---

# DDoS Attack

Attack that overwhelms servers with traffic.

---

# ARP Spoofing

Attacker sends fake ARP messages to intercept traffic.

---

# 19. Network Tools

---

# Nmap

Network scanning tool.

Example:

```
nmap 192.168.1.1
```

---

# Wireshark

Packet capture and analysis tool.

Used for:

- debugging
- security analysis

---

# Netstat

Displays network connections.

```
netstat -an
```

---

# 20. Troubleshooting Commands

Ping

```
ping google.com
```

Traceroute

```
traceroute google.com
```

ifconfig

```
ifconfig
```

ip













1. What is a Subnet?

A subnet (subnetwork) is a smaller network created from a larger network.

Instead of using one big network for everything, we divide the network into smaller logical networks.

Example

Suppose a company has this network:

192.168.1.0

If all devices are in one network:

PC1

PC2

Printer

Servers

Cameras

All devices broadcast to everyone.

This causes:

Network congestion

Security issues

Hard management

So we divide the network into subnets.

Example:

192.168.1.0/26
192.168.1.64/26
192.168.1.128/26
192.168.1.192/26

Now the network is divided into 4 smaller networks.

2. What is a Subnet Mask?

A subnet mask tells the system:

which part of the IP address represents the network and which part represents the host

Example IP:

192.168.1.10

Example subnet mask:

255.255.255.0

This means:

Network part → 192.168.1
Host part    → 10
3. Binary View (Very Important)

IP addresses are 32-bit binary numbers.

Example:

IP Address
192.168.1.10

Binary:

11000000.10101000.00000001.00001010

Subnet mask:

255.255.255.0

Binary:

11111111.11111111.11111111.00000000

Explanation:

1 = network portion
0 = host portion

So:

11111111.11111111.11111111.00000000
|--------NETWORK--------| |--HOST--|
4. CIDR Notation

Instead of writing subnet mask like:

255.255.255.0

We write:

/24

Why?

Because there are 24 network bits.

Example:

CIDR	Subnet Mask
/8	255.0.0.0
/16	255.255.0.0
/24	255.255.255.0
/25	255.255.255.128
/26	255.255.255.192

Example:

192.168.1.0/24

Means:

Network bits = 24
Host bits = 8
5. Total Hosts Formula

Formula:

2^(host bits) - 2

We subtract 2 because:

one address = network address

one address = broadcast address

Example

Network:

192.168.1.0/24

Host bits:

32 - 24 = 8

Total hosts:

2^8 - 2 = 254

Usable IP range:

192.168.1.1 → 192.168.1.254
6. Network Address

The first address of a subnet.

Example:

192.168.1.0/24

Network address:

192.168.1.0

It identifies the network itself.

7. Broadcast Address

The last address of a subnet.

Used to send data to all devices in the network.

Example:

192.168.1.255
8. Example Subnet Calculation

Network:

192.168.1.0/26

Step 1 — Find host bits

32 - 26 = 6

Step 2 — Total hosts

2^6 = 64 addresses

Step 3 — Subnet ranges

Subnet	Range
192.168.1.0/26	0 – 63
192.168.1.64/26	64 – 127
192.168.1.128/26	128 – 191
192.168.1.192/26	192 – 255

Example first subnet:

Network: 192.168.1.0
Usable: 192.168.1.1 – 192.168.1.62
Broadcast: 192.168.1.63
9. Why Subnetting is Important
1. Better Network Performance

Less broadcast traffic.

2. Security

Different departments can be isolated.

Example:

HR subnet
Finance subnet
IT subnet
3. Easier Management

Networks become structured.

4. IP Address Efficiency

Better use of IP space.

10. Subnetting in Cybersecurity

Subnetting is heavily used in network reconnaissance.

Example tools:

nmap
netdiscover
arp-scan

Example:

nmap -sn 192.168.1.0/24

This scans the entire subnet.

So understanding subnet masks helps you:

identify live hosts

map network ranges

perform internal pentesting

11. Quick Example for Pentesters

If you get this IP:

192.168.10.45/24

You instantly know:

Network range:

192.168.10.1 – 192.168.10.254

You can scan:

nmap -sn 192.168.10.0/24
12. Most Common Subnets (Memorize These)
CIDR	Hosts
/30	2
/29	6
/28	14
/27	30
/26	62
/25	126
/24	254

These appear very frequently in networking exams and pentesting.
