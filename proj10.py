#########################################################################
#
#   Computer Project #10
#
#   init_game
#      Create new deck and shuffle
#      Return deck, tableau and empty foundation
#
#   check_ace
#       Return card rank accounting for high ace
#
#   deal_to_tableau
#       Deal a card to each column in tableau unless stock is empty
#
#   validate_foundation
#       Get rank and suit of card if there is one
#       Loop through bottom cards
#       Valid move if card of same suit and higher rank exists in bottom
#
#   move_foundation
#       Check if valid move
#       Remove card from bottom, add it to foundation
#
#   validate_within_tableau
#       Check if to column is empty
#       Check if card in column exists
#       Valid if so
#
#   check_win
#       If all aces win
#
#   display
#       Provided
#
#   main
#       play game
#########################################################################


import cards  # required !!!

RULES = '''
Aces High Card Game:
     Tableau columns are numbered 1,2,3,4.
     Only the card at the bottom of a Tableau column can be moved.
     A card can be moved to the Foundation only if a higher ranked card 
     of the same suit is at the bottom of another Tableau column.
     To win, all cards except aces must be in the Foundation.'''

MENU = '''     
Input options:
    D: Deal to the Tableau (one card on each column).
    F x: Move card from Tableau column x to the Foundation.
    T x y: Move card from Tableau column x to empty Tableau column y.
    R: Restart the game (after shuffling)
    H: Display the menu of choices
    Q: Quit the game        
'''

def init_game():
    '''Create new deck and shuffle
    Deal a card to each collumn
    Return deck, tableau and empty foundation'''
    D = cards.Deck()
    D.shuffle()
    
    tableau = [[],[],[],[]]
    
    for i in range(4):
        
        tableau[i].append(D.deal())
        
    return D, tableau, []
 
def check_ace(card):
    '''If card rank is 1(Ace) set it to 14'''
    r = card.rank()
    
    if card.rank() == 1:
        r = 14
        
    return r
    
def deal_to_tableau( tableau, stock):
    '''Deal a card to each column in tableau unless stock is empty'''
    for i in range(4):
        
        if len(stock) > 0:
            
            tableau[i].append(stock.deal())
            
    return tableau,stock

           
def validate_move_to_foundation( tableau, from_col ):
    '''Get rank and suit of card if there is one
    Loop through bottom cards
    Valid move if card of same suit and higher rank exists in bottom'''
    
    val = 0
    
    if len(tableau[from_col]) > 0:
        
        val = check_ace(tableau[from_col][-1])
        suit = tableau[from_col][-1].suit()
    else:
        
        print("\nError, empty column:")
        return False
    
    for row in tableau:
        
        if len(row) > 0:
            
            if row[-1].suit() == suit and check_ace(row[-1]) > val:
                
                return True
      
    print("\nError, cannot move {}.".format(tableau[from_col][-1]))
    return False

    
def move_to_foundation( tableau, foundation, from_col ):
    '''Check if valid move
    Remove card from bottom, add it to foundation'''
    valid = validate_move_to_foundation(tableau, from_col)  
    
    if valid == True:
        
        card = tableau[from_col].pop()
        foundation.append(card)
        
def validate_move_within_tableau( tableau, from_col, to_col ):
    '''Check if to column is empty
    Check if card in column exists
    Valid if so'''

    if len(tableau[to_col]) == 0:
            
        if len(tableau[from_col]) > 0:
            
            return True
        else:
            
            print("\nError, no card in column:",from_col + 1)
            return False
                
    else:
        
        print("\nError, target column is not empty:",to_col + 1)
        return False



def move_within_tableau( tableau, from_col, to_col ):
    '''Check if move is valid
    If so, remove card from bottom, add to column'''
    valid = validate_move_within_tableau(tableau, from_col, to_col)  
    
    if valid == True:
        
        card = tableau[from_col].pop()
        tableau[to_col].append(card)
        
def check_for_win( tableau, stock ):
    '''Loop through columns
    If there is only 1 card and all aces, win'''
    all_aces = True
    
    for row in tableau:
        
        for card in row:
            
            if check_ace(card) != 14:
                
                all_aces = False
                break
                break
            
    if len(stock) != 0 or all_aces == False:
        return False
    
    return True

