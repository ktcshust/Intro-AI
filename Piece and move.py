from copy import deepcopy
def get_opposite_table(table):
    table = deepcopy(table)
    table.reverse()

    for i in range(len(table)):
        for j in range(len(table[i])):
            table[i][j] = 0 - table[i][j]

    return table


# get the value of a piece
def get_piece_value(_piece):
    if _piece == ' ':
        return 0

    return _piece.points


# get the evaluations for a piece at a position according to our piece square tables
def get_piece_evaluation(_piece):
    if _piece == ' ':
        return 0

    row = _piece.row
    col = _piece.col

    piece_table = piece_square_tables[_piece.name]

    if _piece.team == 'white':
        return piece_table[row][col]

    # for black, the evaluations have to be reversed (board reversed)
    else:
        piece_table = get_opposite_table(piece_table)
        return piece_table[row][col]


# get the total value of a board
def get_board_evaluation(_board):
    val = 0

    for row in _board.board:
        for _piece in row:
            val += get_piece_value(_piece) + get_piece_evaluation(_piece)

    return val


# takes in string input and returns appropriate indexes
def parse_input(move: str) -> (int, int, int, int):
    if len(move) != 4:
        return None, None, None, None

    move_piece = move[0] + move[1]
    move_to = move[2] + move[3]

    curr_row = int(move_piece[0]) - 1
    curr_col = ord(move_piece[1]) - ord('a')

    new_row = int(move_to[0]) - 1
    new_col = ord(move_to[1]) - ord('a')

    return curr_row, curr_col, new_row, new_col


# takes in string location and returns the index
def parse_position(pos: str) -> (int, int):
    row = int(pos[0]) - 1
    col = ord(pos[1]) - ord('a')

    return row, col


# takes indexes and returns string input
def un_parse_input(curr_row: int, curr_col: int, new_row: int, new_col: int):
    move_piece = str(curr_row + 1) + chr(curr_col + 97)
    move_to = str(new_row + 1) + chr(new_col + 97)

    return move_piece + move_to


def get_opposite_team(team):
    if team == 'white':
        return 'black'

    if team == 'black':
        return 'white'
        
 class Piece:
    moves = []

    def __init__(self, name, symbol, team, row, col, points):
        self.name = name
        self.symbol = symbol
        self.team = team
        self.row = row
        self.col = col
        self.points = points
        self.has_moved = False

    def update_indexes(self, r, c):
        self.row = r
        self.col = c

    def get_allowed_moves(self, _board):
        allowed_moves = []

        # go through every move available for this piece
        for move in self.moves:
            row = self.row
            col = self.col

            # potential location to move to
            new_row = row + move[0]
            new_col = col + move[1]

            # check that destination is not out of range
            if _board.in_range(new_row, new_col):
                # check that initial location is not empty
                if not _board.is_cell_empty(row, col):
                    # check that the move is possible for that piece
                    if _board.is_move_possible(self, new_row, new_col):
                        # check that there are no team-mates at destination
                        if not _board.team_at_destination(self, new_row, new_col):
                            # check that there are no team-mates blocking the path
                            if not _board.team_in_path(self, new_row, new_col):
                                # form string representation of the move
                                move = extras.un_parse_input(row, col, new_row, new_col)

                                # add to our list
                                if move not in allowed_moves:
                                    allowed_moves.append(move)

        return allowed_moves

    def get_copy(self):
        copy_ = deepcopy(self)
        copy_.name = deepcopy(self.name)
        copy_.symbol = deepcopy(self.symbol)
        copy_.team = deepcopy(self.team)
        copy_.row = deepcopy(self.row)
        copy_.col = deepcopy(self.col)
        copy_.points = deepcopy(self.points)
        copy_.has_moved = deepcopy(self.has_moved)
        copy_.moves = deepcopy(self.moves)

        return deepcopy(copy_)

class Piece_9(Piece):
    def __init__(self, symbol, team, row, col):
        super().__init__('queen', symbol, team, row, col, 9)

        self.moves = [
            [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]   # going right
            [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0] # going down
            [0, -1], [0, -2], [0, -3], [0, -4], [0, -5], [0, -6], [0, -7], [0, -8], [0, -9]  # going left
            [-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0], [-6, 0], [-7, 0], [-8, 0], [-9, 0] # going up
            [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]  # down-right diagonal
            [1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7], [8, -8], [9, -9]  # down-left diagonal
            [-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7], [-8, 8], [-9, 9] # up-right diagonal
            [-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7], [-8, -8], [-9, -9]]  # up-left diagonal
            
