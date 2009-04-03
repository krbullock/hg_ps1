-*- markdown -*-

About `__hg_ps1`
==============

`__hg_ps1` is a shell prompt helper for Mercurial repositories, similar to
`__git_ps1`. It is intended to be called from your custom prompt string (PS1 in
bash and related shells). If your working directory is in a repository, it
prints the current branch name, and appends either a '!' if there are modified
files in the working directory, a '?' if there are untracked files, or nothing
if the repository is clean.

For example:

    ~/repo$ hg st
    A .hgignore
    ~/repo$ PS1='$(__hg_ps1)\n'$PS1
    on default!                       # PS1 calls __hg_ps1
    ~/repo$ 

`__hg_ps1` is a pure Python implementation. Shell-based solutions like [the one
Steve Losh published][1] start multiple Python interpreters every time the
prompt is printed; this implementation only needs to run *one* interpreter.

[1]: http://stevelosh.com/blog/entry/2009/3/17/mercurial-bash-prompts/


Installation
============

To install, copy `__hg_ps1` to somewhere in your `PATH` (e.g.
`/usr/local/bin/`). You may need to change the shebang line (the first line of
the executable) to point to the same version of Python that Mercurial uses. By
default, the shebang line reads:

    #!/usr/bin/env python

On Mac OS X Leopard, to use `__hg_ps1` with the version of Mercurial from
<http://mercurial.berkwood.com/>, the shebang line should read as follows:

    #!/System/Library/Frameworks/Python.framework/Versions/2.5/Resources/Python.app/Contents/MacOS/Python

This shouldn't be a concern unless you have multiple Python interpreters
installed.

Setting your prompt
-------------------

You can then add it into your prompt string. In bash, for example, you might set
the following in ~/.bashrc:

    # ~/.bashrc
    PS1='$(__hg_ps1)\n'$PS1

If you already have a custom prompt string, add the above line *after* it--don't
replace it. For example:

    # ~/.bashrc
    PS1='\u@\h \w\$ '
    PS1='$(__hg_ps1)\n'$PS1
