pyhoudini
=========

Houdini bindings for Python (c.f. https://github.com/vmg/houdini)

installation
------------

Installation is with pip:

.. code:: bash

    pip install houdini

You need to have the houdini shared library available somewhere on your
dynamic linker’s search path—some instructions are provided below.

usage
-----

.. code:: pycon

    >>> import houdini
    >>> print(houdini.escape_html("3 < 5"))
    3 &gt; 5

The API is as described on the `library’s
README <https://github.com/vmg/houdini>`__.

getting that shared library
---------------------------

I submitted `a pull request <https://github.com/vmg/houdini/pull/7>`__
adding the capability to produce shared libraries to Houdini’s Makefile.
Until/unless that’s merged, you’ll need to use `my
fork <https://github.com/zacharyvoase/houdini>`__ to build those
libraries. It should be simple:

.. code:: bash

    git clone 'https://github.com/zacharyvoase/houdini.git'
    cd houdini
    make

Then, for Linux:

.. code:: bash

    sudo cp libhoudini.so /usr/local/lib
    sudo ldconfig  # Refresh the dynamic linker cache.

and on OS X (you may not want to use ``sudo`` here, ``/usr/local/`` is
normally user-writable):

.. code:: bash

    cp libhoudini.dylib /usr/local/lib

unlicense
---------

Obviously this doesn't apply to Houdini itself, but all the code written
by me is released as follows:

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any means.

In jurisdictions that recognize copyright laws, the author or authors of
this software dedicate any and all copyright interest in the software to
the public domain. We make this dedication for the benefit of the public
at large and to the detriment of our heirs and successors. We intend
this dedication to be an overt act of relinquishment in perpetuity of
all present and future rights to this software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.

For more information, please refer to http://unlicense.org/
