#import color for printing menu only
import colorama
from colorama import init
init()
from colorama import Fore, Back, Style

def menu_asking():
    '''Esta funcion pregunta se se imprimen las instrucciones. '''
    print(Fore.LIGHTYELLOW_EX + "Do you wish to see the instructions for the game " + Fore.GREEN + "('yes')" + Fore.RED + "('no')" + Fore.WHITE + "" )
    disp_menu = input(" → ")
    if disp_menu == 'yes':

        print(Fore.LIGHTRED_EX+"________________________________________________________________________________________________________________")
        print(Fore.WHITE+"TICK-TACKTOE                                                                                         ")
        print(Fore.RED +  "    INSTRUCTIONS:                                                                                    ")
        print(Fore.YELLOW+"    DISCLAIMER: INPUT CORRECTLY, PROGRAM WILL CRASH IF YOU DON'T INPUT CORRECTLY                     ")  
        print(Fore.LIGHTBLUE_EX+"    There are three game modes in this game.                                                         ")
        print(            "    * The first one will allow you to play with another person.                                      ")
        print(            "    * The second will allow you to play against the machine.                                         ")
        print(            "    * The third one will allow you to play the game as misere tick-tack-toe,                         ")
        print(            "    - basically you need to win by pushing the other person to score a n-in-a-row                    ")
        print(            "                                                                                                     ")
        print(            "                                                                                                     ")
        print(Fore.GREEN+ "    Game Board:                                                                                      ")
        print(Fore.YELLOW+"     _______________________________________________                                                 ")
        print(            "    |               |               |               |                                                ")
        print(            "    |       Q       |       W       |       E       |                                                ")
        print(            "    |               |               |               |                                                ")
        print(            "    |---------------|---------------|---------------|                                                ")
        print(            "    |               |               |               |                                                ")
        print(            "    |       A       |       S       |       D       |                                                ")
        print(            "    |               |               |               |                                                ")
        print(            "    |---------------|---------------|---------------|                                                ")
        print(            "    |               |               |               |                                                ")
        print(            "    |       Z       |       X       |       C       |                                                ")
        print(            "    |               |               |               |                                                ")
        print(            "    |_______________|_______________|_______________|                                                ")
        print(            "                                                                                                     ")
        print(            "                                                                                                     ")
        print(Fore.LIGHTBLUE_EX+"    * This is the order in which the game board will be displayed, thus to                           ")
        print(            "    enter your choice you must enter the letter of the position as they                              ")
        print(            "    were shown to you previously.                                                                    ")
        print(            "    * The first turn will be always chosen randomly by the machine.                                  ")
        print(            "    * If you are playing in the first game mode you must take turns, no cheating!                    ")
        print(            "    * Your player's input will be reflected by the following symbols:                                ")
        print(Fore.CYAN + "        → First  Player : '☺'                                                                        ")
        print(Fore.MAGENTA+"        → Second Player : '☻'                                                                        ")
        print(Fore.LIGHTBLUE_EX+"    * You can play three times, thus only three posible results, you win, you loose and it is a tie. ")
        print(            "    * If no one is the winner, fill up the board and it will automatically reset, the most points wins")
        print(Fore.RED +  "    * You have four times to play after that the points will be rounded and a winner determined or a tie determined")
        print(Fore.LIGHTBLUE_EX+"    * Good Luck ;)                                                                                   ")
        print(Fore.LIGHTRED_EX+"________________________________________________________________________________________________________________")
        print(Fore.WHITE + "")


