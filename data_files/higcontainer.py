import gtk
import gobject
try:
    from gazpacho.widgets.base.base import SimpleContainerAdaptor
except ImportError:
    pass




class HIGContainer(gtk.Bin):
    __gtype_name__ = 'HIGContainer'
    __gproperties__ = {
        'title': (str, 'Group Title', 'the group title',
                  '', gobject.PARAM_READWRITE|gobject.PARAM_CONSTRUCT),
    }

    def __init__(self, title=None):
        self.__title_text = None
        gtk.widget_push_composite_child()
        self.__title = gobject.new(gtk.Label, visible=True, xalign=0, yalign=0.5)
        self.__indent = gobject.new(gtk.Label, visible=True, label='    ')
        gtk.widget_pop_composite_child()
        gtk.Bin.__init__(self)
        self.__title.set_parent(self)
        self.__indent.set_parent(self)
        if title is not None:
            self.props.title = title

    def do_size_request(self, requisition):
        title_req = gtk.gdk.Rectangle(0, 0, *self.__title.size_request())
        indent_req = gtk.gdk.Rectangle(0, 0, *self.__indent.size_request())
        if self.child is None:
            child_req = gtk.gdk.Rectangle()
        else:
            child_req = gtk.gdk.Rectangle(0, 0, *self.child.size_request())
        requisition.height = (title_req.height + 6 +
                              max(child_req.height, indent_req.height))
        requisition.width = max(title_req.width, indent_req.width + child_req.width)

    def do_size_allocate(self, allocation):
	self.allocation = allocation

        
        title_req = gtk.gdk.Rectangle(0, 0, *self.__title.get_child_requisition())
        title_alloc = gtk.gdk.Rectangle()
        title_alloc.x = allocation.x
        title_alloc.y = allocation.y
        title_alloc.width = min(title_req.width, allocation.width)
        title_alloc.height = min(title_req.height, allocation.height)
        self.__title.size_allocate(title_alloc)

        
        if self.child is None:
            return
        indent_req = gtk.gdk.Rectangle(0, 0, *self.__indent.get_child_requisition())
        child_req = gtk.gdk.Rectangle(0, 0, *self.child.get_child_requisition())
        child_alloc = gtk.gdk.Rectangle()
        child_alloc.x = allocation.x + indent_req.width
        child_alloc.y = allocation.y + title_alloc.height + 6
        child_alloc.width = allocation.width - indent_req.width
        child_alloc.height = allocation.height - 6 - title_alloc.height
        self.child.size_allocate(child_alloc)

    def do_forall(self, internal, callback, data):
        if internal:
            callback(self.__title, data)
            callback(self.__indent, data)
        if self.child is not None:
            callback(self.child, data)

    def do_set_property(self, pspec, value):
        if pspec.name == 'title':
            self.__title.set_markup('<span weight="bold">%s</span>' %
                                    gobject.markup_escape_text(value))
            self.__title_text = value
        else:
            raise AttributeError, 'unknown property %s' % pspec.name

    def do_get_property(self, pspec):
        if pspec.name == 'title':
            return self.__title_text
        else:
            raise AttributeError, 'unknown property %s' % pspec.name

if __name__ == '__main__':
    frame = gtk.Frame()
    group = gobject.new(HIGContainer, title="Hello")
    frame.add(group)
    check = gtk.CheckButton("foobar")
    group.add(check)
    w = gtk.Window()
    w.add(frame)
    w.show_all()
    w.connect("destroy", lambda w: gtk.main_quit())
    gtk.main()
    
