#!/usr/bin/env python
#
# __hg_ps1 - Shell prompt helper for Mercurial (cf. __git_ps1)
#
# Copyright 2009 Kevin R. Bullock <kbullock@ringworld.org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301,
# USA.

import os

# Nabbed from mercurial/dispatch.py
def _findrepo(p):
    while not os.path.isdir(os.path.join(p, ".hg")):
        oldp, p = p, os.path.dirname(p)
        if p == oldp:
            return None

    return p


def main():
    import sys
    from mercurial import ui, hg, error

    u = ui.ui()  # get a ui object
    path = _findrepo(os.getcwd()) or ""
    try:
      # get a repository object for the current dir
      r = hg.repository(u, path)
    except error.RepoError:
      # exit if we're not in a repository
      sys.exit(1)

    # repository.status(rev1, rev2, match, ignored, clean, unknown)
    # (last three params are flags whether to include files of the given status)
    # returns a tuple of lists of files:
    # (modified, added, removed, deleted, unknown, ignored, clean)
    stat = r.status('.', None, None, False, False, True)

    sys.stdout.write(r.dirstate.branch())
    if True in [bool(l) for l in stat[0:4]]:
      print "!",
    elif stat[4]:
      print "?",

if __name__ == '__main__':
    main()
