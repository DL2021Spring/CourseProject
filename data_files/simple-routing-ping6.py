




























import ns.applications
import ns.core
import ns.csma
import ns.internet
import ns.network

def main(argv):

    cmd = ns.core.CommandLine();

    cmd.Parse(argv);

    
    print "Create nodes"
    n0 = ns.network.Node();
    r = ns.network.Node();
    n1 = ns.network.Node();

    net1 = ns.network.NodeContainer();
    net1.Add(n0);
    net1.Add(r);
    net2 = ns.network.NodeContainer();
    net2.Add(r);
    net2.Add(n1);
    all = ns.network.NodeContainer();
    all.Add(n0);
    all.Add(r);
    all.Add(n1);

    
    internetv6 = ns.internet.InternetStackHelper();
    internetv6.Install(all);

    
    csma = ns.csma.CsmaHelper();
    csma.SetChannelAttribute("DataRate", ns.network.DataRateValue(ns.network.DataRate(5000000)));
    csma.SetChannelAttribute("Delay", ns.core.TimeValue(ns.core.MilliSeconds(2)));
    d1 = csma.Install(net1);
    d2 = csma.Install(net2);

    
    print "Addressing"
    ipv6 = ns.internet.Ipv6AddressHelper();
    ipv6.NewNetwork(ns.network.Ipv6Address("2001:1::"), ns.network.Ipv6Prefix(64));
    i1 = ipv6.Assign(d1);
    i1.SetRouter(1, True);
    ipv6.NewNetwork(ns.network.Ipv6Address("2001:2::"), ns.network.Ipv6Prefix(64));
    i2 = ipv6.Assign(d2);
    i2.SetRouter(0, True);

    
    print "Application"
    packetSize = 1024;
    maxPacketCount = 5;
    interPacketInterval = ns.core.Seconds(1.);
    ping6 = ns.applications.Ping6Helper();

    ping6.SetLocal(i1.GetAddress(0, 1));
    ping6.SetRemote(i2.GetAddress(1, 1)); 

    ping6.SetAttribute("MaxPackets", ns.core.UintegerValue(maxPacketCount));
    ping6.SetAttribute("Interval", ns.core.TimeValue(interPacketInterval));
    ping6.SetAttribute("PacketSize", ns.core.UintegerValue(packetSize));

    apps = ping6.Install(ns.network.NodeContainer(net1.Get(0)));
    apps.Start(ns.core.Seconds(2.0));
    apps.Stop(ns.core.Seconds(20.0));

    print "Tracing"
    ascii = ns.network.AsciiTraceHelper()
    csma.EnableAsciiAll(ascii.CreateFileStream("simple-routing-ping6.tr"))
    csma.EnablePcapAll("simple-routing-ping6", True)

    
    ns.core.Simulator.Run()
    ns.core.Simulator.Destroy()

if __name__ == '__main__':
    import sys
    main(sys.argv)