def primera_fase():
    '''
    Fase 1
    ● Inicialice el tablero vacio
    ● Pida el Nombre del jugador1 y jugador2
    ● Elija aleatoriamente quien tira primero
    ● El juego termina cuando 1 de los 2 logre hacer N in a row
    ● Las coordenadas seran representadas por 9 letras del teclado QWERTY que se elija ,
    pero se debe especificar como aparece en la imagen, en esta imagen se eligieron esas
    9 letras, otra opcion podria ser: WER,SDF,XCV o RTY,FGH,VBN o 789, 456, 123 (si
    tuviera un teclado numerico)
    ● En cada turno se debe desplegar el jugador de turno y se debe pedir la coordenada.
    '''

    ######################################################################################################################################################
    #definir funcion de impresion de tablero #definir funcion de impresion de tablero #definir funcion de impresion de tablero #definir funcion de impresi 
    #definir funcion de impresion de tablero #definir funcion de impresion de tablero #definir funcion de impresion de tablero #definir funcion de impresi
    ######################################################################################################################################################

    board = [
    ' ', ' ', ' ',
    ' ', ' ', ' ',
    ' ', ' ', ' ',
    ]

    spa_ha = str("       ") 
    under_ = str("_______")
    tabs__ = str("|")

    def board_layout():
        '''Inicialice el tablero vacio'''
        #inputs row 1
        print(spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha)
        print(spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha)
        print(spa_ha + board[0] + spa_ha + tabs__ + spa_ha + board[1] + spa_ha + tabs__ + spa_ha + board[2] + spa_ha)
        print(spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha)
        print(under_ + under_ + str("Q") + tabs__ + under_ + under_ + str("W") + tabs__ + under_ + under_ + str("E"))


        #inputs row 2
        print(spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha)
        print(spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha)
        print(spa_ha + board[3] + spa_ha + tabs__ + spa_ha + board[4] + spa_ha + tabs__ + spa_ha + board[5] + spa_ha)
        print(spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha)
        print(under_ + under_ + str("A") + tabs__ + under_ + under_ + str("S") + tabs__ + under_ + under_ + str("D"))


        #inputs row 3
        print(spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha)
        print(spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha)
        print(spa_ha + board[6] + spa_ha + tabs__ + spa_ha + board[7] + spa_ha + tabs__ + spa_ha + board[8] + spa_ha)
        print(spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha)
        print(spa_ha + spa_ha + str("Z") + tabs__ + spa_ha + spa_ha + str("X") + tabs__ + spa_ha + spa_ha+ str("C"))



    ######################################################################################################################################################
    #pida el nombre #pida el nombre #pida el nombre #pida el nombre #pida el nombre #pida el nombre #pida el nombre #pida el nombre #pida el nombre #pida 
    #pida el nombre #pida el nombre #pida el nombre #pida el nombre #pida el nombre #pida el nombre #pida el nombre #pida el nombre #pida el nombre #pida 
    ######################################################################################################################################################
    print(Fore.CYAN + "")
    user_1 = input("Enter Your Name (first user name): → ")

    print(Fore.MAGENTA + "")
    user_2 = input("Enter Your Name (second user name): → ")

    print(str("________________________________________________________________________________________________________________________________________"))
    print(Fore.BLUE + "Welcome ", user_1, str("&") , user_2)
    print(Fore.WHITE + "")


    ######################################################################################################################################################
    #eleccion random #eleccion random #eleccion random #eleccion random #eleccion random #eleccion random #eleccion random #eleccion random #eleccion rand
    #eleccion random #eleccion random #eleccion random #eleccion random #eleccion random #eleccion random #eleccion random #eleccion random #eleccion rand
    ######################################################################################################################################################



    #ELIJA ALEATORIAMENTE QUIÉN TIRA PRIMERO
    #quien va primero
    import random
    randomly_chosen = random.choice([user_1,user_2])
    print(Fore.LIGHTRED_EX + "")
    print(str("________________________________________________________________________________________________________________________________________"))
    print(str("Machine Random Choice → ") + str("'") + randomly_chosen + str("'") + str(" goes first!"))
    print(str("________________________________________________________________________________________________________________________________________"))


    #turnos
    user_1_turn = int(0)
    user_2_turn = int(0)


    #hago comparaciones para determinar quien ya paso y quien deberá pasar despues



    print("")

    clared_board = [' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',]

    #############################################################################################################################################################################################################################################################################################################
    #############################################################################################################################################################################################################################################################################################################
    #############################################################################################################################################################################################################################################################################################################
    #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scena #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scena
    #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scena #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scena
    #############################################################################################################################################################################################################################################################################################################
    #############################################################################################################################################################################################################################################################################################################
    #############################################################################################################################################################################################################################################################################################################

    positions_taken = []

    user_1_points = 0
    user_2_points = 0
    times_played = 0


    if randomly_chosen == user_1:
        while times_played <= int(3):
        
            if user_1_turn % 2 == 0:
                print(Fore.LIGHTGREEN_EX + "")
                print(user_1, str("you're up!"))
                ################################
                
                valid = 'no'
                while valid == 'no': 
                    print(Fore.CYAN + "")
                    input_users = input("Enter the position (  Q  W  E  / A  S  D /  Z  X  C  ): → ")

                    convert = input_users.upper()

                    if convert == 'Q':
                        input_users = 0
                    if convert == 'W':
                        input_users = 1
                    if convert == 'E':
                        input_users = 2
                    if convert == 'A':
                        input_users = 3
                    if convert == 'S':
                        input_users = 4
                    if convert == 'D':
                        input_users = 5
                    if convert == 'Z':
                        input_users = 6
                    if convert == 'X':
                        input_users = 7
                    if convert == 'C':
                        input_users = 8



                    if input_users not in positions_taken:    

                        #warning user not to choose the taken options
                        print("")


                        #inserting input to the board
                        print(Fore.YELLOW + "")
                        board[input_users] = '☺'


                        


                        #calling board layout
                        board_layout()
                        print("")


                        

                        #appending the input to the taken list
                        positions_taken.append(input_users)
                        

                        #######################################################################################################################################################################
                        # first player # first player # first player # first player # first player # first player # first player # first player # first player # first player # first player #f 
                        #######################################################################################################################################################################

                        print(Fore.CYAN + "")

                        #horizontal comparison
                        if (board[0] == '☺' and board[1] == '☺' and board[2] == '☺'):
                            
                            print("")
                            print(user_1, str("congrats you won"))
                            
                            board = clared_board
                            positions_taken = []

                            print("")
                            print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU WON " + user_1 + " ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ 1")
                            print("")

                            print(str("A new game will be started "))
                            
                            user_1_points = user_1_points + int(1)
                            times_played = times_played + int(1)

                            print(user_1,str("Your points are → "), user_1_points)
                            


                        if (board[3] == '☺' and board[4] == '☺' and board[5] == '☺'):
                            print("")
                            print(user_1, str("congrats you won"))
                            
                            board = clared_board
                            positions_taken = []

                            print("")
                            print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU WON " + user_1 + " ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ 2")
                            print("")

                            print(str("A new game will be started "))
                            
                            user_1_points = user_1_points + int(1)
                            times_played = times_played + int(1)

                            print(user_1,str("Your points are → "), user_1_points)



                        if (board[6] == '☺' and board[7] == '☺' and board[8] == '☺'):
                            print("")
                            print(user_1, str("congrats you won"))
                            
                            board = clared_board
                            positions_taken = []

                            print("")
                            print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU WON " + user_1 + " ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ 3")
                            print("")

                            print(str("A new game will be started "))
                            
                            user_1_points = user_1_points + int(1)
                            times_played = times_played + int(1)

                            print(user_1,str("Your points are → "), user_1_points)
                            



                        #vertical comparison
                        if (board[0] == '☺' and board[3] == '☺' and board[6] == '☺'):
                            print("")
                            print(user_1, str("congrats you won"))
                            
                            board = clared_board
                            positions_taken = []

                            print("")
                            print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU WON " + user_1 + " ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ 4")
                            print("")

                            print(str("A new game will be started "))
                            
                            user_1_points = user_1_points + int(1)
                            times_played = times_played + int(1)

                            print(user_1,str("Your points are → "), user_1_points)
                            

                        if (board[1] == '☺' and board[4] == '☺' and board[7] == '☺'):
                            print("")
                            print(user_1, str("congrats you won"))
                            
                            board = clared_board
                            positions_taken = []

                            print("")
                            print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU WON " + user_1 + " ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ 5")
                            print("")

                            print(str("A new game will be started "))
                            
                            user_1_points = user_1_points + int(1)
                            times_played = times_played + int(1)

                            print(user_1,str("Your points are → "), user_1_points)
                            

                        if (board[2] == '☺' and board[5] == '☺' and board[8] == '☺'):
                            print("")
                            print(user_1, str("congrats you won"))
                            
                            board = clared_board
                            positions_taken = []

                            print("")
                            print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU WON " + user_1 + " ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ 6")
                            print("")

                            print(str("A new game will be started "))
                            
                            
                            user_1_points = user_1_points + int(1)
                            times_played = times_played + int(1)

                            print(user_1,str("Your points are → "), user_1_points)
                            


                        #diagonal comparison
                        if (board[0] == '☺' and board[4] == '☺' and board[8] == '☺'):
                            print("")
                            print(user_1, str("congrats you won"))
                            
                            board = clared_board
                            positions_taken = []

                            print("")
                            print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU WON " + user_1 + " ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ 7")
                            print("")

                            print(str("A new game will be started "))
                            
                            user_1_points = user_1_points + int(1)
                            times_played = times_played + int(1)

                            print(user_1,str("Your points are → "), user_1_points)
                            
                            


                        if (board[6] == '☺' and board[4] == '☺' and board[2] == '☺'):
                            print("")
                            print(user_1, str("congrats you won"))
                            
                            board = clared_board
                            positions_taken = []

                            print("")
                            print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU WON " + user_1 + " ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ 8")
                            print("")

                            print(str("A new game will be started "))
                            
                            user_1_points = user_1_points + int(1)
                            times_played = times_played + int(1)

                            print(user_1,str("Your points are → "), user_1_points)


                        #fulll board reset
                        if (board[0] != ' ' and board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' '):
                            print(str("The board is full and no one could score an N-IN a row, a new game will start."))
                            print("Reset #1")
                            
                            times_played = times_played + int(1)
                            board = clared_board
                            positions_taken = []

                        

                        
                        #iterating on user turns
                        user_1_turn = user_1_turn + int(1)

                        valid = 'yes'
                    
                    else:
                        print("")
                        print(Fore.RED + " → This position is already taken, please insert another position.")
                        print(Fore.YELLOW + "Error on user 1")
            
            #####################################################################################################################################################################################################
            #####################################################################################################################################################################################################
            #####################################################################################################################################################################################################
            #####################################################################################################################################################################################################
            
            else:
                    print("")
                    print(Fore.LIGHTGREEN_EX + "")
                    print(user_2, str("you're up!"))
                    ################################
                    valid = 'no'

                    while valid == 'no': 
                        print(Fore.MAGENTA + "")
                        input_users = input("Enter the position (  Q  W  E  / A  S  D /  Z  X  C  ): → ")

                        convert = input_users.upper()

                        if convert == 'Q':
                            input_users = 0
                        if convert == 'W':
                            input_users = 1
                        if convert == 'E':
                            input_users = 2
                        if convert == 'A':
                            input_users = 3
                        if convert == 'S':
                            input_users = 4
                        if convert == 'D':
                            input_users = 5
                        if convert == 'Z':
                            input_users = 6
                        if convert == 'X':
                            input_users = 7
                        if convert == 'C':
                            input_users = 8


                        if input_users not in positions_taken:

                            #inserting input to the board
                            print(Fore.YELLOW + "")
                            board[input_users] = '☻'

                            #iterating on user turns
                            user_2_turn = user_2_turn + 1
                            user_1_turn = user_1_turn + 1
                            

                            #calling board layout
                            board_layout()
                            print("")
                            

                            #iterating on times played
                            

                            #appending the input to the taken list
                            positions_taken.append(input_users)
                            



                            #######################################################################################################################################################################
                            #second player #second player #second player #second player #second player #second player #second player #second player #second player #second player #second player #s
                            #######################################################################################################################################################################

                            print(Fore.MAGENTA + "")
                            
                            #horizontal comparison
                            if (board[0] == '☻' and board[1] == '☻' and board[2] == '☻'):
                                print("")
                                print(user_2, str("congrats you won"))
                                print("")

                                board = clared_board
                                positions_taken = []

                                print("")
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU WON " + user_2 + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ 9")
                                print("")

                                print(str("A new game will be started "))

                                user_2_points = user_2_points + int(1)
                                times_played = times_played + int(1)

                                print(user_2,str("Your points are → "), user_2_points)
                                

                            if (board[3] == '☻' and board[4] == '☻' and board[5] == '☻'):
                                print("")
                                print(user_2, str("congrats you won"))
                                print("")

                                board = clared_board
                                positions_taken = []

                                print("")
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU WON " + user_2 + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ 10")
                                print("")

                                print(str("A new game will be started "))
                                
                                user_2_points = user_2_points + int(1)
                                times_played = times_played + int(1)

                                print(user_2,str("Your points are → "), user_2_points)
                                

                            if (board[6] == '☻' and board[7] == '☻' and board[8] == '☻'):
                                print("")
                                print(user_2, str("congrats you won"))
                                print("")

                                board = clared_board
                                positions_taken = []

                                print("")
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU WON " + user_2 + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ 11")
                                print("")

                                print(str("A new game will be started "))
                                
                                user_2_points = user_2_points + int(1)
                                times_played = times_played + int(1)

                                print(user_2,str("Your points are → "), user_2_points)
                                

                            #vertical comparison
                            if (board[0] == '☻' and board[3] == '☻' and board[6] == '☻'):
                                print("")
                                print(user_2, str("congrats you won"))
                                print("")

                                board = clared_board
                                positions_taken = []

                                print("")
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU WON " + user_2 + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ 12")
                                print("")

                                print(str("A new game will be started "))
                                
                                user_2_points = user_2_points + int(1)
                                times_played = times_played + int(1)

                                print(user_2,str("Your points are → "), user_2_points)
                                


                            if (board[1] == '☻' and board[4] == '☻' and board[7] == '☻'):
                                print("")
                                print(user_2, str("congrats you won"))
                                print("")

                                board = clared_board
                                positions_taken = []

                                print("")
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU WON " + user_2 + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ 13")
                                print("")

                                print(str("A new game will be started "))
                                
                                user_2_points = user_2_points + int(1)
                                times_played = times_played + int(1)

                                print(user_2,str("Your points are → "), user_2_points)
                                

                            if (board[2] == '☻' and board[5] == '☻' and board[8] == '☻'):
                                print("")
                                print(user_2, str("congrats you won"))
                                print("")

                                board = clared_board
                                positions_taken = []

                                print("")
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU WON " + user_2 + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ 14")
                                print("")

                                print(str("A new game will be started "))
                                
                                user_2_points = user_2_points + int(1)
                                times_played = times_played + int(1)

                                print(user_2,str("Your points are → "), user_2_points)
                                

                            #diagonal comparison
                            if (board[0] == '☻' and board[4] == '☻' and board[8] == '☻'):
                                print("")
                                print(user_2, str("congrats you won"))
                                print("")

                                board = clared_board
                                positions_taken = []

                                print("")
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU WON " + user_2 + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ 15")
                                print("")

                                print(str("A new game will be started "))
                                
                                user_2_points = user_2_points + int(1)
                                times_played = times_played + int(1)

                                print(user_2,str("Your points are → "), user_2_points)
                                

                            if (board[6] == '☻' and board[4] == '☻' and board[2] == '☻'):
                                print("")
                                print(user_2, str("congrats you won"))
                                print("")

                                board = clared_board
                                positions_taken = []

                                print("")
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU WON " + user_2 + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ 16")
                                print("")

                                print(str("A new game will be started "))
                                
                                user_2_points = user_2_points + int(1)
                                times_played = times_played + int(1)

                                print(user_2,str("Your points are → "), user_2_points)

                                

                            
                            #fulll board reset
                            if (board[0] != ' ' and board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' '):
                                print(str("The board is full and no one could score an N-IN a row, a new game will start. "))
                                print("Reset #2")
                                
                                times_played = times_played + int(1)
                                board = clared_board
                                positions_taken = []


                            
                            valid = 'yes'

                        else:
                            valid = 'no'
                            print("")
                            print(Fore.RED + " → This position is already taken, please insert another position.")
                            print(Fore.YELLOW + "Error on user2")
                            print(Fore.WHITE + "")
                    



                

















    #############################################################################################################################################################################################################################################################################################################
    #############################################################################################################################################################################################################################################################################################################
    #############################################################################################################################################################################################################################################################################################################
    #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scena #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scena 
    #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scena #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scena 
    #############################################################################################################################################################################################################################################################################################################
    #############################################################################################################################################################################################################################################################################################################
    #############################################################################################################################################################################################################################################################################################################


    if randomly_chosen == user_2:
        while times_played <= int(4):
                if user_2_turn % 2 == 0:

                    print(Fore.LIGHTGREEN_EX + "")
                    print(user_2, str("you're up!"))
                    ################################
                    
                    valid = 'no'
                    while valid == 'no': 
                        print(Fore.MAGENTA + "")
                        input_users = input(str("Enter the position (  Q  W  E  / A  S  D /  Z  X  C  ): → "))

                        convert = input_users.upper()

                        if convert == 'Q':
                            input_users = 0
                        if convert == 'W':
                            input_users = 1
                        if convert == 'E':
                            input_users = 2
                        if convert == 'A':
                            input_users = 3
                        if convert == 'S':
                            input_users = 4
                        if convert == 'D':
                            input_users = 5
                        if convert == 'Z':
                            input_users = 6
                        if convert == 'X':
                            input_users = 7
                        if convert == 'C':
                            input_users = 8



                        if input_users not in positions_taken:    

                            #warning user not to choose the taken options
                            


                            #inserting input to the board
                            print(Fore.YELLOW + "")
                            board[input_users] = '☻'


                            #calling board layout
                            board_layout()
                            print("")

                            #iterating on turns
                            user_2_turn = user_2_turn + 1


                            #appending the input to the taken list
                            positions_taken.append(input_users)
                            



                            ######################################################################################################################################################################
                            #first player # first player # first player # first player # first player # first player # first player # first player # first player # first player # first player #f 
                            ######################################################################################################################################################################

                            print(Fore.MAGENTA + "")

                            #horizontal comparison
                            if (board[0] == '☻' and board[1] == '☻' and board[2] == '☻'):
                                print(user_2, str("congrats you won"))
                                board = clared_board
                                positions_taken = []
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU WON " + user_2 + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ 17")
                                print(str("New game: → "))

                                user_2_points = user_2_points + int(1)
                                times_played = times_played + int(1)

                                print(user_2,str("Your points are → "), user_2_points)




                            if (board[3] == '☻' and board[4] == '☻' and board[5] == '☻'):
                                print(user_2, str("congrats you won"))
                                board = clared_board
                                positions_taken = []
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU WON " + user_2 + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ 18")
                                print(str("New game: → "))

                                user_2_points = user_2_points + int(1)
                                times_played = times_played + int(1)

                                print(user_2,str("Your points are → "), user_2_points)





                            if (board[6] == '☻' and board[7] == '☻' and board[8] == '☻'):
                                print(user_2, str("congrats you won"))
                                board = clared_board
                                positions_taken = []
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU WON " + user_2 + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ 19")
                                print(str("New game: → "))

                                user_2_points = user_2_points + int(1)
                                times_played = times_played + int(1)

                                print(user_2,str("Your points are → "), user_2_points)





                            #vertical comparison
                            if (board[0] == '☻' and board[3] == '☻' and board[6] == '☻'):
                                print(user_2, str("congrats you won"))
                                board = clared_board
                                positions_taken = []
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU WON " + user_2 + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ 20")
                                print(str("New game: → "))

                                user_2_points = user_2_points + int(1)
                                times_played = times_played + int(1)

                                print(user_2,str("Your points are → "), user_2_points)



                            if (board[1] == '☻' and board[4] == '☻' and board[7] == '☻'):
                                print(user_2, str("congrats you won"))
                                board = clared_board
                                positions_taken = []
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU WON " + user_2 + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ 21")
                                print(str("New game: → "))

                                user_2_points = user_2_points + int(1)
                                times_played = times_played + int(1)

                                print(user_2,str("Your points are → "), user_2_points)



                            if (board[2] == '☻' and board[5] == '☻' and board[8] == '☻'):
                                print(user_2, str("congrats you won"))
                                board = clared_board
                                positions_taken = []
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU WON " + user_2 + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ 22")
                                print(str("New game: → "))

                                user_2_points = user_2_points + int(1)
                                times_played = times_played + int(1)

                                print(user_2,str("Your points are → "), user_2_points)



                            #diagonal comparison
                            if (board[0] == '☻' and board[4] == '☻' and board[8] == '☻'):
                                print(user_2, str("congrats you won"))
                                board = clared_board
                                positions_taken = []
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU WON " + user_2 + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ 23")
                                print(str("New game: → "))

                                user_2_points = user_2_points + int(1)
                                times_played = times_played + int(1)

                                print(user_2,str("Your points are → "), user_2_points)



                            if (board[6] == '☻' and board[4] == '☻' and board[2] == '☻'):
                                print(user_2, str("congrats you won"))
                                board = clared_board
                                positions_taken = []
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU WON " + user_2 + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ 24")
                                print(str("New game: → "))

                                user_2_points = user_2_points + int(1)
                                times_played = times_played + int(1)
                                
                                print(user_2,str("Your points are → "), user_2_points)


                            #fulll board reset
                            if (board[0] != ' ' and board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' '):
                                print(str("The board is full and no one could score an N-IN a row, a new game will start. "))
                                print("Reset #3")
                                
                                times_played = times_played + int(1)
                                board = clared_board
                                positions_taken = []
                    
                            valid = 'yes'
                        
                        else:
                            print("")
                            print(Fore.YELLOW + " → This position is already taken, please insert another position.")
                            print(Fore.RED + "Error on user1")
                            print(Fore.WHITE + "Input again.")
                
                #####################################################################################################################################################################################################
                #####################################################################################################################################################################################################
                #####################################################################################################################################################################################################
                #####################################################################################################################################################################################################
                
                else:
                    print("")
                    print(Fore.LIGHTGREEN_EX + "")
                    print(user_1, str("you're up!"))
                    ################################
                    valid = 'no'
                    while valid == 'no': 
                        print(Fore.CYAN + "")
                        input_users = input(str("Enter the position (  Q  W  E  / A  S  D /  Z  X  C  ): → "))

                        convert = input_users.upper()

                        if convert == 'Q':
                            input_users = 0
                        if convert == 'W':
                            input_users = 1
                        if convert == 'E':
                            input_users = 2
                        if convert == 'A':
                            input_users = 3
                        if convert == 'S':
                            input_users = 4
                        if convert == 'D':
                            input_users = 5
                        if convert == 'Z':
                            input_users = 6
                        if convert == 'X':
                            input_users = 7
                        if convert == 'C':
                            input_users = 8


                        if input_users not in positions_taken:

                            #inserting input to the board
                            print(Fore.YELLOW + "")
                            board[input_users] = '☺'

                            #iterating on user turns
                            user_2_turn = user_2_turn + 1
                            user_1_turn = user_1_turn + 1
                            

                            #calling board layout
                            board_layout()
                            print("")


                            #appending the input to the taken list
                            positions_taken.append(input_users)
                            



                            #######################################################################################################################################################################
                            #second player #second player #second player #second player #second player #second player #second player #second player #second player #second player #second player #s
                            #######################################################################################################################################################################

                            print(Fore.CYAN + "")
                            
                            #horizontal comparison
                            if (board[0] == '☺' and board[1] == '☺' and board[2] == '☺'):
                                print(user_1, str("congrats you won"))
                                board = clared_board
                                positions_taken = []
                                print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU WON " + user_1 + "☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ 25")
                                print(str("New game: → "))

                                user_1_points = user_1_points + int(1)
                                times_played = times_played + int(1)

                                print(user_1,str("Your points are → "), user_1_points)



                            if (board[3] == '☺' and board[4] == '☺' and board[5] == '☺'):
                                print(user_1, str("congrats you won"))
                                board = clared_board
                                positions_taken = []
                                print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU WON " + user_1 + "☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ 26")
                                print(str("New game: → "))

                                user_1_points = user_1_points + int(1)
                                times_played = times_played + int(1)

                                print(user_1,str("Your points are → "), user_1_points)



                            if (board[6] == '☺' and board[7] == '☺' and board[8] == '☺'):
                                print(user_1, str("congrats you won"))
                                board = clared_board
                                positions_taken = []
                                print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU WON " + user_1 + "☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ 27")
                                print(str("New game: → "))

                                user_1_points = user_1_points + int(1)
                                times_played = times_played + int(1)

                                print(user_1,str("Your points are → "), user_1_points)



                            #vertical comparison
                            if (board[0] == '☺' and board[3] == '☺' and board[6] == '☺'):
                                print(user_1, str("congrats you won"))
                                board = clared_board
                                positions_taken = []
                                print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU WON " + user_1 + "☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ 28")
                                print(str("New game: → "))

                                user_1_points = user_1_points + int(1)
                                times_played = times_played + int(1)

                                print(user_1,str("Your points are → "), user_1_points)




                            if (board[1] == '☺' and board[4] == '☺' and board[7] == '☺'):
                                print(user_1, str("congrats you won"))
                                board = clared_board
                                positions_taken = []
                                print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU WON " + user_1 + "☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ 29")
                                print(str("New game: → "))

                                user_1_points = user_1_points + int(1)
                                times_played = times_played + int(1)

                                print(user_1,str("Your points are → "), user_1_points)

                            if (board[2] == '☺' and board[5] == '☺' and board[8] == '☺'):
                                print(user_1, str("congrats you won"))
                                board = clared_board
                                positions_taken = []
                                print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU WON " + user_1 + "☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ 30")
                                print(str("New game: → "))

                                user_1_points = user_1_points + int(1)
                                times_played = times_played + int(1)

                                print(user_1,str("Your points are → "), user_1_points)



                            #diagonal comparison
                            if (board[0] == '☺' and board[4] == '☺' and board[8] == '☺'):
                                print(user_1, str("congrats you won"))
                                board = clared_board
                                positions_taken = []
                                print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU WON " + user_1 + "☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ 31")
                                print(str("New game: → "))

                                user_1_points = user_1_points + int(1)
                                times_played = times_played + int(1)

                                print(user_1,str("Your points are → "), user_1_points)




                            if (board[6] == '☺' and board[4] == '☺' and board[2] == '☺'):
                                print(user_1, str("congrats you won"))
                                board = clared_board
                                positions_taken = []
                                print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU WON " + user_1 + "☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ 32")
                                print(str("New game: → "))

                                user_1_points = user_1_points + int(1)
                                times_played = times_played + int(1)

                                print(user_1,str("Your points are → "), user_1_points)
                            


                            #fulll board reset
                            if (board[0] != ' ' and board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' '):
                                print(str("The board is full and no one could score an N-IN a row, a new game will start. "))
                                print("Reset #4")
                                
                                times_played = times_played + int(1)
                                board = clared_board
                                positions_taken = []
                            
                            
                            valid = 'yes'

                        else:
                            valid = 'no'
                            print("")
                            print(Fore.YELLOW + " → This position is already taken, please insert another position.")
                            print(Fore.RED + "Error on user2")
                            print(Fore.WHITE + "Input again.")
                    
    if user_1_points > user_2_points:
        print("")
        print(Fore.RED + "RESULTS:")
        print(user_1 + " " + Fore.RED + "YOU WIN THE GAME, Your Points are", user_1_points)
        print(Fore.WHITE + "")

    if user_2_points > user_1_points:
        print("")
        print(Fore.RED + "RESULTS:")
        print(user_2 + " " + Fore.RED + "YOU WIN THE GAME, Your Points are", user_2_points)
        print(Fore.WHITE + "")

    if user_1_points == user_2_points:
        print("")
        print(Fore.RED + "RESULTS:")
        print(Fore.YELLOW + "UNFORTUNETLY IT'S A TIE!")
        print(Fore.WHITE + "")
    

