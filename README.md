# SNMP-Client

### SNMP-Client written in python using the library [pysnmp](https://github.com/etingof/pysnmp)

## Installation

To run the program you need to open the [release](https://github.com/simonnieder/snmp-client/releases/), download the **main.exe** and run it.
Alternatively if you have at least python 3 installed on your system, you can install pysnmp using the command `pip install pysnmp` and then you'd have to run "src/main.py".

## Working Features

- SNMP GET-Request
- SNMP SET-Request
- Receive SNMP-traps
- Scan whole network
- Use SNMPv2-MIB file to request information

## Coming Soon

- Use Custom MIBs added by user

## Usage

`/help` to see all available commands  
`/get` to perform SNMP GET-Request  
`/set` to perform SNMP SET-Request  
`/get-auto` to get basic SNMP information from a client  
`/scan` to scan a network for SNMP devices  
`/listen` to listen for incoming snmp traps  
`/quit` to quit the program

## User Interface

![user interface](https://i.imgur.com/7YD2CFD.png)

Made by Simon Niederwolfsgruber
