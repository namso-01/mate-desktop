#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    autotools.configure("--enable-maintainer-mode")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.install()

    #pisitools.removeDir("/usr/share/gtkmm-2.4")
    #pisitools.removeDir("/usr/share/devhelp")

    pisitools.dodoc("ChangeLog","COPYING", "PORTING", "NEWS", "README")
