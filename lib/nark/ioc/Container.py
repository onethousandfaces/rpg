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

class Container():
  """ Container is a helper for binding interfaces to implementations. 

      Use it like this:

        c = Container()
        c.register(InterfaceType, InstanceType)
        
        single = c.singelton()
        instance = c.instance()
        
      Container does not keep track of the objects it creates. 

      Only a single type can be bound against a single interface.
  """
      
  __binding = {}
  """ Set of bindings of interface -> impl """
  
  def register(self, interface_type, class_type):
    """ Bind an instance to the register by type 

        Pass in classes, not class instances for interface
        and class types.

        class_type must be a subclass of interface_type.
    """
    if issubclass(class_type, interface_type):
      key = interface_type.__name__
      binding = Binding(interface_type, class_type)
      self.__binding[key] = binding
    else:
      raise Exception("Invalid registration: " + class_type.__name__ + " does not implement " + interface_type.__name__)
  
  def resolve(self, interface_type, singleton = True):
    """ Return an instance of the implementing class """
    rtn = None
    name = interface_type.__name__
    if self.__binding.has_key(name):
      binding = self.__binding[name]
      if singleton:
        if binding.instance is None:
          binding.instance = binding.class_type()
        rtn = binding.instance
      else:
        rtn = binding.class_type()
    else:
      raise Exception("Invalid request: " + interface_type.__name__ + " is not registered")
    return rtn

class Binding():
  """ Binding for a single type

      Don't really need a class for this, but makes it handy if
      it ever has to implement instance tracking.
  """
  
  def __init__(self, interface_type, class_type):
    self.interface_type = interface_type;
    self.class_type = class_type
    self.instance = None
