#!/usr/bin/python
# -*- coding: utf-8 -*-
#

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("data/caja.desktop.in*", "Exec=caja", "Exec=caja -n --sync")
    autotools.configure("--disable-static \
                         --disable-schemas-compile \
                         --with-gnu-ld \
                         --with-gtk=3.0 \
                         --disable-update-mimedb")
    
    # for fix unused dependency
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README", "TODO")