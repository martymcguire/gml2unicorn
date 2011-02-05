gml2unicorn.py
==============

Convert [Graffiti Markup Language](http://www.graffitimarkuplanguage.com/) (GML)
files into G-Code files for the [MakerBot Unicorn](http://store.makerbot.com/makerbot-unicorn-pen-plotter-kit.html)
pen plotter!

Pre-Requisites
--------------

You'll need to install Python and some support libraries:

* [Python](http://python.org/)
* [PyGML](https://bitbucket.org/keegan3d/pygml)

Usage
-----

* Edit the configuration section of `gml2unicorn.py` to match your Unicorn
plotting preferences.
* Acquire a GML file. [000000book](http://000000book.com/) is great for this.
* `python gml2unicorn.py my_graffiti.gml > my_graffiti.gcode`
* Load `my_graffiti.gcode` in ReplicatorG
* Build!
