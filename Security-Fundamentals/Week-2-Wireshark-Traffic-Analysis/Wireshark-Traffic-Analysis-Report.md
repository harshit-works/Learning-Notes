# Wireshark Traffic Analysis Lab

## 1. Objective

The objective of this lab was to capture and analyze network traffic using Wireshark. The analysis included common protocols, TCP communication, FTP, SSH, HTTP/HTTPS traffic, and Nmap scan activity.

---

## 2. Lab Setup

- Kali Linux
- Metasploitable 2
- VirtualBox
- Wireshark
- Nmap
- Host-Only Network for the lab environment

Network communication was captured through the appropriate network interface during the analysis.

---

## 3. TCP Traffic Analysis

Captured and analyzed TCP packets in Wireshark.

Observed:

- TCP communication
- SYN packet
- SYN/ACK packet
- ACK packet
- TCP Three-Way Handshake

**Finding:** The TCP Three-Way Handshake establishes a connection before data communication begins.

**Screenshot:** `tcp-three-way-handshake.png`

---

## 4. ARP and DNS Analysis

Captured and analyzed ARP and DNS traffic.

### ARP

Observed ARP requests and replies used to associate IP addresses with MAC addresses on the local network.

### DNS

Observed DNS queries and responses used to resolve domain names into IP addresses.

**Screenshots:**

- `arp-analysis.png`
- `dns-analysis.png`

---

## 5. FTP Traffic Analysis

Created an FTP connection from Kali Linux to the authorized Metasploitable 2 lab machine and captured the traffic using Wireshark.

Analyzed:

- FTP connection traffic
- Login process
- FTP commands and server responses
- File and directory navigation commands

**Finding:** Traditional FTP does not provide encryption by default, meaning sensitive information may be exposed to someone able to observe the traffic.

**Screenshot:** `ftp-traffic-analysis.png`

---

## 6. SSH Traffic Analysis

Captured SSH traffic between systems and analyzed the packets in Wireshark.

Observed that Wireshark could capture the SSH packets, but the communication content was encrypted.

**Finding:** Unlike traditional FTP, SSH encrypts communication, helping protect commands and authentication data from being readable in normal packet captures.

**Screenshot:** `ssh-analysis.png`

---

## 7. HTTP and HTTPS Analysis

Captured and compared HTTP and HTTPS traffic.

### HTTP

Observed that HTTP communication does not provide encryption by itself.

### HTTPS

Observed TLS-encrypted communication used to protect data between the client and server.

**Finding:** HTTPS provides encrypted communication using TLS, making application data significantly more protected than plain HTTP traffic.

**Screenshot:** `http-https-analysis.png`

---

## 8. Detecting Nmap Scan Activity

Generated Nmap scan traffic against the authorized Metasploitable 2 lab environment and captured the packets using Wireshark.

Analyzed the packet patterns created during scanning and observed how scan activity appears in network traffic.

**Finding:** Nmap scans can generate recognizable patterns, such as repeated connection attempts or probes to multiple ports.

**Screenshot:** `nmap-scan-detection.png`

---

## 9. Key Findings

- Wireshark can capture and analyze network packets travelling through a selected network interface.
- TCP communication can be identified through the TCP Three-Way Handshake.
- ARP is used for IP-to-MAC address resolution on local networks.
- DNS resolves domain names to IP addresses.
- Traditional FTP traffic may expose sensitive information because it is not encrypted by default.
- SSH encrypts remote communication.
- HTTP does not provide encryption by itself, while HTTPS uses TLS to protect communication.
- Network scanning activity can be observed and analyzed through packet patterns.

---

## 10. Conclusion

This lab provided hands-on experience with capturing and analyzing network traffic using Wireshark. The practical exercises improved my understanding of network protocols, encrypted and unencrypted communication, packet analysis, and how Nmap scanning activity can appear on a network.