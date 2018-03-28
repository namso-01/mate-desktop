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
    autotools.configure(" --enable-locking \
                          --with-xf86gamma-ext \
                          --with-kbd-layout-indicator \
                          --with-systemd=no \
                          --prefix=/usr \
                          --enable-compile-warnings=yes \
                          --enable-maintainer-mode \
                          --enable-docbook-docs \
                          --sysconfdir=/etc \
                          --with-shadow \
                          --with-xscreensaverdir=/usr/share/xscreensaver/config \
                          --with-xscreensaverhackdir=/usr/lib/misc/xscreensaver")
    
    
    # for fix unused dependency
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    pisitools.ldflags.add("-lmate-menu")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "NEWS", "ChangeLog", "AUTHORS", "COPYING")
