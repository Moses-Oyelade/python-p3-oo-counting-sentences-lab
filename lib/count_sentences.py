#!/usr/bin/env python3

class MyString:
    def __init__(self, value = "mystring"):
        self.value = value
    
    
    def get_value(self):
      return self.value
    def set_value(self):
      if type(self.value) in (str, float) or self.value == " ":
        print("The value must be a string.")
      else:
        return self.value
    
    def is_sentence(self):
        return self.value.endswith(".")
    def is_question(self):
        return self.value.endswith("?")
    def is_exclamation(self):
        return self.value.endswith("!")
    def count_sentences(self):
      count = 0
      for letter in self.value:
        if letter == "." or letter == "?" or letter == "!": count += 1
      return count
              





personal = MyString()
personal.value = "this is the town."
print(personal.is_sentence())

simple_string = MyString("one. teo. three?")
empty_string = MyString()
complex_string = MyString("This is a string! It has three sentences. Right?")

print(simple_string.count_sentences())