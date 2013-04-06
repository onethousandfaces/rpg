import cocos
import rpg.ui

import pyglet
from pywidget.dialog import Dialog
from pywidget.button import Button
from pywidget.vbox import VBox
from pywidget.hbox import HBox
from pywidget.slider import Slider
from pywidget.checkbox import Checkbox
from pywidget.label import Label
from pywidget.radiobutton import Radiobutton

label1 = Label(text='<font face="Helvetica,Arial" size="2" color=white>First Label</font>',
                    x=50, y=50)
label2 = Label(text='<font face="Helvetica,Arial" size="2" color=white>second Label</font>',
                    x=50, y=50)
label3 = Label(text='<font face="Helvetica,Arial" size="2" color=white>third Label</font>',
                    x=50, y=50)
rbutton = Radiobutton(x=50, y=50, height=90, width=100, elements=[label1, label2, label3])

button1 = Button(text='<font face="Helvetica,Arial" size="2" color="white">Click me 1</font>')
button2 = Button(text='<font face="Helvetica,Arial" size="2" color=white>Click me 2</font>')
button3 = Button(text='<font face="Helvetica,Arial" size="2" color=white>Click me 3</font>')
button4 = Button(text='<font face="Helvetica,Arial" size="2" color=white>Click me 4</font>')
checkbox = Checkbox()
label = Label(text='<font face="Helvetica,Arial" size="2" color=white>Some text</font>')
slider = Slider(x=50, y=50)

vbox = VBox(elements=[
            slider,
            HBox(elements=[button2, button3]),
            button1,
            rbutton,
            HBox(elements=[checkbox, label, button4])])

dialog = Dialog(title='My Dialog', x=100, y=100, content=vbox, width=300, height=160)

@rbutton.event
def on_Radiobutton_press(radiobutton):
    print 'change'

@slider.event
def on_value_change(slider):
    print 'Value change : ', round(slider.value, 2)
    
@button1.event
def on_button_press(button):
    print 'Button 1'

@button2.event
def on_button_press(button):
    print 'Button 2'
    
@button3.event
def on_button_press(button):
    print 'Button 3'
    
@button4.event
def on_button_press(button):
    print 'Button 4'
    
@checkbox.event
def on_value_change(checkbox):
    print 'Checkbox : ', checkbox.checked
    
class Client:
  def run(self):

    cocos.director.director.init()
    cocos.director.director.gui = dialog
    cocos.director.director.window.push_handlers(dialog)

    ui = rpg.ui.Test()
    main_scene = cocos.scene.Scene (ui)
    cocos.director.director.run (main_scene)
