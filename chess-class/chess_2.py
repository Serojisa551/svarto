class Board:
    def __init__(self, big):
        self.big = big
        self.big[6][0] = Pawn(Color.black)
        self.big[6][1] = Pawn(Color.black)
        self.big[6][2] = Pawn(Color.black)
        self.big[6][3] = Pawn(Color.black)
        self.big[6][4] = Pawn(Color.black)
        self.big[6][5] = Pawn(Color.black)
        self.big[6][6] = Pawn(Color.black)
        self.big[6][7] = Pawn(Color.black)

    def __repr__(self):
        res = ""
        for y in range(8):
            res += " ".join(map(str, self.big[y])) + "\n"
        return res


class Color:
    black = 0
    white = 1


class Figure:
    img = None

    def __init__(self,color):
        self.set_color(color)

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def __repr__(self):
        return self.img[1 if self.get_color == Color.white else 0]


class Pawn(Figure):
    img = ("♟", "♙")

    def get_moves(big, x, y):
        moves = []
        print(big[x][y])
        if big[x][y] != Color.black and y < 7 and big.get_color(x, y+1) != Color.black:
            moves.append([x, y+1])
            print("barev")
        return moves

board = [["◻", "◼"] * 4 for i in range(4)]
board1 = [["◼", "◻"] * 4 for i in range(4)]
big = []
for i in range(0, 4):
    big.append(board1[i])
    big.append(board[i])

big[1][0] = Pawn(Color.white)
big[6][0] = Pawn(Color.black)
big[6][1] = Pawn(Color.black)
big[6][2] = Pawn(Color.black)
big[6][3] = Pawn(Color.black)
big[6][4] = Pawn(Color.black)
big[6][5] = Pawn(Color.black)
big[6][6] = Pawn(Color.black)
big[6][7] = Pawn(Color.black)
# print(big[1][0].get_color(x, y+1))
print(Pawn.get_moves(big, 1, 0))
# print(big))