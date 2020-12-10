from pysnmp.hlapi import *
import ipaddress
from threading import Thread
from pysnmp.entity import engine, config
from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.entity.rfc3413 import ntfrcv

def listen(): #listens for incoming traps  #! currently no way of stopping the function
    Port=163 
    myEngine = engine.SnmpEngine()
    print("Listening on port:" + str(Port))
    config.addTransport(
        myEngine,
        udp.domainName + (1,),
        udp.UdpTransport().openServerMode(("localhost", Port))
    )

    #Configure community here
    config.addV1System(myEngine, 'community', 'public')
    def cbFun(snmpEngine, stateReference, contextEngineId, contextName,
            varBinds, cbCtx):
        print("Received new Trap message")
        for name, val in varBinds:        
            print(f"{name.prettyPrint()} = {val.prettyPrint()}")

    ntfrcv.NotificationReceiver(myEngine, cbFun)

    myEngine.transportDispatcher.jobStarted(1)  

    try:
        myEngine.transportDispatcher.runDispatcher()
    except:
        myEngine.transportDispatcher.closeDispatcher()
        raise
    
def get(ip, oid, communityName): #executes SNMP GET-operation
    iterator = getCmd(
        SnmpEngine(),
        CommunityData(communityName),
        UdpTransportTarget((ip, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(oid)))
    
    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
    
    if errorIndication:
        print(f"{ip} not reachable")
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        result = ip;
        for varBind in varBinds:
            for x in varBinds:
                result = result +  " " + str(x)
        print(result)
                
    
def set(ip, oid, value, communityName): #executes SNMP SET-operation
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
        print('Value set\n')
            
            
def scanNetwork(network, community): #iterates through all ips of a given network and makes a snmp request to get host name
    for ip in ipaddress.IPv4Network(network):
        oids = [".1.3.6.1.2.1.1.5.0"]
        for oid in oids:
            thread = Thread(target = get,args =(str(ip), oid, community))
            thread.start()

