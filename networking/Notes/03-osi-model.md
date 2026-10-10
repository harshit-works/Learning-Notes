# OSI Model

## What is the OSI Model?

The **OSI (Open Systems Interconnection) Model** is a conceptual framework that explains how data travels from one device to another over a network.

It divides network communication into **7 layers**, where each layer performs a specific task.

---

# Why do we use the OSI Model?

The OSI Model helps us:

- Standardize network communication.
- Understand how data flows across a network.
- Troubleshoot networking problems.
- Design and develop networking protocols.

---

# 7 Layers of the OSI Model

```
+------------------------+
| 7. Application Layer   |
+------------------------+
| 6. Presentation Layer  |
+------------------------+
| 5. Session Layer       |
+------------------------+
| 4. Transport Layer     |
+------------------------+
| 3. Network Layer       |
+------------------------+
| 2. Data Link Layer     |
+------------------------+
| 1. Physical Layer      |
+------------------------+
```

---

# Layer 7 – Application Layer

### Purpose

Provides network services directly to end-user applications.

### Examples

- Web Browser
- Zoom
- Gmail
- WhatsApp
- FTP Client

### Common Protocols

- HTTP
- HTTPS
- FTP
- SMTP
- DNS

---

# Layer 6 – Presentation Layer

### Purpose

Formats, encrypts, compresses, and translates data before sending it.

### Responsibilities

- Data Encryption
- Data Decryption
- Compression
- Data Format Conversion

### Examples

- JPEG
- PNG
- MP3
- MP4
- SSL/TLS Encryption

---

# Layer 5 – Session Layer

### Purpose

Creates, manages, and terminates communication sessions between two devices.

### Functions

- Starts a session
- Maintains the session
- Ends the session

Example:

A Zoom meeting remains active because the Session Layer maintains the connection.

---

# Layer 4 – Transport Layer

### Purpose

Provides end-to-end communication between sender and receiver.

### Responsibilities

- Reliable delivery
- Error checking
- Flow control
- Data segmentation

### Protocols

- TCP
- UDP

### PDU

Segment

---

# Layer 3 – Network Layer

### Purpose

Determines the best path for data to travel between different networks.

### Responsibilities

- Logical Addressing (IP Address)
- Routing
- Path Selection

### Device

Router

### Protocol

IP (Internet Protocol)

### PDU

Packet

---

# Layer 2 – Data Link Layer

### Purpose

Transfers data between devices connected to the same network.

### Responsibilities

- MAC Addressing
- Error Detection
- Framing

### Device

Switch

### Address Used

MAC Address

### PDU

Frame

---

# Layer 1 – Physical Layer

### Purpose

Transmits raw bits over the physical medium.

### Responsibilities

- Electrical Signals
- Fiber Optics
- Copper Cable
- Wireless Signals

### Examples

- Ethernet Cable
- Fiber Cable
- RJ45 Connector

### PDU

Bits

---

# PDU (Protocol Data Unit)

Each layer has a different name for the transmitted data.

| Layer | PDU |
|--------|-----|
| Application | Data |
| Presentation | Data |
| Session | Data |
| Transport | Segment |
| Network | Packet |
| Data Link | Frame |
| Physical | Bits |

---

# Devices Associated with OSI Layers

| Layer | Device |
|--------|---------|
| Layer 3 | Router |
| Layer 2 | Switch |
| Layer 1 | Hub / Cable |

---

# Data Flow Through the OSI Model

When data is sent:

```
Application
↓
Presentation
↓
Session
↓
Transport
↓
Network
↓
Data Link
↓
Physical
```

When the receiver gets the data, it moves upward through the layers in reverse order.

---

# Mnemonic

Top to Bottom

```
All
People
Seem
To
Need
Data
Processing
```

Bottom to Top

```
Please
Do
Not
Throw
Sausage
Pizza
Away
```

---

# Real-Life Example

Suppose you open **google.com** in your browser.

- Application Layer → Browser creates the request.
- Presentation Layer → Data is encrypted using HTTPS.
- Session Layer → Creates the communication session.
- Transport Layer → Breaks data into TCP segments.
- Network Layer → Adds IP addresses and routes packets.
- Data Link Layer → Adds MAC addresses.
- Physical Layer → Sends bits through Ethernet or Wi-Fi.

The receiving server performs the same process in reverse order.

