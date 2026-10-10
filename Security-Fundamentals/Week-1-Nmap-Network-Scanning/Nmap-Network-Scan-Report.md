# Nmap Network Scan Report

## Objective

The objective of this lab was to use Nmap to perform network discovery and scan an authorized target in my personal Kali Linux and Windows lab environment.

The scans were performed to identify:

- Active hosts
- Open ports
- Running services
- Service versions
- Possible operating system information

All scans were performed only in my own authorized lab environment.

---

## Lab Environment

### Attacker Machine

- Operating System: Kali Linux
- Tool Used: Nmap

### Target Machine

- Operating System: Windows
- Target IP: <TARGET-IP>

### Network

- Network Range: <NETWORK-RANGE>

---

# 1. Host Discovery

## Command

nmap -sn <NETWORK-RANGE>

## Purpose

This command was used to discover active hosts on the network without performing a port scan.

## Result

Nmap identified the active hosts available on the lab network.

Screenshot: 01-host-discovery.png

---

# 2. Basic Nmap Scan

## Command

nmap <TARGET-IP>

## Purpose

This command was used to perform a basic scan of the target and identify accessible ports and services.

## Result

The scan showed the ports discovered on the target and their states.

Screenshot: 02-basic-port-scan.png

---

# 3. TCP SYN Scan

## Command

sudo nmap -sS <TARGET-IP>

## Purpose

A SYN scan was performed to check the TCP ports of the target.

Nmap sends a SYN packet and analyzes the response to determine the state of the port.

## Result

The scan identified the TCP port states of the target.

Screenshot: 03-syn-scan.png

---

# 4. Service and Version Detection

## Command

nmap -sV <TARGET-IP>

## Purpose

This scan was used to identify services running on open ports and attempt to detect their versions.

## Result

Nmap provided information about the services discovered on the target.

Screenshot: 04-service-version-detection.png

---

# 5. OS Detection

## Command

sudo nmap -O <TARGET-IP>

## Purpose

This scan was used to attempt operating system detection based on the target's network responses.

## Result

Nmap attempted to identify the operating system of the target.

OS detection results may not always be completely accurate.

Screenshot: 05-os-detection.png

---

# Findings

The Nmap scans provided information about the target system's network exposure.

The main information collected included:

- Active host status
- Open or accessible ports
- Detected services
- Service version information
- Possible operating system information

The exact results depend on the configuration of the Windows target machine and the services running during the scan.

---

# Security Analysis

Open ports increase the attack surface of a system because they may expose network services to other devices.

It is important to:

- Close unnecessary ports
- Disable unused services
- Keep services updated
- Use firewall rules to restrict access
- Monitor exposed services regularly

Network scanning helps security professionals understand which services are exposed and identify areas that may require further security review.

---

# Skills Practiced

- Network discovery
- Host discovery
- Port scanning
- TCP SYN scanning
- Service and version detection
- Operating system detection
- Understanding Nmap output
- Basic network reconnaissance

---

# Disclaimer

All scans in this project were performed only against systems and networks that I own or have explicit permission to test.