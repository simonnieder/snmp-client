import snmpFunctions
import pysnmp
import ipaddress

def getOperation(ip, oid, community):
    try:
        snmpFunctions.get(ip, str(oid), community)
    except pysnmp.smi.error.MibNotFoundError:
        print('OID format not valid! Try again!')
    except pysnmp.smi.error.PySnmpError:
        print('IP-Address format not valid! Try again!')
    
def setOperation(ip, oid, value, community):
    try:
        snmpFunctions.set(ip, str(oid), value, community)
    except pysnmp.smi.error.MibNotFoundError:
        print('OID format not valid! Try again!')
    except pysnmp.smi.error.PySnmpError:
        print('IP-Address format not valid! Try again!')
        
def scanOperation(network, community):
    try: 
        snmpFunctions.scanNetwork(network, community)
    except ipaddress.AddressValueError:
        print("Network address not valid! Try again!")
        
if __name__ == "__main__":
    print("\nSNMP-Client by Simon Niederwolfsgruber\n")
    print("Command list:")
    print("/help to see all available commands\n/get to perform snmp get operation\n/set to perform snmp set operation\n/get-auto to get basic snmp information from a client\n/scan to scan a network for snmp devices\n/listen listen to snmp trap\n")
    
    while True:
        operation = input("Type your command! Type /help to see all available commands\n")
        
        if operation == "/help":
            print("/help to see all available commands\n/get to perform snmp get operation\n/set to perform snmp set operation from a client\n/get-auto to get basic snmp information\n/scan to scan a network for snmp devices\n/listen listen to snmp trap\n")
        
        elif operation == "/get":
            ip = input('Enter the IP you want to use\n')
            community = input('Enter the community (default is "public") press enter to skip input and keep default)\n')
            
            if not community:
                community = "public"
            oid = input('Enter the oid you want to use\n')
            
            getOperation(ip, oid, community)

        elif operation == "/set":
            ip = input('Enter the IP you want to use\n')
            community = input('Enter the community (default is "private") press enter to skip and keep default)\n')
            
            if not community:
                community = "private"
            
            oid = input('Enter the oid whose value you want to set\n')
            value = input('Enter value\n')
            
            setOperation(ip, oid, value, community)
                
        elif operation == "/get-auto":
            ip = input('Enter the IP you want to use\n')
            community = input('Enter the community (default is "public") press enter to skip and keep default)\n')
            
            if not community:
                community = "public"
                
            oids = [".1.3.6.1.2.1.1.3.0", ".1.3.6.1.2.1.1.4.0", ".1.3.6.1.2.1.1.5.0", ".1.3.6.1.2.1.1.6.0", ".1.3.6.1.2.1.1.1.0", ".1.3.6.1.2.1.25.1.6.0"]
            for oid in oids:
                snmpFunctions.get(ip, oid, community)
                
        elif operation == "/scan":
            community = input('Enter the community (default is "private") press enter to skip and keep default)\n')
            
            if not community:
                community = "private"
            network = input("Type your network address (example: 10.10.30.0/24)\n")
            
            scanOperation(network, community)
        
        elif operation == "/listen":
            snmpFunctions.listen()
        else:
            print("Command not valid! Try again!")



'''
uptime: .1.3.6.1.2.1.1.3.0
contact: .1.3.6.1.2.1.1.4.0
name: .1.3.6.1.2.1.1.5.0
location: .1.3.6.1.2.1.1.6.0
systemdescription: .1.3.6.1.2.1.1.1.0
process number: .1.3.6.1.2.1.25.1.6.0
ram size: .1.3.6.1.2.1.25.2.2.0
'''