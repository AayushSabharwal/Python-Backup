import random as rd

words = ['bagpipes', 'awkward', 'resolve', 'absolute', 'confidential', 'inaccurate', 'resolute', 'frivolous']
nwords = len(words)

while True:
  word = words[rd.randrange(0, nwords)]
  lives = len(word) + 2
  guessedWord = '_'*len(word)
  triedLetters = []
  while not(guessedWord == word) and lives > 0:
    print(guessedWord + "\t\t\t lives = " + str(lives))

    guess = str(input("Enter Letter: "))
    if not guess.isalpha():
      print("Enter a letter!")
      continue
    elif guess in triedLetters:
      print("You've tried this! Try again")
      continue
    
    triedLetters.append(guess)
    if guess not in word:
      print("Wrong guess!")
      lives = lives - 1
      continue
    
    guessedWord = word
    for letter in guessedWord:
      if letter not in triedLetters:
        guessedWord = guessedWord.replace(letter, '_')
    
  if word == guessedWord:
    print("You win!")
  else:
    print("You lose!")
  print("Continue? (y/n)")
  if not str(input()).lower() == 'y':
    break
