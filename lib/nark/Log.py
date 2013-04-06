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

from log.IWriter import LOG_CONSTS
import nark

class Log():
  """ Log writer """
  
  __writer = None
  """ The IWriter attached to this object for log output. """
  
  def setLogWriter(self, writer):
    """ Set an object conforming to the IWriter interface as an output. """
    self.__writer = writer
    
  def trace(self, msg):
    """ Print a debug message to the log file """
    self.__writer.trace(LOG_CONSTS.INFO, msg)

  def warn(self, msg):
    """ Print a warning message to the log file """
    self.__writer.trace(LOG_CONSTS.WARN, msg)
    
  def error(self, msg, exception):
    """ Log an exception to the log file """
    self.__writer.trace(LOG_CONSTS.ERROR, msg)
    self.__writer.traceback(exception)
    
  @staticmethod
  def get():
    """ Shortcut to get the log interface if it is already bound """
    return nark.Register.get().instance(Log);
