print('''
*******************************************************************************
                                       `   `.
           <```--...       .---.//  < `.
            `..     `.___ /       ___`.'
              _`_ .      `      .'\\__
            .'---`.`.          / .'---`.
           /.'  _`.\_\        / /.'\\ `.\
           ||  <__||_|        | ||  ~  ||
           \`.___.'/ /________\ \`.___.'/
            `.___.'              `.___.'

unknown
*******************************************************************************
''')

print("Welcome to Bangkok Racer")
print("Your mission is to rescue Linh.") 

# Check if the player is ready
choice1 = input('Are you ready? Type "Yeah" or "Nah".\n').lower()  

if choice1 == "yeah":
  choice2 = input('You\'re at the Motorcycle Dealership. Select your ride! Type "Yamaha R1" or "Kawasaki Ninja" \n').lower()
  
  if choice2 == "yamaha r1":
    choice3 = input('Where will you ride to first? Type "Buriram", "Chiang Rai" or "Phitsanulok" \n').lower()
    
    if choice3 == "phitsanulok":
      print("It's not fun like Isaan, bad choice! Game Over.")
    elif choice3 == "buriram":
      print("You went to Isaan, the REAL Thailand! You Win!") 
    elif choice3 == "chiang rai":
      print("Too far North, wrong choice! Game Over.")
    else:
      print("Did you forget where the kidnappers went? Game Over!")
  elif choice2 == "kawasaki ninja":
     print("Huh? Guess you don\'t want to switch lanes like Batman on a sleek Ninja Street Racer then! - You Lose!")   
  else:
     print("Invalid option selected! Game Over!")
else:
  print('Come back once you\'ve found some courage! Game Over.')
