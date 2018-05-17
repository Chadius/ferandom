# Import the gi or pgi library
try:
    import gi
    gi.require_version("Gtk", "3.0")
except ImportError:
    import pgi
    pgi.require_version("Gtk", "3.0")
from pgi.repository import Gtk

window = Gtk.Window(title="Hello World")
window.show()
window.connect("destroy", Gtk.main_quit)
Gtk.main()