###################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################
#SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE
#SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE
#SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE
#SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE
#SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE
#SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE
#SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE
#SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE
#SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE
#SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE
#SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE #SEGUNDA FASE
###################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################

def segunda_fase():
    '''
    Fase 2
    ● Debe crear un bot, un oponente que sera la “Computadora”
    ● usted elige como hacer el “algoritmo” del oponente.
    ● Debe crear el nombre del bot de una manera “graciosa” y no puede ser el mismo
    nombre cada partida
    '''

    ############################################################################################################################################################################################################
    ############################################################################################################################################################################################################
    ############################################################################################################################################################################################################
    #get robot name and input of name #get robot name and input of name #get robot name and input of name #get robot name and input of name #get robot name and input of name #get robot name and input of name 
    #get robot name and input of name #get robot name and input of name #get robot name and input of name #get robot name and input of name #get robot name and input of name #get robot name and input of name 
    #get robot name and input of name #get robot name and input of name #get robot name and input of name #get robot name and input of name #get robot name and input of name #get robot name and input of name 
    ############################################################################################################################################################################################################
    ############################################################################################################################################################################################################
    ############################################################################################################################################################################################################
    #you input your name
    print(Fore.CYAN + "")
    user_1 = input(str("Enter Your Name: → "))

    #define a robot name the is random
    print(Fore.MAGENTA + "")
    print(str("Wait for robot to pick name... he's nervous. LOADING..."))
    import urllib.request
    import random
    word_url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = urllib.request.urlopen(word_url)
    long_txt = response.read().decode()
    words = long_txt.splitlines()
    #the robot picks a name
    print("")
    automated_bot = random.choice(words)
    print(str("This is the robot's name: → "), automated_bot)
    print(str("________________________________________________________________________________________________________________________________________"))
    print(Fore.BLUE + "Welcome ", user_1, str("&") , automated_bot)
    print(Fore.WHITE + "")



    #impresion de tablero
    board = [
    ' ', ' ', ' ',
    ' ', ' ', ' ',
    ' ', ' ', ' ',
    ]

    spa_ha = str("       ") 
    under_ = str("_______")
    tabs__ = str("|")

    def board_layout():
        '''Inicialice el tablero vacio'''
        #inputs row 1
        print(spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha)
        print(spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha)
        print(spa_ha + board[0] + spa_ha + tabs__ + spa_ha + board[1] + spa_ha + tabs__ + spa_ha + board[2] + spa_ha)
        print(spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha)
        print(under_ + under_ + str("Q") + tabs__ + under_ + under_ + str("W") + tabs__ + under_ + under_ + str("E"))
        #inputs row 2
        print(spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha)
        print(spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha)
        print(spa_ha + board[3] + spa_ha + tabs__ + spa_ha + board[4] + spa_ha + tabs__ + spa_ha + board[5] + spa_ha)
        print(spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha)
        print(under_ + under_ + str("A") + tabs__ + under_ + under_ + str("S") + tabs__ + under_ + under_ + str("D"))
        #inputs row 3
        print(spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha)
        print(spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha)
        print(spa_ha + board[6] + spa_ha + tabs__ + spa_ha + board[7] + spa_ha + tabs__ + spa_ha + board[8] + spa_ha)
        print(spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha)
        print(spa_ha + spa_ha + str("Z") + tabs__ + spa_ha + spa_ha + str("X") + tabs__ + spa_ha + spa_ha+ str("C"))

    #establecer quien va primero
    import random
    randomly_chosen = user_1
    print(Fore.LIGHTRED_EX + "")
    print(str("________________________________________________________________________________________________________________________________________"))
    print(str("Machine Random Choice → ") + str("'") + randomly_chosen + str("'") + str(" goes first!"))
    print(str("________________________________________________________________________________________________________________________________________"))

    #######################################################################################################################################################

    #list for position
    positions_taken = []
    #user points
    user_1_points = 0
    autom_points = 0
    #control de partidas
    times_played = 0
    #turnos
    user_1_turn = 0
    autom_turn = 0

    clared_board = [' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ']

    automated_bot_list = ['Q', 'W', 'E', 'A', 'S', 'D','Z' ,'X' ,'C']

    #############################################################################################################################################################################################################################################################################################################
    #############################################################################################################################################################################################################################################################################################################
    #############################################################################################################################################################################################################################################################################################################
    #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scena #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scena
    #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scena #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scena
    #############################################################################################################################################################################################################################################################################################################
    #############################################################################################################################################################################################################################################################################################################
    #############################################################################################################################################################################################################################################################################################################

    if randomly_chosen == user_1:
        while times_played <= int(4):
                if user_1_turn % 2 == 0:
                    print(Fore.LIGHTGREEN_EX + "")
                    print(user_1, str("you're up!"))
                    ################################
                    
                    valid = 'no'
                    while valid == 'no': 
                        #fulll board reset
                        if len(automated_bot_list) == 1:
                            print(Fore.YELLOW + "The board is full and no one could score an N-IN a row, thus no one winns and a new game will start.")
                            print(Fore.RED + "Reset #2")
                            
                            times_played = times_played + int(1)
                            board = clared_board
                            positions_taken = []
                            automated_bot_list = ['Q', 'W', 'E', 'A', 'S', 'D','Z' ,'X' ,'C']
                            valid = 'no'
                            print(Fore.LIGHTGREEN_EX + "")
                            print("times played: ", times_played)


                        else:
                            print(Fore.CYAN + "")
                            input_users = input(str("Enter the position (  Q  W  E  / A  S  D /  Z  X  C  ): → "))

                            convert = input_users.upper()
                            print(convert)

                            if convert == 'Q':
                                input_users = 0
                            if convert == 'W':
                                input_users = 1
                            if convert == 'E':
                                input_users = 2
                            if convert == 'A':
                                input_users = 3
                            if convert == 'S':
                                input_users = 4
                            if convert == 'D':
                                input_users = 5
                            if convert == 'Z':
                                input_users = 6
                            if convert == 'X':
                                input_users = 7
                            if convert == 'C':
                                input_users = 8

                            
                            if input_users not in positions_taken:    

                                #warning user not to choose the taken options
                                print("")

                                #remove input from this user from autolist
                                print("automated bot list : ", automated_bot_list)
                                automated_bot_list.remove(convert)
                                print("automated bot list : ", automated_bot_list)

                                #inserting input to the board
                                print(Fore.YELLOW + "")
                                board[input_users] = '☺'


                                #iterating on user turns
                                user_1_turn = user_1_turn + int(1)


                                #calling board layout
                                board_layout()
                                print("")



                                #appending the input to the taken list
                                positions_taken.append(input_users)
                                



                                #######################################################################################################################################################################
                                # first player # first player # first player # first player # first player # first player # first player # first player # first player # first player # first player #f 
                                #######################################################################################################################################################################

                                print(Fore.CYAN + "")

                                #horizontal comparison
                                if (board[0] == '☺' and board[1] == '☺' and board[2] == '☺'):
                                    
                                    print("")
                                    print(user_1, str("congrats you won"))
                                    
                                    board = clared_board
                                    positions_taken = []

                                    print("")
                                    print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU WON " + user_1 + " ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺")
                                    print("")

                                    user_1_points = user_1_points + int(1)
                                    times_played = times_played + int(1)

                                    automated_bot_list = ['Q', 'W', 'E', 'A', 'S', 'D','Z' ,'X' ,'C']

                                    print(str("A new game will be started "))
                                    print(user_1,str("Your points are → "), user_1_points)

                                    
                                    


                                if (board[3] == '☺' and board[4] == '☺' and board[5] == '☺'):
                                    print("")
                                    print(user_1, str("congrats you won"))
                                    
                                    board = clared_board
                                    positions_taken = []

                                    print("")
                                    print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU WON " + user_1 + " ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺")
                                    print("")

                                    automated_bot_list = ['Q', 'W', 'E', 'A', 'S', 'D','Z' ,'X' ,'C']

                                    user_1_points = user_1_points + int(1)
                                    times_played = times_played + int(1)

                                    print(str("A new game will be started "))
                                    print(user_1,str("Your points are → "), user_1_points)
                                    
                                    



                                if (board[6] == '☺' and board[7] == '☺' and board[8] == '☺'):
                                    print("")
                                    print(user_1, str("congrats you won"))
                                    
                                    board = clared_board
                                    positions_taken = []

                                    print("")
                                    print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU WON " + user_1 + " ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺")
                                    print("")

                                    user_1_points = user_1_points + int(1)
                                    times_played = times_played + int(1)

                                    automated_bot_list = ['Q', 'W', 'E', 'A', 'S', 'D','Z' ,'X' ,'C']

                                    print(str("A new game will be started "))
                                    print(user_1,str("Your points are → "), user_1_points)
                                    
                                    



                                #vertical comparison
                                if (board[0] == '☺' and board[3] == '☺' and board[6] == '☺'):
                                    print("")
                                    print(user_1, str("congrats you won"))
                                    
                                    board = clared_board
                                    positions_taken = []

                                    print("")
                                    print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU WON " + user_1 + " ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺")
                                    print("")

                                    user_1_points = user_1_points + int(1)
                                    times_played = times_played + int(1)

                                    automated_bot_list = ['Q', 'W', 'E', 'A', 'S', 'D','Z' ,'X' ,'C']
                                    
                                    print(str("A new game will be started "))
                                    print(user_1,str("Your points are → "), user_1_points)
                                    
                                    
                                    

                                if (board[1] == '☺' and board[4] == '☺' and board[7] == '☺'):
                                    print("")
                                    print(user_1, str("congrats you won"))
                                    
                                    board = clared_board
                                    positions_taken = []

                                    print("")
                                    print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU WON " + user_1 + " ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺")
                                    print("")

                                    user_1_points = user_1_points + int(1)
                                    times_played = times_played + int(1)

                                    automated_bot_list = ['Q', 'W', 'E', 'A', 'S', 'D','Z' ,'X' ,'C']

                                    print(str("A new game will be started "))
                                    print(user_1,str("Your points are → "), user_1_points)
                                    
                                    

                                if (board[2] == '☺' and board[5] == '☺' and board[8] == '☺'):
                                    print("")
                                    print(user_1, str("congrats you won"))
                                    
                                    board = clared_board
                                    positions_taken = []

                                    print("")
                                    print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU WON " + user_1 + " ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺")
                                    print("")

                                    user_1_points = user_1_points + int(1)
                                    times_played = times_played + int(1)

                                    automated_bot_list = ['Q', 'W', 'E', 'A', 'S', 'D','Z' ,'X' ,'C']

                                    print(str("A new game will be started "))
                                    print(user_1,str("Your points are → "), user_1_points)
                                    
                                    


                                #diagonal comparison
                                if (board[0] == '☺' and board[4] == '☺' and board[8] == '☺'):
                                    print("")
                                    print(user_1, str("congrats you won"))
                                    
                                    board = clared_board
                                    positions_taken = []

                                    print("")
                                    print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU WON " + user_1 + " ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺")
                                    print("")

                                    user_1_points = user_1_points + int(1)
                                    times_played = times_played + int(1)

                                    automated_bot_list = ['Q', 'W', 'E', 'A', 'S', 'D','Z' ,'X' ,'C']

                                    print(str("A new game will be started "))
                                    print(user_1,str("Your points are → "), user_1_points)
                                    
                                    


                                if (board[6] == '☺' and board[4] == '☺' and board[2] == '☺'):
                                    print("")
                                    print(user_1, str("congrats you won"))
                                    
                                    board = clared_board
                                    positions_taken = []

                                    print("")
                                    print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU WON " + user_1 + " ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺")
                                    print("")

                                    user_1_points = user_1_points + int(1)
                                    times_played = times_played + int(1)

                                    automated_bot_list = ['Q', 'W', 'E', 'A', 'S', 'D','Z' ,'X' ,'C']

                                    print(str("A new game will be started "))
                                    print(user_1,str("Your points are → "), user_1_points)
                                    
                                    

                                #fulll board reset
                                if (board[0] != ' ' and board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' '):
                                    print("The board is full and no one could score an N-IN a row, thus no one winns and a new game will start.")
                                    print("Reset #1")
                                    
                                    times_played = times_played + int(1)
                                    board = clared_board
                                    positions_taken = []
                                    automated_bot_list = ['Q', 'W', 'E', 'A', 'S', 'D','Z' ,'X' ,'C']
                                    

                                

                                valid = 'yes'
                            
                            else:
                                print("")
                                print(Fore.RED + " → This position is already taken, please insert another position.")
                                print(Fore.YELLOW + "Error on user 1")
                                valid = 'no'
                
                #####################################################################################################################################################################################################
                #####################################################################################################################################################################################################
                #####################################################################################################################################################################################################
                #####################################################################################################################################################################################################
                #automated_bot_list = ['Q', 'W', 'E', 'A', 'S', 'D','Z' ,'X' ,'C']
                else:
                    valid = 'no'
                    while valid == 'no':
                        #fulll board reset
                        if len(automated_bot_list) == 0:
                            print("The board is full and no one could score an N-IN a row, thus no one winns and a new game will start.")
                            print("Reset #2")
                            
                            times_played = times_played + int(1)
                            board = clared_board
                            positions_taken = []
                            automated_bot_list = ['Q', 'W', 'E', 'A', 'S', 'D','Z' ,'X' ,'C']
                            valid = 'no'


                        else:
                            print(Fore.LIGHTGREEN_EX + "")
                            print(automated_bot, str("you're up!"))
                            ################################
                            

                            #######################################################################################################################################################################
                            #second player #second player #second player #second player #second player #second player #second player #second player #second player #second player #second player #s
                            #######################################################################################################################################################################

                            print(Fore.MAGENTA + "")
                                
                            #horizontal comparison
                            if (board[0] == '☻' and board[1] == '☻' and board[2] == '☻'):
                                print("")
                                print(automated_bot, str("congrats you won"))
                                print("")

                                board = clared_board
                                positions_taken = []
                                automated_bot_list = ['Q', 'W', 'E', 'A', 'S', 'D','Z' ,'X' ,'C']

                                print("")
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU WON " + automated_bot + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻")
                                print("")

                                autom_points = autom_points + int(1)
                                times_played = times_played + int(1)

                                print(str("A new game will be started "))
                                print(automated_bot,str("Your points are → "), autom_points)

                                
                                

                            if (board[3] == '☻' and board[4] == '☻' and board[5] == '☻'):
                                print("")
                                print(automated_bot, str("congrats you won"))
                                print("")

                                board = clared_board
                                positions_taken = []
                                automated_bot_list = ['Q', 'W', 'E', 'A', 'S', 'D','Z' ,'X' ,'C']

                                print("")
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU WON " + automated_bot + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻")
                                print("")

                                autom_points = autom_points + int(1)
                                times_played = times_played + int(1)

                                print(str("A new game will be started "))
                                print(automated_bot,str("Your points are → "), autom_points)
                                
                                

                            if (board[6] == '☻' and board[7] == '☻' and board[8] == '☻'):
                                print("")
                                print(automated_bot, str("congrats you won"))
                                print("")

                                board = clared_board
                                positions_taken = []
                                automated_bot_list = ['Q', 'W', 'E', 'A', 'S', 'D','Z' ,'X' ,'C']

                                print("")
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU WON " + automated_bot + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻")
                                print("")

                                autom_points = autom_points + int(1)
                                times_played = times_played + int(1)

                                print(str("A new game will be started "))
                                print(automated_bot,str("Your points are → "), autom_points)
                                
                                

                            #vertical comparison
                            if (board[0] == '☻' and board[3] == '☻' and board[6] == '☻'):
                                print("")
                                print(automated_bot, str("congrats you won"))
                                print("")

                                board = clared_board
                                positions_taken = []
                                automated_bot_list = ['Q', 'W', 'E', 'A', 'S', 'D','Z' ,'X' ,'C']

                                print("")
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU WON " + automated_bot + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻")
                                print("")

                                autom_points = autom_points + int(1)
                                times_played = times_played + int(1)

                                print(str("A new game will be started "))
                                print(automated_bot,str("Your points are → "), autom_points)
                                
                                


                            if (board[1] == '☻' and board[4] == '☻' and board[7] == '☻'):
                                print("")
                                print(automated_bot, str("congrats you won"))
                                print("")

                                board = clared_board
                                positions_taken = []
                                automated_bot_list = ['Q', 'W', 'E', 'A', 'S', 'D','Z' ,'X' ,'C']

                                print("")
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU WON " + automated_bot + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻")
                                print("")

                                autom_points = autom_points + int(1)
                                times_played = times_played + int(1)

                                print(str("A new game will be started "))
                                print(automated_bot,str("Your points are → "), autom_points)
                                
                                

                            if (board[2] == '☻' and board[5] == '☻' and board[8] == '☻'):
                                print("")
                                print(automated_bot, str("congrats you won"))
                                print("")

                                board = clared_board
                                positions_taken = []
                                automated_bot_list = ['Q', 'W', 'E', 'A', 'S', 'D','Z' ,'X' ,'C']

                                print("")
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU WON " + automated_bot + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻")
                                print("")

                                autom_points = autom_points + int(1)
                                times_played = times_played + int(1)

                                print(str("A new game will be started "))
                                print(automated_bot,str("Your points are → "), autom_points)
                                
                                

                            #diagonal comparison
                            if (board[0] == '☻' and board[4] == '☻' and board[8] == '☻'):
                                print("")
                                print(automated_bot, str("congrats you won"))
                                print("")

                                board = clared_board
                                positions_taken = []
                                automated_bot_list = ['Q', 'W', 'E', 'A', 'S', 'D','Z' ,'X' ,'C']

                                print("")
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU WON " + automated_bot + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻")
                                print("")

                                autom_points = autom_points + int(1)
                                times_played = times_played + int(1)

                                print(str("A new game will be started "))
                                print(automated_bot,str("Your points are → "), autom_points)
                                
                                
                                

                            if (board[6] == '☻' and board[4] == '☻' and board[2] == '☻'):
                                print("")
                                print(automated_bot, str("congrats you won"))
                                print("")

                                board = clared_board
                                positions_taken = []
                                automated_bot_list = ['Q', 'W', 'E', 'A', 'S', 'D','Z' ,'X' ,'C']

                                print("")
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU WON " + automated_bot + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻")
                                print("")

                                autom_points = autom_points + int(1)
                                times_played = times_played + int(1)

                                print(str("A new game will be started "))
                                print(automated_bot,str("Your points are → "), autom_points)
                            




                            #start choosing randomly once list is refilled
                            input_users = random.choice(automated_bot_list)
                            print(Fore.MAGENTA + "")
                            print("Robot's choice: → ", input_users)

                            automated_bot_list.remove(input_users)

                            if input_users == 'Q':
                                intconvert = 0
                            if input_users == 'W':
                                intconvert = 1
                            if input_users == 'E':
                                intconvert = 2
                            if input_users == 'A':
                                intconvert = 3
                            if input_users == 'S':
                                intconvert = 4
                            if input_users == 'D':
                                intconvert = 5
                            if input_users == 'Z':
                                intconvert = 6
                            if input_users == 'X':
                                intconvert = 7
                            if input_users == 'C':
                                intconvert = 8

                            #input users are converted in to the indexes 
                            


                            #inserting input to the board
                            print(Fore.YELLOW + "")
                            board[intconvert] = '☻'

                            #iterating on user turns
                            autom_turn = autom_turn + 1
                            user_1_turn = user_1_turn + 1
                            

                            #calling board layout
                            board_layout()
                            print("")
                            

                            #appending the input to the taken list
                            positions_taken.append(intconvert)
                            valid = 'yes'
                        

    if user_1_points > autom_points:
        print("")
        print(Fore.RED + "RESULTS:")
        print(user_1 + " " + Fore.RED + "YOU WIN THE GAME, Your Points are", user_1_points)
        print(Fore.WHITE + "")

    if autom_points > user_1_points:
        print("")
        print(Fore.RED + "RESULTS:")
        print(automated_bot + " " + Fore.RED + "YOU WIN THE GAME, Your Points are", autom_points)
        print(Fore.WHITE + "")

    if user_1_points == autom_points:
        print("")
        print(Fore.RED + "RESULTS:")
        print(Fore.YELLOW + "UNFORTUNETLY IT'S A TIE!")
        print(Fore.WHITE + "")
    


