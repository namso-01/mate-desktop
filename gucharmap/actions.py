#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools, get, shelltools

def setup():
    shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc \
                         --localstatedir=/var \
                         --disable-static \
                         --disable-schemas-compile \
                         --enable-introspection \
                         --with-unicode-data=/usr/share/unicode")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("TODO", "README", "NEWS", "ChangeLog", "AUTHORS")
