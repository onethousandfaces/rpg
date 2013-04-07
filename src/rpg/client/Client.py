import rpg.ui
import cocos
    
class Client:
  def run(self):
    cocos.director.director.init()
    main_scene = cocos.scene.Scene(*rpg.ui.Test.layers())
    cocos.director.director.run (main_scene)
