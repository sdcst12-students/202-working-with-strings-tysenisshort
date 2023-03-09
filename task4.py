#!python3

"""
Strings are iterable.  Use for loops to iterate through both strings to create a list to represent a deck of cards. Note: We can also use list comprehension as strings are still iterable!
"""

cards = "A23456789TJQK"
suits = "CDHS"

def createDeck():
  
  card=[f"{i}{j}" for i in ranks for j in suits]
  
  
  
  
  return card

def main():
  deckcards = createDeck()
  print(deckcards)
  assert "AS" in deckcards
  assert "KC" in deckcards
  assert deckcards.count("TC") == 1


if __name__ == "__main__":
  main()