print("""
*******************************************************************************
                          WELCOME TO TREASURE ISLAND
*******************************************************************************
Your mission is to find the treasure and escape the island alive!
""")

print("""
    ^  ^  ^
   /|\\ | /|\\
    | /   \ |
   _|_     _|_
   
    ISLAND
""")

# Start of the game
print("You wake up on a mysterious island. You need to find the treasure!")
print()

# First choice
choice1 = input("You see a path splitting into two directions. Do you go LEFT or RIGHT? ").lower()

if choice1 == "left":
    print("""
    
         <---
        / - \\
       /  -  \\
      / FOREST\\
     -----------
    
    """)
    print("You walk left and encounter a dark forest with strange sounds...")
    print()
    
    choice2 = input("You find an old cabin. Do you ENTER or IGNORE it? ").lower()
    
    if choice2 == "enter":
        print("""
        
         ___
        /   \\
       / === \\
      |_CABIN_|
       |  |  |
      _|__|__|_
       
        """)
        print("Inside the cabin, you find a map! You also find a key on the floor.")
        print()
        
        choice3 = input("The map shows two paths. Do you follow the MOUNTAIN route or the CAVE route? ").lower()
        
        if choice3 == "mountain":
            print("""
            
               /\\
              /  \\
             /    \\
            /      \\
           /________\\
           MOUNTAIN
           
            """)
            print("You climb the mountain. At the top, you discover a treasure chest!")
            print("You found the treasure! 🎉")
            print("""
            
             +----------+
             |   GOLD   |
             |   $$$$   |
             | $$    $$ |
             | $  XX  $ |
             | $$    $$ |
             |   $$$$   |
             +----------+
             TREASURE FOUND!
             
            """)
            print("Congratulations! You've escaped the island with the treasure and won the game!")
        elif choice3 == "cave":
            print("""
            
             (  CAVE  )
            (           )
           (  ~DANGER~  )
            (           )
             (         )
              (_______)
              CREATURES!
              
            """)
            print("You enter the cave and find it filled with dangerous creatures.")
            print("Game Over! You were caught by the creatures.")
        else:
            print("\nInvalid choice. You stand confused and the sun sets.")
            print("Game Over! You didn't make a choice.")
    
    elif choice2 == "ignore":
        print("""
        
        ~ ~ ~ ~ ~ ~ ~ ~
       LOST IN FOREST
        ~ ~ ~ ~ ~ ~ ~ ~
        
         X_X
        (   )
         | |
         / \\
        
        """)
        print("You ignore the cabin and continue walking.")
        print("You get lost in the forest and run out of food and water.")
        print("Game Over! You didn't survive.")
    else:
        print("\nInvalid choice.")
        print("Game Over! You couldn't make a decision.")

elif choice1 == "right":
    print("""
    
         --->
        / - \\
       / SHIP \\
      / BEACH  \\
     -----------
    
    """)
    print("You walk right and find yourself near a beach with a ship!")
    print()
    
    choice2 = input("The ship's captain asks: Will you SAIL with me or SEARCH the island? ").lower()
    
    if choice2 == "sail":
        print("""
        
           ~  ~  ~
          ~~BETRAYAL~~
           ~  ~  ~
           
            /|\\
           / | \\
             |
            / \\
            
        """)
        print("The captain betrays you! He sails away leaving you stranded.")
        print("Game Over! You were betrayed.")
    
    elif choice2 == "search":
        print("""
        
        ___     ___
       |   |   |   |
       | T |   | E |
       |   |   |   |
       |___|   |___|
       
        TEMPLE FOUND!
        
        """)
        print("You search the island and find a hidden temple!")
        print()
        
        choice3 = input("Inside the temple, you see three doors. Which do you choose: RED, BLUE, or GREEN? ").lower()
        
        if choice3 == "red":
            print("""
            
             ________
            |        |
            | RED ░░ |
            |   ░░░░ |
            | ░░░  ░ |
            |________|
            
            DOOR OPENS!
            
            """)
            print("The red door opens to a room full of gold and jewels!")
            print("You found the treasure! 🎉")
            print("""
            
             +----------+
             |   GOLD   |
             |   $$$$   |
             | $$    $$ |
             | $  XX  $ |
             | $$    $$ |
             |   $$$$   |
             +----------+
             VICTORY!
             
            """)
            print("Congratulations! You've discovered the treasure and escaped the island!")
        elif choice3 == "blue":
            print("""
            
             ________
            |        |
            | BLUE ░ |
            |   ░░░░ |
            | ░░░  ░ |
            |________|
            
            DEAD END!
            
            """)
            print("The blue door leads to a dead end. You're trapped!")
            print("Game Over! You're stuck.")
        elif choice3 == "green":
            print("""
            
             ________
            |        |
            | GREEN  |
            |  exit  |
            | ~~~~~~ |
            |________|
            
            ESCAPED!
            
            """)
            print("The green door opens to a secret passage leading outside.")
            print("You escape but find no treasure.")
            print("Game Over! You escaped but didn't find the treasure.")
        else:
            print("\nInvalid choice.")
            print("Game Over!")
    else:
        print("\nInvalid choice.")
        print("Game Over! You couldn't make a decision.")

else:
    print("\nInvalid choice. You stand paralyzed by indecision.")
    print("""
    
     ???
     ???
      ?
      
    CONFUSED!
    
    """)
    print("Game Over! You didn't make a choice.")

