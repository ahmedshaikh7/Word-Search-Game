""" Where's That Word? functions. """

# The constant describing the valid directionsf. These should be used
# in functions get_factor and check_guess.
UP = 'up'
DOWN = 'down'
FORWARD = 'forward'
BACKWARD = 'backward'

# The constants describing the multiplicative factor for finding a
# word in a particular direction.  This should be used in get_factor.
FORWARD_FACTOR = 1
DOWN_FACTOR = 2
BACKWARD_FACTOR = 3
UP_FACTOR = 4

# The constant describing the threshold for scoring. This should be
# used in get_points.
THRESHOLD = 5
BONUS = 12

# The constants describing two players and the result of the
# game. These should be used as return values in get_current_player
# and get_winner.
P1 = 'player one'
P2 = 'player two'
P1_WINS = 'player one wins'
P2_WINS = 'player two wins'
TIE = 'tie game'

# The constant describing which puzzle to play. Replace the 'puzzle1.txt' with
# any other puzzle file (e.g., 'puzzle2.txt') to play a different game.
PUZZLE_FILE = 'puzzle1.txt'


# Helper functions.  Do not modify these, although you are welcome to
# call them!

def get_column(puzzle: str, col_num: int) -> str:
    """Return column col_num of puzzle.

    Precondition: 0 <= col_num < number of columns in puzzle

    >>> get_column('abcd\nefgh\nijkl\n', 1)
    'bfj'
    """

    puzzle_list = puzzle.strip().split('\n')
    column = ''
    for row in puzzle_list:
        column += row[col_num]

    return column


def get_row_length(puzzle: str) -> int:
    """Return the length of a row in puzzle.

    >>> get_row_length('abcd\nefgh\nijkl\n')
    4
    """

    return len(puzzle.split('\n')[0])


def contains(text1: str, text2: str) -> bool:
    """Return whether text2 appears anywhere in text1.

    >>> contains('abc', 'bc')
    True
    >>> contains('abc', 'cb')
    False
    """

    return text2 in text1


# Implement the required functions below.

def get_current_player(player_one_turn: bool) -> str:
    """Return 'player one' iff player_one_turn is True; otherwise, return
    'player two'.

    >>> get_current_player(True)
    'player one'
    >>> get_current_player(False)
    'player two'
    """

    # Complete this function.
    if player_one_turn == True:
        return P1
    else:
        return P2
        
def get_winner(x: int, y: int) -> str:
    """Return the value of constants P1_WINS, P2_WINS, or TIE as 
    appropriate based on the score. In this game, the highest score wins/
    >>> get_winner(15,29)
    'player one wins'
    >>> get_winner(29,12)
    'player two wins'
    >>> get_winner(29,29)
    'tie game'
    """
    if(x>y):
        return P1_WINS
    elif(x<y):
        return P2_WINS
    else:
        return TIE
    
def reverse(reversedstring: str) -> str:
    """Return a reversed copy of that string
    >>> reverse('hello')
    'olleh'
    """
    stringlength = len(reversedstring)
    reversedstring = reversedstring[stringlength::-1]
    return reversedstring

def get_row(mix: str, line: int) -> str:
    """Return the letters in the row corresponding 
    to the row number, excluding the newline character. 
    >>>get_row('h\ne\nl\nl\no\n', 1)
    'e'
    """
    return mix.split('\n')[line]  
    
def get_factor(s: str) -> int:
    """Return the multiplicative factor associated with this direction
    >>>get_factor(FORWARD)
    1
    get_factor(DOWN)
    2
    get_factor(BACKWARD)
    3
    get_factor(UP)
    4
    """
    if s == FORWARD:
        return(FORWARD_FACTOR)
    elif s == DOWN:
        return(DOWN_FACTOR)
    elif s == BACKWARD:
        return(BACKWARD_FACTOR)
    elif s == UP:
        return(UP_FACTOR)
    
def get_points(pax: str, lar: int) -> int:
    """ Return the points that would be earned 
    if we were to now find some word in this direction
    >>>
    """
    if lar >= THRESHOLD:
        return THRESHOLD*get_factor(pax)
    elif lar>1 and lar<5:
        return (2*THRESHOLD-lar)*get_factor(pax)
    elif lar == 1:
        return (2*THRESHOLD-lar)*get_factor(pax) + BONUS

        
def check_guess(puzz: str, direc: str, wordy: str, rc: int, left: int) -> int:
    """
    >>> check_guess('abcd\nefgh\nijkl\n', FORWARD, 'abc', 0, 2)
    8
    """
    coll=''
    roww=''
    rev=''
    rev2=''
   
# if direc == UP or DOWN or FORWARD or BACKWARD:
    if direc == UP or direc == DOWN:
        coll = get_column(puzz, rc)
        if direc == UP:
            rev = reverse(wordy)
            if contains(coll, rev) == True:
                return get_points(direc,left)
            else:
                return 0
        elif contains(coll, wordy) == True:
            return get_points(direc, left)
        else:
            return 0


    # else:
    if direc == FORWARD or direc == BACKWARD:
        roww = get_row(puzz, rc)
        if direc == BACKWARD:
            rev2 = reverse(wordy)
            if contains(roww, rev2) == True:
                return get_points(direc,left)
            else:
                return 0
        elif contains(roww,wordy) == True:
            return get_points(direc, left)
        else:
            return 0
    
    



    

    



