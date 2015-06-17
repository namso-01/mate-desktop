#!    pisitools.remove("bin/python
# -*- coding: utf-8 -*-
#

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    #Change default xcursor
    pisitools.dosed("schemas/org.mate.peripherals-mouse.gschema.xml.in.in", "<default>''</default>", "<default>'mate'</default>")
    #Change default desktop image
    pisitools.dosed("schemas/org.mate.background.gschema.xml.in.in", "backgrounds/mate/desktop/Stripes.png", "backgrounds/mate/nature/pisi.jpg")
    autotools.configure("--prefix=/usr \
                         --with-gtk=3.0 \
                         --disable-static \
                         --disable-schemas-compile \
                         --enable-gtk-doc")

def build():
    autotools.make()
    
def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README")