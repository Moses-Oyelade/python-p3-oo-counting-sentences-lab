#!/usr/bin/env python3

class MyString:
    def __init__(self, value = "mystring"):
        self.value = value
    
    
    def set_value(self, value):
      if isinstance(value, str):
        self._value = value
      else:
        print('The value must be a string.')

    def get_value(self):
      return self._value

    value = property(get_value, set_value)
    
    def is_sentence(self):
        return self.value.endswith(".")
    def is_question(self):
        return self.value.endswith("?")
    def is_exclamation(self):
        return self.value.endswith("!")
    def count_sentences(self):
      count = 0
      for word in self.value.split():
        if word.endswith(".") or word.endswith("?") or word.endswith("!"): 
          count += 1
      return count
              





personal = MyString()
personal.value = "this is the town."
print(personal.is_sentence())

simple_string = MyString("one. teo. three?")
empty_string = MyString()
complex_string = MyString("This is a string! It has three sentences. Right?")

print(simple_string.count_sentences())