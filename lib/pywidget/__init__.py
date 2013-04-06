#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Copyright (c) 2009 Nicolas Rougier, Matthieu Kluj, Jessy Cyganczuk
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions 
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright 
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# -----------------------------------------------------------------------------
'''Defines a set of basic 2D widgets.

All widgets have:
----------------

- a position in 2D space
- a dimension in 2D space
- a x alignment ('left', 'center' or 'right')
- a y alignment ('top', 'center' or 'bottom')

Available widgets:
-----------------

- Button (a simple button)
- Checkbox (a simple checkbox)
- Dialog (a dialog with a title, a close button and a content which has to be a children of Widget)
- HBox (used to split content into horizontal parts)
- Label (a simple label)
- Slider (a simple slider)
- VBox (used to split content into vertical parts)

Example usage:
--------------
 
   window = pyglet.window.Window(resizable=True)
   button = Button(text='<font face="Helvetica,Arial" size="2" color=white>Click me</font>',
                   x=50, y=50)
   window.push_handlers(button)

   @window.event
   def on_draw():
       window.clear()
       button.on_draw()

   @button.event
   def on_button_press(button):
       print 'Click'

   pyglet.app.run()

:requires: pyglet 1.1
'''
__docformat__ = 'restructuredtext'
__version__ = '1.0'

from button import Button
from checkbox import Checkbox
from dialog import Dialog
from hbox import HBox
from label import Label
from slider import Slider
from vbox import VBox
from radiobutton import Radiobutton

