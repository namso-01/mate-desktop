#!/usr/bin/python
# -*- coding: utf-8 -*-
#

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    #pisitools.dosed("data/org.mate.peripherals-touchpad.gschema.xml.in.in", "<default>false</default>", "<default>true</default>")
    autotools.configure("--enable-polkit \
                         --disable-static")
    
    # for fix unused dependency
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")
                       
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "COPYING", "NEWS", "ChangeLog", "AUTHORS")
