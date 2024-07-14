#Treasure Island Game
print('''
             .       .                   .       .      .     .      .
            .    .         .    .            .     ______
        .           .             .               ////////
                  .    .   ________   .  .      /////////     .    .
             .            |.____.  /\        ./////////    .
      .                 .//      \/  |\     /////////
         .       .    .//          \ |  \ /////////       .     .   .
                      ||.    .    .| |  ///////// .     .
       .    .         ||           | |//`,/////                .
               .      \\\        ./ //  /  \/   .
    .                  \\\.___./ //\` '   ,_\     .     .
            .           .     \ //////\ , /   \                 .    .
                         .    ///////// \|  '  |    .
        .        .          ///////// .   \ _ /          .
                          /////////                              .
                   .   ./////////     .     .
           .           --------   .                  ..             .
    .               .        .         .                       .
                          ________________________
  ____________------------                        -------------_________
''')
print("Welcome to Space Adventure")
print("Your mission is to escape the aliens")
choice1 = input('You\'re arriving at a planet, do you want to land or keep going? Type "land" or "go".').lower()
if choice1 == 'land':
    print('You are now on a deserted island. You have to find the treasure.')
    choice2 = input('Do you want to go back to the planet or search for the treasure? Type "back" or "search".').lower()
    if choice2 == 'back':
        print('You are now on a deserted island. You have to find the treasure.')
        choice3 = input('Do you want to go back to the planet or search for the treasure? Type "back" or "search".').lower()
        if choice2 == 'search':
            print('You are now on a deserted island. You have to find the treasure.')
            choice4 = input('Do you want to go back to the planet or search for the treasure? Type "back" or "search".').lower()
   


