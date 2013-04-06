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

def trace(msg):
  """ Simple CLI helper method """
  l = nark.Log.get()
  if l is None:
    from nark.log import CliWriter
    cli = CliWriter()
    l = nark.Log()
    l.setLogWriter(cli)
    nark.Register.get().bind(l)
  l.trace(msg)
