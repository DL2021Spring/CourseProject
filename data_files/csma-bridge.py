





























import ns.applications
import ns.bridge
import ns.core
import ns.csma
import ns.internet
import ns.network


def main(argv):

    
    
    
    
    cmd = ns.core.CommandLine()
    cmd.Parse(argv)

    
    
    
    
    terminals = ns.network.NodeContainer()
    terminals.Create(4)

    csmaSwitch = ns.network.NodeContainer()
    csmaSwitch.Create(1)

    
    csma = ns.csma.CsmaHelper()
    csma.SetChannelAttribute("DataRate", ns.network.DataRateValue(ns.network.DataRate(5000000)))
    csma.SetChannelAttribute("Delay", ns.core.TimeValue(ns.core.MilliSeconds(2)))

    

    terminalDevices = ns.network.NetDeviceContainer()
    switchDevices = ns.network.NetDeviceContainer()

    for i in range(4):
        link = csma.Install(ns.network.NodeContainer(ns.network.NodeContainer(terminals.Get(i)), csmaSwitch))
        terminalDevices.Add(link.Get(0))
        switchDevices.Add(link.Get(1))

    
    switchNode = csmaSwitch.Get(0)
    bridgeDevice = ns.bridge.BridgeNetDevice()
    switchNode.AddDevice(bridgeDevice)

    for portIter in range(switchDevices.GetN()):
        bridgeDevice.AddBridgePort(switchDevices.Get(portIter))

    
    internet = ns.internet.InternetStackHelper()
    internet.Install(terminals)

    
    
    
    ipv4 = ns.internet.Ipv4AddressHelper()
    ipv4.SetBase(ns.network.Ipv4Address("10.1.1.0"), ns.network.Ipv4Mask("255.255.255.0"))
    ipv4.Assign(terminalDevices)

    
    
    
    
    port = 9   

    onoff = ns.applications.OnOffHelper("ns3::UdpSocketFactory", 
                            ns.network.Address(ns.network.InetSocketAddress(ns.network.Ipv4Address("10.1.1.2"), port)))
    onoff.SetAttribute("OnTime", ns.core.RandomVariableValue(ns.core.ConstantVariable(1)))
    onoff.SetAttribute("OffTime", ns.core.RandomVariableValue(ns.core.ConstantVariable(0)))

    app = onoff.Install(ns.network.NodeContainer(terminals.Get(0)))
    
    app.Start(ns.core.Seconds(1.0))
    app.Stop(ns.core.Seconds(10.0))

    
    sink = ns.applications.PacketSinkHelper("ns3::UdpSocketFactory",
                                ns.network.Address(ns.network.InetSocketAddress(ns.network.Ipv4Address.GetAny(), port)))
    app = sink.Install(ns.network.NodeContainer(terminals.Get(1)))
    app.Start(ns.core.Seconds(0.0))

    
    
    
    onoff.SetAttribute("Remote", 
                       ns.network.AddressValue(ns.network.InetSocketAddress(ns.network.Ipv4Address("10.1.1.1"), port)))
    app = onoff.Install(ns.network.NodeContainer(terminals.Get(3)))
    app.Start(ns.core.Seconds(1.1))
    app.Stop(ns.core.Seconds(10.0))

    app = sink.Install(ns.network.NodeContainer(terminals.Get(0)))
    app.Start(ns.core.Seconds(0.0))

    
    
    
    
    
    
    

    
    
    
    
    
    
    
    csma.EnablePcapAll("csma-bridge", False)

    
    
    
    
    ns.core.Simulator.Run()
    ns.core.Simulator.Destroy()
    



if __name__ == '__main__':
    import sys
    main(sys.argv)

