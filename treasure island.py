print('''____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/ ''')





print("Welcome to Treasure island \n Your mission is to find the treasure.")

#choose a direction

direction= input("You are at an island. Please choose left or right :\n").lower()
if direction== "right":
    print("You are trapped. \n Game Over hahaha")
elif direction== "left":
    
    #do you wanna swim or wait now
    #Game continues
    
    
    further= input("You have chosen left? \n Do you wanna swim or wait:\n").upper()
    if further == "SWIM":
        print("Attacked by trouts . \n ITS GAME OVER hahahaha")
    elif further == "WAIT":
        
        #which door you wanna choose  



        print("*Your treasure hunt continues*\n Which door you wanna choose?")
        door = input("RED or BLUE or YELLOW--->\n").lower()
        if door == "red":
            print("Burned by fire. You are dead now \n Game Over")
        elif door == "yellow":
            print("You Win the Treasure!!!! Share some of it with your friends  \n CONGRATS for winning the treasure")
        elif door == "blue":    
            print("Eaten by beasts. You are dead now \n Game Over.")
        else:
            print("You chose a non existent door . \n Now its GAME OVER")
    else:
        print("You chose nothing... Its \n GAME OVER hahahaha")
else:
    print("You chose NO direction . YOu are dead now: \n GAME OVER")