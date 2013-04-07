# Copyright 2012 Douglas Linder
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import src.bootstrap
import pyglet
import cocos
from pywidget.dialog import Dialog
from pywidget.button import Button
from pywidget.textbox import Textbox
from pywidget.vbox import VBox

# Stupid sprite test
class Hello(cocos.layer.Layer):

  def __init__(self):
    super( Hello, self ).__init__()

    sprite = cocos.sprite.Sprite("assets/cat.jpg")
    sprite.position = 150, 150
    self.add(sprite)

    # Load image, convert to sequence of images for animation, create sprite animation.
    raw = pyglet.image.load('assets/cat.jpg')
    raw_seq = pyglet.image.ImageGrid(raw, 5, 5)
    anim = pyglet.image.Animation.from_image_sequence(raw_seq, 0.05, True)
    sprite2 = cocos.sprite.Sprite(anim)
    sprite2.position = 300, 300
    self.add(sprite2)

# Stupid ui test
class Ui(cocos.cocosnode.CocosNode):

  button1 = Button(text='Hello World')
  text = Textbox(text="Hi")
  vbox = VBox(elements=[button1, text])
  dialog = Dialog(title='My Dialog', x=100, y=100, content=vbox, width=200, height=100)

  def on_enter(self):
    cocos.director.director.window.push_handlers(self.dialog)

  def on_exit(self):
    cocos.director.director.window.remove_handlers(self.dialog)

  def draw(self):
    self.dialog.on_draw()

  @button1.event
  def on_button_press(button):
     print('Button pressed: %s' % button)

# Start scene
if __name__ == "__main__":
  cocos.director.director.init()
  hello_layer = Hello ()
  ui_layer = Ui()
  main_scene = cocos.scene.Scene (hello_layer, ui_layer)
  cocos.director.director.run (main_scene)
