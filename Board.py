from copy import deepcopy
class ChessBoard:
    board = []
    row_ = 11
    column_ = 9
 def __init__(self, skip):
        if not skip:
            for i in range(self.row_):
                col = []
                for j in range(self.column_):
                    col.append(' ')

                self.board.append(col)

    # put initial pieces on the actual board
    def place_pieces(self):
        # placing black pieces on top of board
        self.board[0][0] = piece.Piece1('1', 'black', 0, 0)
        self.board[0][1] = piece.Piece2('2', 'black', 0, 1)
        self.board[0][2] = piece.Piece3('3', 'black', 0, 2)
        self.board[0][3] = piece.Piece4('4', 'black', 0, 3)
        self.board[0][4] = piece.Piece5('5', 'black', 0, 4)
        self.board[0][5] = piece.Piece6('6', 'black', 0, 5)
        self.board[0][6] = piece.Piece7('7', 'black', 0, 6)
        self.board[0][7] = piece.Piece8('8', 'black', 0, 7)
        self.board[0][8] = piece.Piece9('9', 'black', 0, 8)
        self.board[1][4] = piece.Piece0('0', 'black', 1, 4)

      

        # placing white pieces
        self.board[10][0] = piece.Piece1('1', 'white', 10, 0)
        self.board[10][1] = piece.Piece2('2', 'white', 10, 1)
        self.board[10][2] = piece.Piece3('3', 'white', 10, 2)
        self.board[10][3] = piece.Piece4('4', 'white', 10, 3)
        self.board[10][4] = piece.Piece5('5', 'white', 10, 4)
        self.board[10][5] = piece.Piece6('6', 'white', 10, 5)
        self.board[10][6] = piece.Piece7('7', 'white', 10, 6)
        self.board[10][7] = piece.Piece8('8', 'white', 10, 7)
        self.board[10][8] = piece.Piece9('9', 'white', 10, 8)
        self.board[9][4] = piece.Piece0('0', 'white', 9, 4)

    # get a copy of the board (all pieces and their attributes copied as well)
    def get_copy(self):
        b = []

        for i in range(self.row_):
            col = []
            for j in range(self.column_):
                col.append(' ')

            b.append(col)

        for row in range(self.row_):
            for col in range(self.column_):
                if self.board[row][col] != ' ':
                    b[row][col] = deepcopy(self.board[row][col].get_copy())

        return deepcopy(b)
       # change the points of a piece depending on its colour
    def update_points(self):
        for row in self.board:
            for _piece in row:
                if _piece != ' ':
                    _piece.points = -1 * _piece.points if _piece.team == 'black' else _piece.points

    # depending on colour, the moves have to be negated as the teams face opposite directions
    def update_moves(self):
        for row in self.board:
            for _piece in row:
                if _piece != ' ':
                    for move in _piece.moves:
                        for i in range(len(move)):
                            if _piece.team == 'black':
                                move[i] = 0 - move[i]

  def display(self):
        columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        rows = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']

        print()

        for letter in columns:
            print('', letter, sep=' ', end='  ')
        print()

        for i in range(self.row_):
            print(rows[i], end=' ')

            for j in range(self.column_):
                p = '🙾' if self.board[i][j] == ' ' else self.board[i][j].symbol
                print('', p, sep=' ', end=' ')
            print()
            
  def in_range(self, row: int, col: int):
        if 0 <= row < self.size_ and 0 <= col < self.size_:
            return True
        return False

    # check if a particular cell is empty
    def is_cell_empty(self, row: int, col: int):
        if self.board[row][col] == ' ':
            return True
        return False

    def team_at_destination(self, _piece: piece.Piece, row: int, col: int) -> bool:
        if self.is_cell_empty(row, col):
            return False

        if self.get_piece(row, col).team == _piece.team:
            return True

        return False

    # check if there is a member of opposite team at destination
    def enemy_at_destination(self, _piece: piece.Piece, row: int, col: int):
        if self.is_cell_empty(row, col):
            return False

        if self.get_piece(row, col).team != _piece.team:
            return True

        return False
     # list of all allowed moves for this board
    def get_all_allowed_moves(self, team: str):
        allowed_moves = []
        for row in self.board:
            for _piece in row:
                if _piece != ' ':
                    if _piece.team == team:
                        allowed_moves += _piece.get_allowed_moves(self)

        return allowed_moves

    # list of (row, column) positions of every piece of the specified team
    def get_team_positions(self, team: str):
        positions = []

        for row in self.board:
            for _piece in row:
                if _piece != ' ':
                    if _piece.team == team:
                        pos = (_piece.row, _piece.col)
                        positions.append(pos)

        return positions

    # get a piece at a cell
    def get_piece(self, row: int, col: int):
        return self.board[row][col]

    # get the team of the piece at specified coordinates
    def get_team(self, row: int, col: int):
        if self.is_cell_empty(row, col):
            return None

        return self.board[row][col].team

    # get the name of a piece at specified string coordinates
    def get_piece_name(self, pos):
        row, col = extras.parse_position(pos)
        return self.board[row][col].name
