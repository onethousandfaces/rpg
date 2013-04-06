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

from IWriter import IWriter, LOG_CONSTS
import sys
import traceback

class CliWriter(IWriter):
  """ Stdout writer """
  
  def trace(self, level, msg):
    """ Invoked to record a message """
    if level == LOG_CONSTS.INFO:
      print(msg)
    elif level == LOG_CONSTS.WARN:
      print("! Warning: " + msg)
    elif level == LOG_CONSTS.ERROR:
      print("!!! ERRROR: " + msg)
      
  def traceback(self, exception):
    """ Print a traceback for an exception. """
    self.trace(LOG_CONSTS.ERROR, str(exception))
    traceback.print_stack(file=sys.stdout)