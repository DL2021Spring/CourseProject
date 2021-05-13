




















































import ns.applications
import ns.core
import ns.csma
import ns.internet
import ns.mobility
import ns.network
import ns.olsr
import ns.wifi











def main(argv): 
    
    
    
    
    backboneNodes = 10
    infraNodes = 5
    lanNodes = 5
    stopTime = 10

    
    
    
    
    ns.core.Config.SetDefault("ns3::OnOffApplication::PacketSize", ns.core.StringValue("210"))
    ns.core.Config.SetDefault("ns3::OnOffApplication::DataRate", ns.core.StringValue("448kb/s"))

    
    
    
    
    
    cmd = ns.core.CommandLine()
    
    
    
    

    
    
    
    
    cmd.Parse(argv)

    
    
    
    
    

    
    
    
    
    backbone = ns.network.NodeContainer()
    backbone.Create(backboneNodes)
    
    
    
    
    wifi = ns.wifi.WifiHelper()
    mac = ns.wifi.NqosWifiMacHelper.Default()
    mac.SetType("ns3::AdhocWifiMac")
    wifi.SetRemoteStationManager("ns3::ConstantRateWifiManager",
                                  "DataMode", ns.core.StringValue("OfdmRate54Mbps"))
    wifiPhy = ns.wifi.YansWifiPhyHelper.Default()
    wifiChannel = ns.wifi.YansWifiChannelHelper.Default()
    wifiPhy.SetChannel(wifiChannel.Create())
    backboneDevices = wifi.Install(wifiPhy, mac, backbone)
    
    
    
    print "Enabling OLSR routing on all backbone nodes"
    internet = ns.internet.InternetStackHelper()
    olsr = ns.olsr.OlsrHelper()
    internet.SetRoutingHelper(olsr); 
    internet.Install(backbone);
    
    internet.Reset()
    
    
    
    
    ipAddrs = ns.internet.Ipv4AddressHelper()
    ipAddrs.SetBase(ns.network.Ipv4Address("192.168.0.0"), ns.network.Ipv4Mask("255.255.255.0"))
    ipAddrs.Assign(backboneDevices)

    
    
    
    
    mobility = ns.mobility.MobilityHelper()
    positionAlloc = ns.mobility.ListPositionAllocator()
    x = 0.0
    for i in range(backboneNodes):
        positionAlloc.Add(ns.core.Vector(x, 0.0, 0.0))
        x += 5.0
    mobility.SetPositionAllocator(positionAlloc)
    mobility.SetMobilityModel("ns3::RandomDirection2dMobilityModel",
                               "Bounds", ns.mobility.RectangleValue(ns.mobility.Rectangle(0, 1000, 0, 1000)),
                               "Speed", ns.core.RandomVariableValue(ns.core.ConstantVariable(2000)),
                               "Pause", ns.core.RandomVariableValue(ns.core.ConstantVariable(0.2)))
    mobility.Install(backbone)

    
    
    
    
    

    
    
    ipAddrs.SetBase(ns.network.Ipv4Address("172.16.0.0"), ns.network.Ipv4Mask("255.255.255.0"))

    for i in range(backboneNodes):
        print "Configuring local area network for backbone node ", i
        
        
        
        
        
        newLanNodes = ns.network.NodeContainer()
        newLanNodes.Create(lanNodes - 1)
        
        lan = ns.network.NodeContainer(ns.network.NodeContainer(backbone.Get(i)), newLanNodes)
        
        
        
        
        csma = ns.csma.CsmaHelper()
        csma.SetChannelAttribute("DataRate", ns.network.DataRateValue(ns.network.DataRate(5000000)))
        csma.SetChannelAttribute("Delay", ns.core.TimeValue(ns.core.MilliSeconds(2)))
        lanDevices = csma.Install(lan)
        
        
        
        internet.Install(newLanNodes)
        
        
        
        
        ipAddrs.Assign(lanDevices)
        
        
        
        
        ipAddrs.NewNetwork()

    
    
    
    
    

    
    
    ipAddrs.SetBase(ns.network.Ipv4Address("10.0.0.0"), ns.network.Ipv4Mask("255.255.255.0"))

    for i in range(backboneNodes):
        print "Configuring wireless network for backbone node ", i
        
        
        
        
        
        stas = ns.network.NodeContainer()
        stas.Create(infraNodes - 1)
        
        infra = ns.network.NodeContainer(ns.network.NodeContainer(backbone.Get(i)), stas)
        
        
        
        ssid = ns.wifi.Ssid('wifi-infra' + str(i))
        wifiInfra = ns.wifi.WifiHelper.Default()
        wifiPhy.SetChannel(wifiChannel.Create())
        wifiInfra.SetRemoteStationManager('ns3::ArfWifiManager')
        macInfra = ns.wifi.NqosWifiMacHelper.Default();
        macInfra.SetType("ns3::StaWifiMac",
                         "Ssid", ns.wifi.SsidValue(ssid),
                         "ActiveProbing", ns.core.BooleanValue(False))

        
        staDevices = wifiInfra.Install(wifiPhy, macInfra, stas)
        
        macInfra.SetType("ns3::ApWifiMac",
                         "Ssid", ns.wifi.SsidValue(ssid),
                         "BeaconGeneration", ns.core.BooleanValue(True),
                         "BeaconInterval", ns.core.TimeValue(ns.core.Seconds(2.5)))
        apDevices = wifiInfra.Install(wifiPhy, macInfra, backbone.Get(i))
        
        infraDevices = ns.network.NetDeviceContainer(apDevices, staDevices)

        
        
        internet.Install(stas)
        
        
        
        
        ipAddrs.Assign(infraDevices)
        
        
        
        
        ipAddrs.NewNetwork()
        
        
        
        
        subnetAlloc = ns.mobility.ListPositionAllocator()
        for j in range(infra.GetN()):
            subnetAlloc.Add(ns.core.Vector(0.0, j, 0.0))

        mobility.PushReferenceMobilityModel(backbone.Get(i))
        mobility.SetPositionAllocator(subnetAlloc)
        mobility.SetMobilityModel("ns3::RandomDirection2dMobilityModel",
                                  "Bounds", ns.mobility.RectangleValue(ns.mobility.Rectangle(-25, 25, -25, 25)),
                                  "Speed", ns.core.RandomVariableValue(ns.core.ConstantVariable(30)),
                                  "Pause", ns.core.RandomVariableValue(ns.core.ConstantVariable(0.4)))
        mobility.Install(infra)

    
    
    
    
    

    
    
    print "Create Applications."
    port = 9   

    
    
    assert(lanNodes >= 5)
    appSource = ns.network.NodeList.GetNode(11)
    appSink = ns.network.NodeList.GetNode(13)
    remoteAddr = ns.network.Ipv4Address("172.16.0.5")

    onoff = ns.applications.OnOffHelper("ns3::UdpSocketFactory", 
                            ns.network.Address(ns.network.InetSocketAddress(remoteAddr, port)))
    onoff.SetAttribute("OnTime", ns.core.RandomVariableValue(ns.core.ConstantVariable(1)))
    onoff.SetAttribute("OffTime", ns.core.RandomVariableValue(ns.core.ConstantVariable(0)))
    apps = onoff.Install(ns.network.NodeContainer(appSource))
    apps.Start(ns.core.Seconds(3.0))
    apps.Stop(ns.core.Seconds(20.0))

    
    sink = ns.applications.PacketSinkHelper("ns3::UdpSocketFactory", 
                                ns.network.InetSocketAddress(ns.network.Ipv4Address.GetAny(), port))
    apps = sink.Install(ns.network.NodeContainer(appSink))
    apps.Start(ns.core.Seconds(3.0))

    
    
    
    
    

    print "Configure Tracing."
    
    
    
    
    
    
    
    
    print "(tracing not done for Python)"
    
    
    

    
    wifiPhy.EnablePcap("mixed-wireless", backboneDevices)
    
    csma = ns.csma.CsmaHelper()
    csma.EnablePcapAll("mixed-wireless", False)







    
    
    
    
    

    print "Run Simulation."
    ns.core.Simulator.Stop(ns.core.Seconds(stopTime))
    ns.core.Simulator.Run()
    ns.core.Simulator.Destroy()


if __name__ == '__main__':
    import sys
    main(sys.argv)


