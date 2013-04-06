import pyglet.window.key

class TextInput:
""" Read in coming text and handle it as a string """

  _text = ""
  """ The currently held text """

  _submit = False
  """ Have we received a submit event """

  _cancel = False
  """ Have we received a cancel event """

  def bind(self, start_code, cancel_code, submit_code):
  """ Set the key binding for cancel and submit """
    self._scode = submit_code
    self._ccode = cancel_code

  def in(self, code):
    if code == self.cancel:
      self.text = ""
    if code == self.submit

  def submit(self):
  """ Return true if the submit code was received """
    return self._scode
  
  def out(self):
    return text
