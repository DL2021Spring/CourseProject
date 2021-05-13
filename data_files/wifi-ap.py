





















import sys

import ns.applications
import ns.core
import ns.internet
import ns.mobility
import ns.network
import ns.point_to_point
import ns.wifi















































def SetPosition(node, position):
    mobility = node.GetObject(ns.mobility.MobilityModel.GetTypeId())
    mobility.SetPosition(position)


def GetPosition(node):
    mobility = node.GetObject(ns.mobility.MobilityModel.GetTypeId())
    return mobility.GetPosition()

def AdvancePosition(node):
    pos = GetPosition(node);
    pos.x += 5.0
    if pos.x >= 210.0:
      return
    SetPosition(node, pos)
    ns.core.Simulator.Schedule(ns.core.Seconds(1.0), AdvancePosition, node)


def main(argv):
    ns.core.CommandLine().Parse(argv)

    ns.network.Packet.EnablePrinting();

    
    ns.core.Config.SetDefault("ns3::WifiRemoteStationManager::RtsCtsThreshold", ns.core.StringValue("0"))
    
    ns.core.Config.SetDefault("ns3::WifiRemoteStationManager::FragmentationThreshold", ns.core.StringValue("2200"))

    wifi = ns.wifi.WifiHelper.Default()
    mobility = ns.mobility.MobilityHelper()
    stas = ns.network.NodeContainer()
    ap = ns.network.NodeContainer()
    
    packetSocket = ns.network.PacketSocketHelper()

    stas.Create(2)
    ap.Create(1)

    
    packetSocket.Install(stas)
    packetSocket.Install(ap)

    wifiPhy = ns.wifi.YansWifiPhyHelper.Default()
    wifiChannel = ns.wifi.YansWifiChannelHelper.Default()
    wifiPhy.SetChannel(wifiChannel.Create())

    ssid = ns.wifi.Ssid("wifi-default")
    wifi.SetRemoteStationManager("ns3::ArfWifiManager")
    wifiMac = ns.wifi.NqosWifiMacHelper.Default()

    
    wifiMac.SetType("ns3::StaWifiMac",
                    "Ssid", ns.wifi.SsidValue(ssid),
                    "ActiveProbing", ns.core.BooleanValue(False))
    staDevs = wifi.Install(wifiPhy, wifiMac, stas)
    
    wifiMac.SetType("ns3::ApWifiMac",
                    "Ssid", ns.wifi.SsidValue(ssid),
                    "BeaconGeneration", ns.core.BooleanValue(True),
                    "BeaconInterval", ns.core.TimeValue(ns.core.Seconds(2.5)))
    wifi.Install(wifiPhy, wifiMac, ap)

    
    mobility.Install(stas)
    mobility.Install(ap)

    ns.core.Simulator.Schedule(ns.core.Seconds(1.0), AdvancePosition, ap.Get(0))

    socket = ns.network.PacketSocketAddress()
    socket.SetSingleDevice(staDevs.Get(0).GetIfIndex())
    socket.SetPhysicalAddress(staDevs.Get(1).GetAddress())
    socket.SetProtocol(1)

    onoff = ns.applications.OnOffHelper("ns3::PacketSocketFactory", ns.network.Address(socket))
    onoff.SetAttribute("OnTime", ns.core.RandomVariableValue(ns.core.ConstantVariable(42)))
    onoff.SetAttribute("OffTime", ns.core.RandomVariableValue(ns.core.ConstantVariable(0)))

    apps = onoff.Install(ns.network.NodeContainer(stas.Get(0)))
    apps.Start(ns.core.Seconds(0.5))
    apps.Stop(ns.core.Seconds(43.0))

    ns.core.Simulator.Stop(ns.core.Seconds(44.0))

  
  
  
  
  
  


    ns.core.Simulator.Run()
    ns.core.Simulator.Destroy()

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))

