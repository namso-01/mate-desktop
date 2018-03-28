#!/usr/bin/python
# -*- coding: utf-8 -*-
#

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc \
                         --localstatedir=/var \
                         --disable-static \
                         --enable-caja \
                         --enable-pdf \
                         --enable-tiff \
                         --enable-djvu \
                         --enable-dvi \
                         --enable-xps --enable-introspection \
                         --enable-t1lib --enable-gtk-doc \
                         --enable-comics \
                         --enable-pixbuf ")
    
    # for fix unused dependency
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "NEWS", "AUTHORS", "COPYING")
