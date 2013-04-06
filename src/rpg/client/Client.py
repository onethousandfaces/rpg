import cocos
import rpg.ui

class Client:
  def run(self):
    cocos.director.director.init()
    ui = rpg.ui.Test()
    main_scene = cocos.scene.Scene (ui)
    cocos.director.director.run (main_scene)