def display( stock, tableau, foundation ):
    '''Provided: Display the stock, tableau, and foundation.'''

    print("\n{:<8s}{:^13s}{:s}".format( "stock", "tableau", "  foundation"))
    maxm = 0
    
    for col in tableau:
        
        if len(col) > maxm:
            
            maxm = len(col)
    
    assert maxm > 0   # maxm == 0 should not happen in this game?
        
    for i in range(maxm):
        
        if i == 0:
            
            if stock.is_empty():
                
                print("{:<8s}".format(""),end='')
                
            else:
                
                print("{:<8s}".format(" XX"),end='')
        else:
            
            print("{:<8s}".format(""),end='')        
        
        #prior_ten = False  # indicate if prior card was a ten
        for col in tableau:
            
            if len(col) <= i:
                
                print("{:4s}".format(''), end='')
            else:
                
                print( "{:4s}".format( str(col[i]) ), end='' )

        if i == 0:
            
            if len(foundation) != 0:
                
                print("    {}".format(foundation[-1]), end='')
                
        print()


def get_option():
    '''Get option string from user
    Seperate out
    Check letters
    Get additional information if valid for that letter
    Return option info in list'''
    
    option = input("\nInput an option (DFTRHQ): ")
    op_temp = option
    option = option.lower()
    
    if len(option) == 0:
        return []
    
    if option[0] == 'q':
        
        return ['Q']
    
    if option[0] == 'h':
        
        return ['H']
    
    if option[0] == 'r':
        
        return ['R']
    
    if option[0] == 'd':
        
        if len(option) > 1:
            
            print("\nError in option:",op_temp)
            return []
        
        return ['D']
    
    if option[0] == 'f':
        
        try:
            
            l = option.split(' ')
            
            if len(l) != 2:
                
                f = float("burger")
                
            l[0] = l[0].upper()
            l[1] = int(l[1])
            
            if l[1] > 4 or l[1] < 1:
                f = float("burger")
               
            l[1] = l[1] - 1
                
            return l
            
        except:
            print("\nError in option:",op_temp)
            return []
        
    if option[0] == 't':
        
        try:
            
            l = option.split(' ')
            
            if len(l) != 3:
                f = float("burger")
                
            l[0] = l[0].upper()
            
            l[1] = int(l[1]) 
            
            if l[1] > 4 or l[1] < 1:
                f = float("burger")
                
            l[2] = int(l[2])  
            
            if l[2] > 4 or l[2] < 1:
                f = float("burger")
            
            l[1] = l[1] - 1
            l[2] = l[2] - 1
            
            return l
            
        except:
            
            print("\nError in option:",op_temp)
            return []
    
    print("\nError in option:",op_temp)
    return []
 

def main():
    
    #Initialize game
    stock, tableau, foundation = init_game()
    
    #Print rules and menu
    print(RULES)
    print(MENU)
    
    #Display
    display(stock,tableau,foundation)
    
    #Until user quits
    while True:
        
        #Get option
        option = get_option()
        
        #Make sure option is entered
        if len(option) == 0:
            continue
        
        #Quit option
        if option == ['Q']:
            print("\nYou have chosen to quit.")
            break
        
        #Restart game option
        elif option == ['R']:
            
            print("\n=========== Restarting: new game ============")
            
            print(RULES)
            print(MENU)
            
            #Initialize new game
            stock, tableau, foundation = init_game()
            display(stock,tableau,foundation)
            continue
        
        #Display menu option
        elif option == ['H']:
            print(MENU)
            
        #Deal cards option    
        elif option == ['D']:
            deal_to_tableau(tableau,stock)
        
        #Move card to foundation option
        elif option[0] == 'F':
            move_to_foundation(tableau, foundation, option[1])
        
            #Move card to empty space option
        elif option[0] == 'T':
            move_within_tableau(tableau, option[1], option[2])
        
        #Check for win
        won = check_for_win(tableau,stock)
        
        if won == True:
            print("\nYou won!")
            break
        
        #Display game info
        display(stock,tableau,foundation)

if __name__ == '__main__':
     main()
