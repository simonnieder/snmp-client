import snmpFunctions
import pysnmp
import ipaddress


def inputIP(): #performs the ip input
    return input('Enter the IP you want to use\n')


def inputCommunity(): #performs the community input
    default = 'public'
    community = input(f'Enter the community! Default is {default}. Press enter to skip input and keep default.\n')
    if not community:
        community = default
    return community


def inputOID(): #performs the oid input
    return input('Enter the Objectname you want to use\n')


def getOperation(ip, community, oid): #performs the GET operation and handles result + errors
    try:
        print(f'{ip} OID = {oid}, VALUE = {snmpFunctions.get(ip, community, oid)}')
    except pysnmp.smi.error.MibNotFoundError:
        print(f'OID {oid} is not valid! Try again!')
    except pysnmp.smi.error.PySnmpError:
        print(f'IP-Address {ip} is not valid! Try again!')
        

def setOperation(ip, community, oid, value): #performs the SET operation and handles result + errors
    try:
        snmpFunctions.set(ip, community, oid, value)
    except pysnmp.smi.error.MibNotFoundError:
        print(f'OID {oid} is not valid! Try again!')
    except pysnmp.smi.error.PySnmpError:
        print(f'IP-Address {ip} is not valid! Try again!')
        

def getMibOperation(ip, community,oid, mib): #performs the GET operation using mib files and handles result + errors
    if not mib:
        mib = 'SNMPv2-MIB'
    try:
        print(f'{ip} OID = {oid}, VALUE = {snmpFunctions.getWithMib(ip, community,oid, mib)}')
    except pysnmp.smi.error.MibNotFoundError:
        print(f'OID {oid} is not valid! Try again!')
    except pysnmp.smi.error.PySnmpError:
        print(f'IP-Address {ip} is not valid! Try again!')


if __name__ == '__main__':
    print('\nSNMP-Client by Simon Niederwolfsgruber\n')
    
    while True:
        operation = input('Type your command! Type /help to see all available commands\n')
        
        if operation == '/help':
            print('/help to see all available commands\n/get to perform snmp get operation\n/set to perform snmp set operation from a client\n/get-auto to get basic snmp information\n/get-mib get operation using mib files\n/scan to scan a network for snmp devices\n/listen receive snmp trap\n/quit quit the program\n')
        
        elif operation == '/get':
            getOperation(inputIP(), inputCommunity(), inputOID())
            
        elif operation == '/get-mib':
            getMibOperation(inputIP(), inputCommunity(), inputOID(), input('Enter the name of the mib file (default is SNMPv2-MIB). Press enter to skip input and keep default.\n'))
        
        elif operation == '/set':
            setOperation(inputIP(), inputCommunity('private'),inputOID(), input('Enter new value.\n'))
        
        elif operation == '/get-auto':
            ip = inputIP()
            community = inputCommunity()
            oids = ['.1.3.6.1.2.1.1.3.0', '.1.3.6.1.2.1.1.4.0', '.1.3.6.1.2.1.1.5.0', '.1.3.6.1.2.1.1.6.0', '.1.3.6.1.2.1.1.1.0', '.1.3.6.1.2.1.25.1.6.0']
            for oid in oids:
                getOperation(ip, community, oid)
                
        elif operation == '/scan':
            print('Reachable IPs will return their sysName. This can take a few seconds')
            network = input('Enter the network address you want to scan (example: 10.10.30.0/24)\n')
            try: 
                snmpFunctions.scanNetwork(network, inputCommunity())
            except ipaddress.AddressValueError:
                print(f'Network {network} is not valid! Try again!')
        
        elif operation == '/listen':
            print('Press Ctrl + C to stop listening!')
            port = input('Type the port you want to listen on:\n')
            snmpFunctions.listen(int(port))
            
        elif operation == '/quit':
            exit(0)

        else:
            print('Command not valid! Try again!')
            


'''
uptime: .1.3.6.1.2.1.1.3.0
contact: .1.3.6.1.2.1.1.4.0
name: .1.3.6.1.2.1.1.5.0
location: .1.3.6.1.2.1.1.6.0
systemdescription: .1.3.6.1.2.1.1.1.0
process number: .1.3.6.1.2.1.25.1.6.0
ram size: .1.3.6.1.2.1.25.2.2.0
'''