

















import sys

import ns.core
import ns.csma
import ns.internet
import ns.network
import ns.tap_bridge

def main(argv):
    
    
    
    
    
    ns.core.GlobalValue.Bind("SimulatorImplementationType", ns.core.StringValue("ns3::RealtimeSimulatorImpl"))
    ns.core.GlobalValue.Bind("ChecksumEnabled", ns.core.BooleanValue("true"))

    
    
    
    
    
    nodes = ns.network.NodeContainer()
    nodes.Create (2)

    
    
    
    
    
    csma = ns.csma.CsmaHelper()
    devices = csma.Install(nodes)

    
    
    
    
    
    
    
    
    tapBridge = ns.tap_bridge.TapBridgeHelper()
    tapBridge.SetAttribute ("Mode", ns.core.StringValue ("UseLocal"))
    tapBridge.SetAttribute ("DeviceName", ns.core.StringValue ("tap-left"))
    tapBridge.Install (nodes.Get (0), devices.Get (0))

    
    
    
    
    tapBridge.SetAttribute ("DeviceName", ns.core.StringValue ("tap-right"))
    tapBridge.Install (nodes.Get (1), devices.Get (1))

    
    
    
    ns.core.Simulator.Stop (ns.core.Seconds (600))
    ns.core.Simulator.Run(signal_check_frequency = -1)
    ns.core.Simulator.Destroy()
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
