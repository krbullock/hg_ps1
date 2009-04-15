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

To install, run the setup script:

    python setup.py install

This will install the source as an egg in your Python site-packages directory,
and put `__hg_ps1` into (most likely) `/usr/local/bin`. (Run `python setup.py
install --help` for more options.)

Be sure to run `setup.py` with the same version of Python that Mercurial uses.
On Mac OS X Leopard, to use `__hg_ps1` with the version of Mercurial from
<http://mercurial.berkwood.com/>, use `/usr/bin/python`, as follows:

    $ /usr/bin/python setup.py [command]

This shouldn't be a concern unless you have multiple Python interpreters
installed (e.g. through Fink or MacPorts).

Thanks to Jannis Leidel &lt;<jannis@leidel.info>&gt; for creating the setup
script and reworking the code into module form.

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


Local branches
==============

zerok has created a fork of `__hg_ps1` that provides support for local branches.
His repository is here: <http://bitbucket.org/zerok/hg_ps1-lbranch/>.
