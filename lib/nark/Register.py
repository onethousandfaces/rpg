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

class Register(object):
  """ Singleton register helper
      
      Any class type can be registered here, but only a single instance 
      per class type is supported. You would typically use this like:
      
      nark.Register.get().bind(my_instance)
      instance = nark.Register.get().instance(MyType)
      
      Note that register is not a factory, and does not support binding
      types to interfaces / creating multiple instances by sub-type.
  """
  
  __instances = {}
  """ Set of bound instances """
  
  __instance = None
  """ Global instance """
  
  @staticmethod
  def get():
    """ Return the global register instance """
    if Register.__instance is None:
      Register.__instance = Register()
    return Register.__instance
  
  def bind(self, item):
    """ Bind an instance to the register by type """
    name = item.__class__.__name__
    self.__instances[name] = item
  
  def instance(self, class_type):
    """ Fetch an instance or return None """
    rtn = None
    name = class_type.__name__
    if self.__instances.has_key(name):
      rtn = self.__instances[name]
    return rtn