###################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################
#TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE 
#TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE 
#TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE 
#TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE 
#TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE 
#TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE #TERCERA FASE
###################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################
################################################################################################################################################################################################################################################################################################################### 

def misere_ttt():
    '''esta funcion hace lo mismo que la primera solo que pierde el que sace n in a row '''
    ######################################################################################################################################################
    #pida el nombre #pida el nombre #pida el nombre #pida el nombre #pida el nombre #pida el nombre #pida el nombre #pida el nombre #pida el nombre #pida 
    #pida el nombre #pida el nombre #pida el nombre #pida el nombre #pida el nombre #pida el nombre #pida el nombre #pida el nombre #pida el nombre #pida 
    ######################################################################################################################################################
    print(Fore.CYAN + "")
    user_1 = input("Enter Your Name (first user name): → ")

    print(Fore.MAGENTA + "")
    user_2 = input("Enter Your Name (second user name): → ")

    print(str("________________________________________________________________________________________________________________________________________"))
    print(Fore.BLUE + "Welcome ", user_1, str("&") , user_2)
    print(Fore.WHITE + "This is misere tick tack toe!")

        ######################################################################################################################################################
    #definir funcion de impresion de tablero #definir funcion de impresion de tablero #definir funcion de impresion de tablero #definir funcion de impresi 
    #definir funcion de impresion de tablero #definir funcion de impresion de tablero #definir funcion de impresion de tablero #definir funcion de impresi
    ######################################################################################################################################################

    board = [
    ' ', ' ', ' ',
    ' ', ' ', ' ',
    ' ', ' ', ' ',
    ]

    spa_ha = str("       ") 
    under_ = str("_______")
    tabs__ = str("|")

    def board_layout():
        '''Inicialice el tablero vacio'''
        #inputs row 1
        print(spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha)
        print(spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha)
        print(spa_ha + board[0] + spa_ha + tabs__ + spa_ha + board[1] + spa_ha + tabs__ + spa_ha + board[2] + spa_ha)
        print(spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha)
        print(under_ + under_ + str("Q") + tabs__ + under_ + under_ + str("W") + tabs__ + under_ + under_ + str("E"))


        #inputs row 2
        print(spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha)
        print(spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha)
        print(spa_ha + board[3] + spa_ha + tabs__ + spa_ha + board[4] + spa_ha + tabs__ + spa_ha + board[5] + spa_ha)
        print(spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha)
        print(under_ + under_ + str("A") + tabs__ + under_ + under_ + str("S") + tabs__ + under_ + under_ + str("D"))


        #inputs row 3
        print(spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha)
        print(spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha)
        print(spa_ha + board[6] + spa_ha + tabs__ + spa_ha + board[7] + spa_ha + tabs__ + spa_ha + board[8] + spa_ha)
        print(spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha + tabs__ + spa_ha + str(" ") + spa_ha)
        print(spa_ha + spa_ha + str("Z") + tabs__ + spa_ha + spa_ha + str("X") + tabs__ + spa_ha + spa_ha+ str("C"))



    ######################################################################################################################################################
    #eleccion random #eleccion random #eleccion random #eleccion random #eleccion random #eleccion random #eleccion random #eleccion random #eleccion rand
    #eleccion random #eleccion random #eleccion random #eleccion random #eleccion random #eleccion random #eleccion random #eleccion random #eleccion rand
    ######################################################################################################################################################
    #ELIJA ALEATORIAMENTE QUIÉN TIRA PRIMERO
    #quien va primero
    import random
    randomly_chosen = random.choice([user_1,user_2])
    print(Fore.LIGHTRED_EX + "")
    print(str("________________________________________________________________________________________________________________________________________"))
    print(str("Machine Random Choice → ") + str("'") + randomly_chosen + str("'") + str(" goes first!"))
    print(str("________________________________________________________________________________________________________________________________________"))


    #turnos
    user_1_turn = int(0)
    user_2_turn = int(0)


    #hago comparaciones para determinar quien ya paso y quien deberá pasar despues



    print("")

    clared_board = [' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',]

    #############################################################################################################################################################################################################################################################################################################
    #############################################################################################################################################################################################################################################################################################################
    #############################################################################################################################################################################################################################################################################################################
    #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scena #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scena
    #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scena #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scenario #1st scena
    #############################################################################################################################################################################################################################################################################################################
    #############################################################################################################################################################################################################################################################################################################
    #############################################################################################################################################################################################################################################################################################################

    positions_taken = []

    user_1_points = 0
    user_2_points = 0
    times_played = 0


    if randomly_chosen == user_1:
        while times_played <= int(4):
        
            if user_1_turn % 2 == 0:
                print(Fore.LIGHTGREEN_EX + "")
                print(user_1, str("you're up!"))
                ################################
                
                valid = 'no'
                while valid == 'no': 
                    print(Fore.CYAN + "")
                    input_users = input("Enter the position (  Q  W  E  / A  S  D /  Z  X  C  ): → ")

                    convert = input_users.upper()

                    if convert == 'Q':
                        input_users = 0
                    if convert == 'W':
                        input_users = 1
                    if convert == 'E':
                        input_users = 2
                    if convert == 'A':
                        input_users = 3
                    if convert == 'S':
                        input_users = 4
                    if convert == 'D':
                        input_users = 5
                    if convert == 'Z':
                        input_users = 6
                    if convert == 'X':
                        input_users = 7
                    if convert == 'C':
                        input_users = 8



                    if input_users not in positions_taken:    

                        #warning user not to choose the taken options
                        print("")


                        #inserting input to the board
                        print(Fore.YELLOW + "")
                        board[input_users] = '☺'


                        


                        #calling board layout
                        board_layout()
                        print("")


                        

                        #appending the input to the taken list
                        positions_taken.append(input_users)
                        

                        #######################################################################################################################################################################
                        # first player # first player # first player # first player # first player # first player # first player # first player # first player # first player # first player #f 
                        #######################################################################################################################################################################

                        print(Fore.CYAN + "")

                        #horizontal comparison
                        if (board[0] == '☺' and board[1] == '☺' and board[2] == '☺'):
                            
                            print("")
                            print(user_1, str("you lost!"))
                            
                            board = clared_board
                            positions_taken = []

                            print("")
                            print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU LOST " + user_1 + " ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺")
                            print("")

                            print(str("A new game will be started "))
                            
                            user_1_points = user_1_points + int(1)
                            times_played = times_played + int(1)

                            
                            


                        if (board[3] == '☺' and board[4] == '☺' and board[5] == '☺'):
                            print("")
                            print(user_1, str("you lost!"))
                            
                            board = clared_board
                            positions_taken = []

                            print("")
                            print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU LOST " + user_1 + " ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺")
                            print("")

                            print(str("A new game will be started "))
                            
                            user_1_points = user_1_points + int(1)
                            times_played = times_played + int(1)

                            



                        if (board[6] == '☺' and board[7] == '☺' and board[8] == '☺'):
                            print("")
                            print(user_1, str("you lost!"))
                            
                            board = clared_board
                            positions_taken = []

                            print("")
                            print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU LOST " + user_1 + " ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺")
                            print("")

                            print(str("A new game will be started "))
                            
                            user_1_points = user_1_points + int(1)
                            times_played = times_played + int(1)

                            
                            



                        #vertical comparison
                        if (board[0] == '☺' and board[3] == '☺' and board[6] == '☺'):
                            print("")
                            print(user_1, str("you lost!"))
                            
                            board = clared_board
                            positions_taken = []

                            print("")
                            print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU LOST " + user_1 + " ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺")
                            print("")

                            print(str("A new game will be started "))
                            
                            user_1_points = user_1_points + int(1)
                            times_played = times_played + int(1)

                            
                            

                        if (board[1] == '☺' and board[4] == '☺' and board[7] == '☺'):
                            print("")
                            print(user_1, str("you lost!"))
                            
                            board = clared_board
                            positions_taken = []

                            print("")
                            print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU LOST " + user_1 + " ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺")
                            print("")

                            print(str("A new game will be started "))
                            
                            user_1_points = user_1_points + int(1)
                            times_played = times_played + int(1)

                            
                            

                        if (board[2] == '☺' and board[5] == '☺' and board[8] == '☺'):
                            print("")
                            print(user_1, str("you lost!"))
                            
                            board = clared_board
                            positions_taken = []

                            print("")
                            print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU LOST " + user_1 + " ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺")
                            print("")

                            print(str("A new game will be started "))
                            
                            
                            user_1_points = user_1_points + int(1)
                            times_played = times_played + int(1)

                            
                            


                        #diagonal comparison
                        if (board[0] == '☺' and board[4] == '☺' and board[8] == '☺'):
                            print("")
                            print(user_1, str("you lost!"))
                            
                            board = clared_board
                            positions_taken = []

                            print("")
                            print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU LOST " + user_1 + " ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺")
                            print("")

                            print(str("A new game will be started "))
                            
                            user_1_points = user_1_points + int(1)
                            times_played = times_played + int(1)

                            
                            
                            


                        if (board[6] == '☺' and board[4] == '☺' and board[2] == '☺'):
                            print("")
                            print(user_1, str("you lost!"))
                            
                            board = clared_board
                            positions_taken = []

                            print("")
                            print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU LOST " + user_1 + " ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺")
                            print("")

                            print(str("A new game will be started "))
                            
                            user_1_points = user_1_points + int(1)
                            times_played = times_played + int(1)

                            


                        #fulll board reset
                        if (board[0] != ' ' and board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' '):
                            print(str("The board is full and no one could score an N-IN a row, thus no one winns and a new game will start."))
                            print("Reset #1")
                            
                            times_played = times_played + int(1)
                            board = clared_board
                            positions_taken = []

                        

                        
                        #iterating on user turns
                        user_1_turn = user_1_turn + int(1)

                        valid = 'yes'
                    
                    else:
                        print("")
                        print(Fore.RED + " → This position is already taken, please insert another position.")
                        print(Fore.YELLOW + "Error on user 1")
            
            #####################################################################################################################################################################################################
            #####################################################################################################################################################################################################
            #####################################################################################################################################################################################################
            #####################################################################################################################################################################################################
            
            else:
                    print("")
                    print(Fore.LIGHTGREEN_EX + "")
                    print(user_2, str("you're up!"))
                    ################################
                    valid = 'no'

                    while valid == 'no': 
                        print(Fore.MAGENTA + "")
                        input_users = input("Enter the position (  Q  W  E  / A  S  D /  Z  X  C  ): → ")

                        convert = input_users.upper()

                        if convert == 'Q':
                            input_users = 0
                        if convert == 'W':
                            input_users = 1
                        if convert == 'E':
                            input_users = 2
                        if convert == 'A':
                            input_users = 3
                        if convert == 'S':
                            input_users = 4
                        if convert == 'D':
                            input_users = 5
                        if convert == 'Z':
                            input_users = 6
                        if convert == 'X':
                            input_users = 7
                        if convert == 'C':
                            input_users = 8


                        if input_users not in positions_taken:

                            #inserting input to the board
                            print(Fore.YELLOW + "")
                            board[input_users] = '☻'

                            #iterating on user turns
                            user_2_turn = user_2_turn + 1
                            user_1_turn = user_1_turn + 1
                            

                            #calling board layout
                            board_layout()
                            print("")
                            

                            #iterating on times played
                            

                            #appending the input to the taken list
                            positions_taken.append(input_users)
                            



                            #######################################################################################################################################################################
                            #second player #second player #second player #second player #second player #second player #second player #second player #second player #second player #second player #s
                            #######################################################################################################################################################################

                            print(Fore.MAGENTA + "")
                            
                            #horizontal comparison
                            if (board[0] == '☻' and board[1] == '☻' and board[2] == '☻'):
                                print("")
                                print(user_2, str("you lost!"))
                                print("")

                                board = clared_board
                                positions_taken = []

                                print("")
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU LOST " + user_2 + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻")
                                print("")

                                print(str("A new game will be started "))

                                user_2_points = user_2_points + int(1)
                                times_played = times_played + int(1)

                                
                                

                            if (board[3] == '☻' and board[4] == '☻' and board[5] == '☻'):
                                print("")
                                print(user_2, str("you lost!"))
                                print("")

                                board = clared_board
                                positions_taken = []

                                print("")
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU LOST " + user_2 + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻")
                                print("")

                                print(str("A new game will be started "))
                                
                                user_2_points = user_2_points + int(1)
                                times_played = times_played + int(1)

                                
                                

                            if (board[6] == '☻' and board[7] == '☻' and board[8] == '☻'):
                                print("")
                                print(user_2, str("you lost!"))
                                print("")

                                board = clared_board
                                positions_taken = []

                                print("")
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU LOST " + user_2 + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻")
                                print("")

                                print(str("A new game will be started "))
                                
                                user_2_points = user_2_points + int(1)
                                times_played = times_played + int(1)

                                
                                

                            #vertical comparison
                            if (board[0] == '☻' and board[3] == '☻' and board[6] == '☻'):
                                print("")
                                print(user_2, str("you lost!"))
                                print("")

                                board = clared_board
                                positions_taken = []

                                print("")
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU LOST " + user_2 + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻")
                                print("")

                                print(str("A new game will be started "))
                                
                                user_2_points = user_2_points + int(1)
                                times_played = times_played + int(1)

                                
                                


                            if (board[1] == '☻' and board[4] == '☻' and board[7] == '☻'):
                                print("")
                                print(user_2, str("you lost!"))
                                print("")

                                board = clared_board
                                positions_taken = []

                                print("")
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU LOST " + user_2 + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻")
                                print("")

                                print(str("A new game will be started "))
                                
                                user_2_points = user_2_points + int(1)
                                times_played = times_played + int(1)

                                
                                

                            if (board[2] == '☻' and board[5] == '☻' and board[8] == '☻'):
                                print("")
                                print(user_2, str("you lost!"))
                                print("")

                                board = clared_board
                                positions_taken = []

                                print("")
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU LOST " + user_2 + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻")
                                print("")

                                print(str("A new game will be started "))
                                
                                user_2_points = user_2_points + int(1)
                                times_played = times_played + int(1)

                                
                                

                            #diagonal comparison
                            if (board[0] == '☻' and board[4] == '☻' and board[8] == '☻'):
                                print("")
                                print(user_2, str("you lost!"))
                                print("")

                                board = clared_board
                                positions_taken = []

                                print("")
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU LOST " + user_2 + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻")
                                print("")

                                print(str("A new game will be started "))
                                
                                user_2_points = user_2_points + int(1)
                                times_played = times_played + int(1)

                                
                                

                            if (board[6] == '☻' and board[4] == '☻' and board[2] == '☻'):
                                print("")
                                print(user_2, str("you lost!"))
                                print("")

                                board = clared_board
                                positions_taken = []

                                print("")
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU LOST " + user_2 + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻")
                                print("")

                                print(str("A new game will be started "))
                                
                                user_2_points = user_2_points + int(1)
                                times_played = times_played + int(1)

                                

                                

                            
                            #fulll board reset
                            if (board[0] != ' ' and board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' '):
                                print(str("The board is full and no one could score an N-IN a row, thus no one winns and a new game will start. "))
                                print("Reset #2")
                                
                                times_played = times_played + int(1)
                                board = clared_board
                                positions_taken = []


                            
                            valid = 'yes'

                        else:
                            valid = 'no'
                            print("")
                            print(Fore.RED + " → This position is already taken, please insert another position.")
                            print(Fore.YELLOW + "Error on user2")
                            print("")
                    



                

















    #############################################################################################################################################################################################################################################################################################################
    #############################################################################################################################################################################################################################################################################################################
    #############################################################################################################################################################################################################################################################################################################
    #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scena #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scena 
    #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scena #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scenario #2nd scena 
    #############################################################################################################################################################################################################################################################################################################
    #############################################################################################################################################################################################################################################################################################################
    #############################################################################################################################################################################################################################################################################################################


    if randomly_chosen == user_2:
        while times_played <= int(3):
                if user_2_turn % 2 == 0:

                    print(Fore.LIGHTGREEN_EX + "")
                    print(user_2, str("you're up!"))
                    ################################
                    
                    valid = 'no'
                    while valid == 'no': 
                        print(Fore.MAGENTA + "")
                        input_users = input(str("Enter the position (  Q  W  E  / A  S  D /  Z  X  C  ): → "))

                        convert = input_users.upper()

                        if convert == 'Q':
                            input_users = 0
                        if convert == 'W':
                            input_users = 1
                        if convert == 'E':
                            input_users = 2
                        if convert == 'A':
                            input_users = 3
                        if convert == 'S':
                            input_users = 4
                        if convert == 'D':
                            input_users = 5
                        if convert == 'Z':
                            input_users = 6
                        if convert == 'X':
                            input_users = 7
                        if convert == 'C':
                            input_users = 8



                        if input_users not in positions_taken:    

                            #warning user not to choose the taken options
                            


                            #inserting input to the board
                            print(Fore.YELLOW + "")
                            board[input_users] = '☻'


                            #calling board layout
                            board_layout()
                            print("")

                            #iterating on turns
                            user_2_turn = user_2_turn + 1


                            #appending the input to the taken list
                            positions_taken.append(input_users)
                            



                            ######################################################################################################################################################################
                            #first player # first player # first player # first player # first player # first player # first player # first player # first player # first player # first player #f 
                            ######################################################################################################################################################################

                            print(Fore.MAGENTA + "")

                            #horizontal comparison
                            if (board[0] == '☻' and board[1] == '☻' and board[2] == '☻'):
                                print(user_2, str("you lost!"))
                                board = clared_board
                                positions_taken = []
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU LOST " + user_2 + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻")
                                print(str("New game: → "))

                                user_2_points = user_2_points + int(1)
                                times_played = times_played + int(1)

                                print(user_2,str("Your points are → "), user_2_points)




                            if (board[3] == '☻' and board[4] == '☻' and board[5] == '☻'):
                                print(user_2, str("you lost!"))
                                board = clared_board
                                positions_taken = []
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU LOST " + user_2 + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻")
                                print(str("New game: → "))

                                user_2_points = user_2_points + int(1)
                                times_played = times_played + int(1)

                                print(user_2,str("Your points are → "), user_2_points)





                            if (board[6] == '☻' and board[7] == '☻' and board[8] == '☻'):
                                print(user_2, str("you lost!"))
                                board = clared_board
                                positions_taken = []
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU LOST " + user_2 + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻")
                                print(str("New game: → "))

                                user_2_points = user_2_points + int(1)
                                times_played = times_played + int(1)

                                print(user_2,str("Your points are → "), user_2_points)





                            #vertical comparison
                            if (board[0] == '☻' and board[3] == '☻' and board[6] == '☻'):
                                print(user_2, str("you lost!"))
                                board = clared_board
                                positions_taken = []
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU LOST " + user_2 + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻")
                                print(str("New game: → "))

                                user_2_points = user_2_points + int(1)
                                times_played = times_played + int(1)

                                print(user_2,str("Your points are → "), user_2_points)



                            if (board[1] == '☻' and board[4] == '☻' and board[7] == '☻'):
                                print(user_2, str("you lost!"))
                                board = clared_board
                                positions_taken = []
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU LOST " + user_2 + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻")
                                print(str("New game: → "))

                                user_2_points = user_2_points + int(1)
                                times_played = times_played + int(1)

                                print(user_2,str("Your points are → "), user_2_points)



                            if (board[2] == '☻' and board[5] == '☻' and board[8] == '☻'):
                                print(user_2, str("you lost!"))
                                board = clared_board
                                positions_taken = []
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU LOST " + user_2 + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻")
                                print(str("New game: → "))

                                user_2_points = user_2_points + int(1)
                                times_played = times_played + int(1)

                                print(user_2,str("Your points are → "), user_2_points)



                            #diagonal comparison
                            if (board[0] == '☻' and board[4] == '☻' and board[8] == '☻'):
                                print(user_2, str("you lost!"))
                                board = clared_board
                                positions_taken = []
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU LOST " + user_2 + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻")
                                print(str("New game: → "))

                                user_2_points = user_2_points + int(1)
                                times_played = times_played + int(1)

                                print(user_2,str("Your points are → "), user_2_points)



                            if (board[6] == '☻' and board[4] == '☻' and board[2] == '☻'):
                                print(user_2, str("you lost!"))
                                board = clared_board
                                positions_taken = []
                                print("☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ YOU LOST " + user_2 + " ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻ ☻")
                                print(str("New game: → "))

                                user_2_points = user_2_points + int(1)
                                times_played = times_played + int(1)
                                
                                print(user_2,str("Your points are → "), user_2_points)


                            #fulll board reset
                            if (board[0] != ' ' and board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' '):
                                print(str("The board is full and no one could score an N-IN a row, thus no one winns and a new game will start. "))
                                print("Reset #3")
                                
                                times_played = times_played + int(1)
                                board = clared_board
                                positions_taken = []
                        

                            

                            
                            

                            valid = 'yes'
                        
                        else:
                            print("")
                            print(Fore.YELLOW + " → This position is already taken, please insert another position.")
                            print(Fore.RED + "Error on user1")
                            print(Fore.WHITE + "Input again.")
                
                #####################################################################################################################################################################################################
                #####################################################################################################################################################################################################
                #####################################################################################################################################################################################################
                #####################################################################################################################################################################################################
                
                else:
                    print("")
                    print(Fore.LIGHTGREEN_EX + "")
                    print(user_1, str("you're up!"))
                    ################################
                    valid = 'no'
                    while valid == 'no': 
                        print(Fore.CYAN + "")
                        input_users = input(str("Enter the position (  Q  W  E  / A  S  D /  Z  X  C  ): → "))

                        convert = input_users.upper()

                        if convert == 'Q':
                            input_users = 0
                        if convert == 'W':
                            input_users = 1
                        if convert == 'E':
                            input_users = 2
                        if convert == 'A':
                            input_users = 3
                        if convert == 'S':
                            input_users = 4
                        if convert == 'D':
                            input_users = 5
                        if convert == 'Z':
                            input_users = 6
                        if convert == 'X':
                            input_users = 7
                        if convert == 'C':
                            input_users = 8


                        if input_users not in positions_taken:

                            #inserting input to the board
                            print(Fore.YELLOW + "")
                            board[input_users] = '☺'

                            #iterating on user turns
                            user_2_turn = user_2_turn + 1
                            user_1_turn = user_1_turn + 1
                            

                            #calling board layout
                            board_layout()
                            print("")


                            #appending the input to the taken list
                            positions_taken.append(input_users)
                            



                            #######################################################################################################################################################################
                            #second player #second player #second player #second player #second player #second player #second player #second player #second player #second player #second player #s
                            #######################################################################################################################################################################

                            print(Fore.CYAN + "")
                            
                            #horizontal comparison
                            if (board[0] == '☺' and board[1] == '☺' and board[2] == '☺'):
                                print(user_1, str("you lost!"))
                                board = clared_board
                                positions_taken = []
                                print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU LOST " + user_1 + "☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺")
                                print(str("New game: → "))

                                user_1_points = user_1_points + int(1)
                                times_played = times_played + int(1)

                                



                            if (board[3] == '☺' and board[4] == '☺' and board[5] == '☺'):
                                print(user_1, str("you lost!"))
                                board = clared_board
                                positions_taken = []
                                print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU LOST " + user_1 + "☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺")
                                print(str("New game: → "))

                                user_1_points = user_1_points + int(1)
                                times_played = times_played + int(1)

                                



                            if (board[6] == '☺' and board[7] == '☺' and board[8] == '☺'):
                                print(user_1, str("you lost!"))
                                board = clared_board
                                positions_taken = []
                                print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU LOST " + user_1 + "☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺")
                                print(str("New game: → "))

                                user_1_points = user_1_points + int(1)
                                times_played = times_played + int(1)

                                



                            #vertical comparison
                            if (board[0] == '☺' and board[3] == '☺' and board[6] == '☺'):
                                print(user_1, str("you lost!"))
                                board = clared_board
                                positions_taken = []
                                print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU LOST " + user_1 + "☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺")
                                print(str("New game: → "))

                                user_1_points = user_1_points + int(1)
                                times_played = times_played + int(1)

                                




                            if (board[1] == '☺' and board[4] == '☺' and board[7] == '☺'):
                                print(user_1, str("you lost!"))
                                board = clared_board
                                positions_taken = []
                                print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU LOST " + user_1 + "☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺")
                                print(str("New game: → "))

                                user_1_points = user_1_points + int(1)
                                times_played = times_played + int(1)

                                

                            if (board[2] == '☺' and board[5] == '☺' and board[8] == '☺'):
                                print(user_1, str("you lost!"))
                                board = clared_board
                                positions_taken = []
                                print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU LOST " + user_1 + "☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺")
                                print(str("New game: → "))

                                user_1_points = user_1_points + int(1)
                                times_played = times_played + int(1)

                                



                            #diagonal comparison
                            if (board[0] == '☺' and board[4] == '☺' and board[8] == '☺'):
                                print(user_1, str("you lost!"))
                                board = clared_board
                                positions_taken = []
                                print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU LOST " + user_1 + "☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ")
                                print(str("New game: → "))

                                user_1_points = user_1_points + int(1)
                                times_played = times_played + int(1)

                                




                            if (board[6] == '☺' and board[4] == '☺' and board[2] == '☺'):
                                print(user_1, str("you lost!"))
                                board = clared_board
                                positions_taken = []
                                print("☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ YOU LOST " + user_1 + "☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺")
                                print(str("New game: → "))

                                user_1_points = user_1_points + int(1)
                                times_played = times_played + int(1)

                                
                            


                            #fulll board reset
                            if (board[0] != ' ' and board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' '):
                                print(str("The board is full and no one could score an N-IN a row, thus no one winns and a new game will start. "))
                                print("Reset #4")
                                
                                times_played = times_played + int(1)
                                board = clared_board
                                positions_taken = []
                            
                            
                            valid = 'yes'

                        else:
                            valid = 'no'
                            print("")
                            print(Fore.YELLOW + " → This position is already taken, please insert another position.")
                            print(Fore.RED + "Error on user2")
                            print(Fore.WHITE + "Input again.")
                    
    if user_1_points > user_2_points:
        print("")
        print(Fore.RED + "RESULTS:")
        print(user_1 + " " + Fore.RED + "YOU LOST THE GAME " + user_2 + " WON")
        print(Fore.WHITE + "")

    if user_2_points > user_1_points:
        print("")
        print(Fore.RED + "RESULTS:")
        print(user_2 + " " + Fore.RED + "YOU LOST THE GAME" + user_1 + "WON")
        print(Fore.WHITE + "")

    if user_1_points == user_2_points:
        print("")
        print(Fore.RED + "RESULTS:")
        print(Fore.YELLOW + "UNFORTUNETLY IT'S A TIE!")
        print(Fore.WHITE + "")




