import snmpFunctions

while True:
    operation = input("What do you want to do? Type /get to perform get operation, /set to perform set operation, /get-auto to get basic snmp information\n")
    if operation == "/get":
        ip = input('Enter the IP you want to use\n')
        community = input('Enter the community (default is "public") press enter to skip input and keep default)\n')
        if not community:
            community = "public"
        oid = input('Enter the oid you want to use\n')
        snmpFunctions.get(ip, str(oid), community)
    elif operation == "/set":
        ip = input('Enter the IP you want to use\n')
        community = input('Enter the community (default is "private") press enter to skip and keep default)\n')
        if not community:
            community = "private"
        oid = input('Enter the oid whose value you want to set\n')
        value = input('Enter value\n')
        snmpFunctions.set(ip, str(oid), value, community)
    elif operation == "/get-auto":
        ip = input('Enter the IP you want to use\n')
        community = input('Enter the community (default is "private") press enter to skip and keep default)\n')
        if not community:
            community = "private"
        oids = [".1.3.6.1.2.1.1.3.0", ".1.3.6.1.2.1.1.4.0", ".1.3.6.1.2.1.1.5.0", ".1.3.6.1.2.1.1.1.0", ".1.3.6.1.2.1.25.1.6.0"]
        for oid in oids:
            snmpFunctions.get(ip, oid, community)
    else:
        print("Command invalid. Try again")


'''
uptime: .1.3.6.1.2.1.1.3.0
contact: .1.3.6.1.2.1.1.4.0
name: .1.3.6.1.2.1.1.5.0
location: .1.3.6.1.2.1.1.6.0
systemdescription: .1.3.6.1.2.1.1.1.0
process number: .1.3.6.1.2.1.25.1.6.0
ram size: .1.3.6.1.2.1.25.2.2.0
'''