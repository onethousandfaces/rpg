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

from abc import ABCMeta, abstractmethod
import nark

LOG_CONSTS = nark.enum("INFO", "WARN", "ERROR")
""" Constants for the logging service """

class IWriter(object):
  """ Generic writer type for logs """
  
  __metaclass__ = ABCMeta
  
  @abstractmethod
  def trace(self, level, msg):
    """ Invoked to record a message """
    return
      
  @abstractmethod
  def traceback(self, exception):
    """ Print a traceback for an exception. """
    return
