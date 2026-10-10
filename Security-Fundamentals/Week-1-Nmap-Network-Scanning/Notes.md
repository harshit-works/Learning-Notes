# Nmap - Network Scanning Notes

## What is Nmap?

Nmap (Network Mapper) is a network scanning tool used to discover hosts, open ports, services, and information about systems on a network.

Nmap can be used for:

- Host discovery
- Port scanning
- Service detection
- Version detection
- OS detection
- Network reconnaissance

> Note: Nmap should only be used on systems and networks you own or have permission to test.

---

# Host Discovery

Host discovery is used to find active devices on a network.

## Ping Scan

nmap -sn <target>

The `-sn` option performs host discovery without performing a port scan.

Example:

nmap -sn 192.168.56.0/24

This checks which hosts are active on the specified network.

---

# Scanning Multiple Hosts

## Scan a Range of IP Addresses

nmap 192.168.56.1-100

## Scan an Entire Subnet

nmap 192.168.56.0/24

---

# Excluding Hosts

A specific host can be excluded from a scan.

nmap 192.168.56.0/24 --exclude 192.168.56.10

---

# Port Scanning

Ports are communication endpoints used by services and applications.

Nmap scans ports to determine whether they are:

- Open
- Closed
- Filtered

## Open

A service is listening and accepting connections on the port.

## Closed

The host is reachable, but no service is listening on that port.

## Filtered

Nmap cannot determine whether the port is open because a firewall or filtering device may be blocking the scan.

---

# TCP and UDP

## TCP

TCP is connection-oriented and uses a handshake to establish communication.

### SYN Scan

sudo nmap -sS <target>

### TCP Connect Scan

nmap -sT <target>

## UDP

UDP is connectionless.

### UDP Scan

sudo nmap -sU <target>

UDP scans can be slower because UDP services may not always respond.

---

# TCP SYN Scan

sudo nmap -sS <target>

`-sS` performs a SYN scan.

Nmap sends a SYN packet to the target.

If a port is open, the target normally responds with SYN/ACK.

Nmap then determines the port state without completing a normal full TCP connection.

---

# TCP Connect Scan

nmap -sT <target>

`-sT` performs a full TCP connection using the operating system's connect() function.

---

# UDP Scan

sudo nmap -sU <target>

`-sU` is used to scan UDP ports and identify UDP services.

---

# DNS Resolution

Nmap may try to resolve IP addresses to hostnames.

## Disable DNS Resolution

nmap -n <target>

## Force DNS Resolution

nmap -R <target>

---

# Port Specification

## Scan a Specific Port

nmap -p 80 <target>

## Scan Multiple Ports

nmap -p 22,80,443 <target>

## Scan a Range of Ports

nmap -p 1-1000 <target>

## Scan All TCP Ports

nmap -p- <target>

`-p-` scans ports from 1 to 65535.

---

# Service and Version Detection

nmap -sV <target>

`-sV` attempts to identify the services running on open ports and their versions.

This provides more information about the software running on the target.

---

# OS Detection

sudo nmap -O <target>

`-O` attempts to identify the operating system of the target.

OS detection may not always be 100% accurate.

---

# Aggressive Scan

sudo nmap -A <target>

The `-A` option enables multiple advanced detection features, including:

- OS detection
- Version detection
- Script scanning
- Traceroute

It generates more network traffic than a basic scan.

---

# Nmap Scripting Engine (NSE)

NSE allows Nmap to run scripts for additional information gathering and security checks.

Example:

nmap --script <script-name> <target>

NSE scripts should only be used against authorized targets.

---

# Understanding Nmap Output

Nmap output can provide information such as:

- Target IP address
- Host status
- Open ports
- Closed ports
- Filtered ports
- Service names
- Service versions
- OS detection results

This information helps identify the services exposed by a target system.

---

# Important Nmap Commands

| Command | Purpose |
|---|---|
| `nmap <target>` | Basic scan |
| `nmap -sn <target>` | Host discovery without port scanning |
| `nmap -sS <target>` | TCP SYN scan |
| `nmap -sT <target>` | TCP Connect scan |
| `sudo nmap -sU <target>` | UDP scan |
| `nmap -p <port> <target>` | Scan a specific port |
| `nmap -p- <target>` | Scan all TCP ports |
| `nmap -sV <target>` | Service and version detection |
| `sudo nmap -O <target>` | OS detection |
| `sudo nmap -A <target>` | Aggressive scan |
| `nmap -n <target>` | Disable DNS resolution |
| `nmap -R <target>` | Force DNS resolution |