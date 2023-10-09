#!/usr/bin/env python3

class MyString:
    def __init__(self):
        self._is_sentence = ""
    
    
    def is_sentence(self, value):
        self._is_sentence == value
        return value.endswith(".")
    def is_question(self, value):
        return value.endswith("?")
    def is_exclamation(self, value):
        return value.endswith("!")
    def count_sentences(self, value):
      count = 0
      for letter in value:
        if letter == "." or letter == "?" or letter == "!": count += 1
      return count
              





personal = MyString()
print(personal.is_sentence("this is the town."))
print(personal.count_sentences("This is a string! It has three sentences. Right?"))