#! /usr/bin/env python
"""
Sample script that monitors smartcard readers.

__author__ = "http://www.gemalto.com"

Copyright 2001-2008 gemalto
Author: Jean-Daniel Aussel, mailto:jean-daniel.aussel@gemalto.com

This file is part of pyscard.

pyscard is free software; you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation; either version 2.1 of the License, or
(at your option) any later version.

pyscard is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with pyscard; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""

from sys import stdin, exc_info
from time import sleep

from smartcard.ReaderMonitoring import ReaderMonitor, ReaderObserver

# a simple reader observer that prints added/removed readers
class printobserver( ReaderObserver ):
    """A simple reader observer that is notified
    when readers are added/removed from the system and
    prints the list of readers
    """
    def update( self, observable, (addedreaders, removedreaders) ):
        print "Added readers", addedreaders
        print "Removed readers", removedreaders

try:
    print "Add or remove a smartcard reader to the system."
    print "This program will exit in 10 seconds"
    print ""
    readermonitor = ReaderMonitor()
    readerobserver = printobserver()
    readermonitor.addObserver( readerobserver )

    sleep(10)

    # don't forget to remove observer, or the
    # monitor will poll forever...
    readermonitor.deleteObserver(readerobserver)

    import sys
    if 'win32'==sys.platform:
        print 'press Enter to continue'
        sys.stdin.read(1)

except:
    print exc_info()[0], ':', exc_info()[1]



