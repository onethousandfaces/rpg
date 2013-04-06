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

import nark

class Resolver(object):
  """ IOC helper class """
  
  @staticmethod
  def __container():
    """ Return the container instance """
    container = nark.Register.get().instance(nark.ioc.Container)
    if container is None:
      container = nark.ioc.Container()
      nark.Register.get().bind(container)
    return container

  @staticmethod
  def register(module):
    """ 
      Applies binding to the container 
      @param module A class with a 'register' function matching.

      A module can apply a series of bindings on a container
      passed to it. A typical module might look like:

      class MyModule:
        def register(c):
          c.register(myInterface, myBinding)
          c.register(interface2, bind2)

      Pass the class type in, not an instance. 
      ie. Resolver.register(MyModule)
    """
    instance = module()
    instance.register(Resolver.__container())

  @staticmethod
  def arg(interface, arg):
    """ Invoke this in an object constructor in inject objects """
    rtn = arg
    if rtn is None:
      rtn = Resolver.__container().resolve(interface)
    return rtn
