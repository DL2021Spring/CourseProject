





















import ns.core

class MyModel(object):

    def Start(self):
        ns.core.Simulator.Schedule(ns.core.Seconds(10.0), self.HandleEvent, ns.core.Simulator.Now().GetSeconds())

    def HandleEvent(self, value):
        print "Member method received event at", ns.core.Simulator.Now().GetSeconds(), \
            "s started at", value, "s"

def ExampleFunction(model):
    print "ExampleFunction received event at", ns.core.Simulator.Now().GetSeconds(), "s"
    model.Start()

def RandomFunction(model):
    print "RandomFunction received event at", ns.core.Simulator.Now().GetSeconds(), "s"

def CancelledEvent():
    print "I should never be called... "

def main(dummy_argv):

    model = MyModel()
    v = ns.core.UniformVariable(10,20)

    ns.core.Simulator.Schedule(ns.core.Seconds(10.0), ExampleFunction, model)

    ns.core.Simulator.Schedule(ns.core.Seconds(v.GetValue()), RandomFunction, model)

    id = ns.core.Simulator.Schedule(ns.core.Seconds(30.0), CancelledEvent)
    ns.core.Simulator.Cancel(id)

    ns.core.Simulator.Run()

    ns.core.Simulator.Destroy()

if __name__ == '__main__':
    import sys
    main(sys.argv)
