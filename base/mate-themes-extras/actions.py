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
    shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    autotools.configure("--prefix=/usr \
                         --enable-Blue-Submarine \
                         --enable-clearlooks-phenix \
                         --enable-DeLorean-Dark \
                         --enable-Faience \
                         --enable-DeLorean \
                         --enable-Faience-Ocre \
                         --enable-Gnome-Cupertino \
                         --enable-Gnome-Cupertino-Mint \
                         --enable-GnomishBeige \
                         --enable-Green-Submarine \
                         --enable-Smoothly \
                         --enable-Smoothly-Black \
                         --enable-Zukitwo \
                         --enable-Zukitwo-Brave \
                         --enable-Zukitwo-Dust \
                         --enable-Zukitwo-Human \
                         --enable-Zukitwo-Illustrious \
                         --enable-Zukitwo-Noble \
                         --enable-Zukitwo-Wine \
                         --enable-Zukitwo-Wise \
                         --enable-Zukitwo-Colors")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "COPYING", "NEWS", "ChangeLog", "AUTHORS")