import pyglet
import cocos
from pywidget.dialog import Dialog
from pywidget.button import Button
from pywidget.textbox import Textbox
from pywidget.vbox import VBox

class Ui(cocos.cocosnode.CocosNode):
  """ User interface for this layer """

  button1 = Button(text='Hello World')

  def on_enter(self):
    text = Textbox(text="Hi")
    #self.on_button_press = button.event(self.on_button_press)
    vbox = VBox(elements=[self.button1, text])
    self.dialog = Dialog(title='My Dialog', x=100, y=100, content=vbox, width=200, height=100)
    cocos.director.director.window.push_handlers(self.dialog)

  @button1.event
  def on_button_press(button):
     print('Button pressed: %s' % button)

  def on_exit(self):
    cocos.director.director.window.remove_handlers(self.dialog)

  def draw(self):
    self.dialog.on_draw()


class Content(cocos.layer.Layer):
  """ Sprites and complicated stuff for this layer """

  # Mark this class as receiving events
  is_event_handler = True

  # The current text entered
  input = ""

  # The text we're currently displaying
  output = ""

  # Widgets~
  widgets = {}

  def __init__(self):
    super( Content, self ).__init__()
    self.widgets['input'] = cocos.text.Label("", x=10, y=30)
    self.widgets['output'] = cocos.text.Label("", x=10, y=300)
    self.add(self.widgets['input'])
    self.add(self.widgets['output'])
    self.keys_pressed = set()
    self.update_text()

  def update_text(self):
    key_names = [pyglet.window.key.symbol_string (k) for k in self.keys_pressed]
    if len(key_names) > 0:
      self.input = self.input + str(key_names[0])
      self.widgets['input'].element.text = self.input

  def on_key_press (self, key, modifiers):
    self.keys_pressed.add(key)
    self.update_text()

  def on_key_release(self, key, modifiers):
    self.keys_pressed.remove(key)
    self.update_text()

class Test:
  """ Factory for easy access to instances of the view types """
  @classmethod
  def layers(self):
    return [ Ui(), Content() ]