######################################################################################################################################################################################################################
######################################################################################################################################################################################################################
######################################################################################################################################################################################################################
######################################################################################################################################################################################################################
######################################################################################################################################################################################################################
######################################################################################################################################################################################################################
######################################################################################################################################################################################################################
#MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MEN
#MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MEN
#MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MEN
#MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MEN
#MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MEN
#MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MENU #MEN
######################################################################################################################################################################################################################
######################################################################################################################################################################################################################
######################################################################################################################################################################################################################
######################################################################################################################################################################################################################
######################################################################################################################################################################################################################
######################################################################################################################################################################################################################
print(Fore.GREEN + "Welcome to Tick Tack Toe! to see the play menu type 'yes': →")
user_choice = input(" → ")

if user_choice == 'yes': 
    menu_asking()
    print(Fore.YELLOW + "There are three modes to this game: " + Fore.RED +  "2player," + Fore.YELLOW +" 1vsmachine" + Fore.CYAN + " and" + Fore.GREEN + " misere" + Fore.CYAN + " please select which game mode you would like: → ")
    mode = input(" → ")
    if mode == '2player':
        primera_fase()
    if mode == '1vsmachine':
        segunda_fase()
    if mode == 'misere':
        misere_ttt()


print(Fore.YELLOW + "David Gabriel Corzo Mcmath -" + Fore.RED + "Coding Course UFM -" + Fore.CYAN + "20190432 -" + Fore.GREEN + "2019")