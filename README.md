# SNMP-Client

### SNMP-Client written in python using the library [pysnmp](https://github.com/etingof/pysnmp)

## Installation

To run the program you need to open the [release](https://github.com/simonnieder/snmp-client/releases/), download the **Source code (zip)** and launch "main.exe" in the /dist folder.  
Alternatively if you have at least python 3 installed on your system, you can install pysnmp using the command `pip install pysnmp` and then you'd have to run "main.py".

## Working Features

- SNMP GET-Request
- SNMP SET-Request
- Receive SNMP-traps
- Scan whole network

## Coming Soon

- Read MIB Information

## Usage

`/help` to see all available commands  
`/get` to perform SNMP GET-Request  
`/set` to perform SNMP SET-Request  
`/get-auto` to get basic SNMP information from a client  
`/scan` to scan a network for SNMP devices  
`/listen` to receive snmp traps  
`/quit` to quit the program

## User Interface

![user interface](https://i.imgur.com/7YD2CFD.png)

Made by Simon Niederwolfsgruber