class Piece_8(Piece):
    def __init__(self, symbol, team, row, col):
        super().__init__('queen', symbol, team, row, col, 8)

        self.moves = [
            [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8]   # going right
            [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0] # going down
            [0, -1], [0, -2], [0, -3], [0, -4], [0, -5], [0, -6], [0, -7], [0, -8]  # going left
            [-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0], [-6, 0], [-7, 0], [-8, 0] # going up
            [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]  # down-right diagonal
            [1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7], [8, -8]  # down-left diagonal
            [-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7], [-8, 8] # up-right diagonal
            [-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7], [-8, -8]]  # up-left diagonal
       
class Piece_7(Piece):
    def __init__(self, symbol, team, row, col):
        super().__init__('queen', symbol, team, row, col, 7)

        self.moves = [
            [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7]   # going right
            [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0]   # going down
            [0, -1], [0, -2], [0, -3], [0, -4], [0, -5], [0, -6], [0, -7]  # going left
            [-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0], [-6, 0], [-7, 0] # going up
            [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]  # down-right diagonal
            [1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7]  # down-left diagonal
            [-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7] # up-right diagonal
            [-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7]]  # up-left diagonal

class Piece_6(Piece):
    def __init__(self, symbol, team, row, col):
        super().__init__('queen', symbol, team, row, col, 6)

        self.moves = [
            [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6]   # going right
            [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0]   # going down
            [0, -1], [0, -2], [0, -3], [0, -4], [0, -5], [0, -6]  # going left
            [-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0], [-6, 0] # going up
            [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]  # down-right diagonal
            [1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6]  # down-left diagonal
            [-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6] # up-right diagonal
            [-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6]]  # up-left diagonal
            

class Piece_5(Piece):
    def __init__(self, symbol, team, row, col):
        super().__init__('queen', symbol, team, row, col, 5)

        self.moves = [
            [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], # going right
            [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], # going down
            [0, -1], [0, -2], [0, -3], [0, -4], [0, -5], # going left
            [-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0], # going up
            [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], # down-right diagonal
            [1, -1], [2, -2], [3, -3], [4, -4], [5, -5], # down-left diagonal
            [-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], # up-right diagonal
            [-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5]]  # up-left diagonal

class Piece_4(Piece):
    def __init__(self, symbol, team, row, col):
        super().__init__('queen', symbol, team, row, col, 4)

        self.moves = [
            [0, 1], [0, 2], [0, 3], [0, 4], # going right
            [1, 0], [2, 0], [3, 0], [4, 0], # going down
            [0, -1], [0, -2], [0, -3], [0, -4],  # going left
            [-1, 0], [-2, 0], [-3, 0], [-4, 0],  # going up
            [1, 1], [2, 2], [3, 3], [4, 4], # down-right diagonal
            [1, -1], [2, -2], [3, -3], [4, -4], # down-left diagonal
            [-1, 1], [-2, 2], [-3, 3], [-4, 4], # up-right diagonal
            [-1, -1], [-2, -2], [-3, -3], [-4, -4]]  # up-left diagonal
     
class Piece_3(Piece):
    def __init__(self, symbol, team, row, col):
        super().__init__('queen', symbol, team, row, col, 3)

        self.moves = [
            [0, 1], [0, 2], [0, 3], # going right
            [1, 0], [2, 0], [3, 0], # going down
            [0, -1], [0, -2], [0, -3],  # going left
            [-1, 0], [-2, 0], [-3, 0],  # going up
            [1, 1], [2, 2], [3, 3], # down-right diagonal
            [1, -1], [2, -2], [3, -3], # down-left diagonal
            [-1, 1], [-2, 2], [-3, 3], # up-right diagonal
            [-1, -1], [-2, -2], [-3, -3]]  # up-left diagonal

class Piece_2(Piece):
    def __init__(self, symbol, team, row, col):
        super().__init__('queen', symbol, team, row, col, 2)

        self.moves = [
            [0, 1], [0, 2], # going right
            [1, 0], [2, 0], # going down
            [0, -1], [0, -2],  # going left
            [-1, 0], [-2, 0],  # going up
            [1, 1], [2, 2], # down-right diagonal
            [1, -1], [2, -2], # down-left diagonal
            [-1, 1], [-2, 2], # up-right diagonal
            [-1, -1], [-2, -2]]  # up-left diagonal
            
class Piece_1Piece):
    def __init__(self, symbol, team, row, col):
        super().__init__('queen', symbol, team, row, col, 1)

        self.moves = [
            [0, 1], # going right
            [1, 0], # going down
            [0, -1],  # going left
            [-1, 0],  # going up
            [1, 1], # down-right diagonal
            [1, -1], # down-left diagonal
            [-1, 1], # up-right diagonal
            [-1, -1]]  # up-left diagonal
