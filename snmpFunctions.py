from pysnmp.hlapi import *
import ipaddress
from threading import Thread
from pysnmp.entity import engine, config
from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.entity.rfc3413 import ntfrcv

def listen(port): #listens for incoming traps
    try:
        myEngine = engine.SnmpEngine()
        print("Listening on port:" + str(port))
        config.addTransport(
            myEngine,
            udp.domainName + (1,),
            udp.UdpTransport().openServerMode(("localhost", port))
        )


        config.addV1System(myEngine, 'community', 'public')
        def printFunc(snmpEngine, stateReference, contextEngineId, contextName,
                varBinds, cbCtx):
            print("Received new Trap message")
            for name, val in varBinds:        
                print(f"{name.prettyPrint()} = {val.prettyPrint()}")

        ntfrcv.NotificationReceiver(myEngine, printFunc)

        myEngine.transportDispatcher.jobStarted(1)  

        try:
            myEngine.transportDispatcher.runDispatcher()
        except:
            myEngine.transportDispatcher.closeDispatcher()
            raise
    except KeyboardInterrupt:
        pass
    
def get(ip, communityName, oid, isThreaded = False): #executes SNMP GET-operation
    iterator = getCmd(
        SnmpEngine(),
        CommunityData(communityName),
        UdpTransportTarget((ip, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(oid)))
    
    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
    
    if errorIndication:
        if isThreaded == False:
            print(f"{ip} not reachable")
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        if isThreaded:
            for varBind in varBinds:
                print(f"{ip}: OID = {oid}, VALUE = {varBind[1]}")
        else:
            for varBind in varBinds:
                return varBind[1]
   
def set(ip, communityName, oid, value): #executes SNMP SET-operation
    iterator = setCmd(
        SnmpEngine(),
        CommunityData(communityName),
        UdpTransportTarget((ip, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(oid), value))
    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        print(f"{ip} not reachable")
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        print(f'Value({value}) has been set!\n')
            
            
def scanNetwork(network, community): #iterates through all ips of a given network and makes a snmp request to get host name
    threads = []
    counter = 0
    for ip in ipaddress.IPv4Network(network):
        oids = [".1.3.6.1.2.1.1.5.0"]
        for oid in oids:
            thread = Thread(target = get,args =(str(ip), community, oid, True))
            thread.start()
            threads.append(thread)
            counter+=1

    for thread in threads:
        thread.join()
