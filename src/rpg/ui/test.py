import pyglet
import cocos

class Test(cocos.layer.Layer):

  # Mark this class as receiving events
  is_event_handler = True

  # The current text entered
  input = ""

  # The text we're currently displaying
  output = ""

  # Widgets~
  widgets = {}

  def __init__(self):
    super( Test, self ).__init__()
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
