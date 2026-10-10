# Router Configuration (Cisco Packet Tracer)

## Introduction

Router configuration is the process of assigning IP addresses and enabling interfaces so that different devices and networks can communicate with each other.

In this repository, Cisco Packet Tracer is used to practice router configuration.

---

# What is Cisco Packet Tracer?

Cisco Packet Tracer is a network simulation software developed by Cisco.

It allows users to:

- Build virtual networks
- Configure routers and switches
- Assign IP addresses
- Test connectivity
- Practice CCNA networking concepts

---

# Basic Router Configuration Steps

## Step 1: Create the Network Topology

Place the required devices in Packet Tracer.

Example:

```
PC1 -------- Router -------- PC2
```

Connect the devices using the appropriate cable.

---

## Step 2: Open the Router CLI

Click:

```
Router
↓
CLI
```

The Command Line Interface (CLI) is used to configure the router.

---

# Basic Router Commands

## 1. Enter Privileged EXEC Mode

```bash
enable
```

Purpose:

Moves from User EXEC Mode to Privileged EXEC Mode.

Prompt changes from:

```
Router>
```

to

```
Router#
```

---

## 2. Enter Global Configuration Mode

```bash
configure terminal
```

or

```bash
conf t
```

Purpose:

Allows configuration changes on the router.

Prompt becomes:

```
Router(config)#
```

---

## 3. Select the Interface

Example:

```bash
interface gigabitEthernet0/0/0
```

or

```bash
interface g0/0/0
```

Purpose:

Selects the interface that will be configured.

Prompt becomes:

```
Router(config-if)#
```

---

## 4. Assign an IP Address

Example:

```bash
ip address 192.168.1.1 255.255.255.0
```

Purpose:

Assigns an IP address and subnet mask to the interface.

---

## 5. Enable the Interface

```bash
no shutdown
```

Purpose:

Activates the interface.

By default, router interfaces are administratively down.

---

## 6. Exit Interface Configuration

```bash
exit
```

Returns to Global Configuration Mode.

---

## 7. Return to Privileged Mode

```bash
exit
```

or

```bash
end
```

Prompt becomes:

```
Router#
```

---

## 8. Verify Interface Configuration

```bash
show ip interface brief
```

Purpose:

Displays:

- Interface names
- Assigned IP addresses
- Interface status
- Protocol status

Example Output:

```
Interface      IP Address      Status
G0/0/0         192.168.1.1     up
```

---

# Configure the PC

Open:

```
PC
↓
Desktop
↓
IP Configuration
```

Assign:

| Setting | Example |
|----------|----------|
| IP Address | 192.168.1.2 |
| Subnet Mask | 255.255.255.0 |
| Default Gateway | 192.168.1.1 |

---

# Test Connectivity

Open Command Prompt on the PC.

Run:

```bash
ping 192.168.1.1
```

If replies are received, the PC can communicate with the router.

Example:

```
Reply from 192.168.1.1
```

---

# Common Commands

| Command | Purpose |
|----------|----------|
| enable | Enter Privileged Mode |
| configure terminal | Enter Configuration Mode |
| interface g0/0/0 | Select Interface |
| ip address | Assign IP Address |
| no shutdown | Enable Interface |
| exit | Exit Current Mode |
| end | Return to Privileged Mode |
| show ip interface brief | View Interface Details |

---

# Troubleshooting Tips

If the ping fails:

- Check the cable connection.
- Verify the IP address.
- Verify the subnet mask.
- Ensure the interface is enabled using `no shutdown`.
- Check the interface status using:

```bash
show ip interface brief
```

---

# Summary

- Cisco Packet Tracer is used to simulate real networks.
- Routers must be configured before communication can occur.
- Every interface requires an IP address.
- Interfaces are disabled by default and must be enabled using `no shutdown`.
- Use `ping` to test connectivity.