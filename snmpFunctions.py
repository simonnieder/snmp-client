from pysnmp.hlapi import *
import ipaddress
from threading import Thread
import asyncio


def get(ip, oid, communityName): #executes SNMP GET-operation
    iterator = getCmd(
        SnmpEngine(),
        CommunityData(communityName),
        UdpTransportTarget((ip, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(oid)))
    
    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    # if errorIndication:
        #print(errorIndication)
    if errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))


def set(ip, oid, value, communityName): #executes SNMP SET-operation
    iterator = setCmd(
        SnmpEngine(),
        CommunityData(communityName),
        UdpTransportTarget((ip, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(oid), value))
    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        print('Value set\n')



def iterateIPs(network, community = "public"): #iterates through ips of a given network
    for ip in ipaddress.IPv4Network(network):
        oids = [".1.3.6.1.2.1.1.3.0"]
        for oid in oids:
            thread = Thread(target = get,args =(str(ip), oid, community))
            thread.start()
