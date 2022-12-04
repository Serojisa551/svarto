class Board:
    def __init__(self, big):
        self.big = big
        self.big[7][3] = white_queen.get_u_number()
        self.big[7][4] = white_king.get_u_number()
        self.big[0][3] = black_queen.get_u_number()
        self.big[0][4] = black_king.get_u_number()
        self.big[7][2] = white_elephant_one.get_u_number()
        self.big[7][5] = white_elephant_two.get_u_number()
        self.big[0][2] = black_elephant_one.get_u_number()
        self.big[0][5] = black_elephant_two.get_u_number()
        self.big[7][1] = white_horse_one.get_u_number()
        self.big[7][6] = white_horse_two.get_u_number()
        self.big[0][1] = black_horse_one.get_u_number()
        self.big[0][6] = black_horse_two.get_u_number()
        self.big[7][0] = white_rook_one.get_u_number()
        self.big[7][7] = white_rook_two.get_u_number()
        self.big[0][0] = black_rook_two.get_u_number()
        self.big[0][7] = black_rook_one.get_u_number()
        self.big[6][0] = white_pawn_one.get_u_number()
        self.big[6][1] = white_pawn_two.get_u_number()
        self.big[6][2] = white_pawn_three.get_u_number()
        self.big[6][3] = white_pawn_four.get_u_number()
        self.big[6][4] = white_pawn_five.get_u_number()
        self.big[6][5] = white_pawn_six.get_u_number()
        self.big[6][6] = white_pawn_seven.get_u_number()
        self.big[6][7] = white_pawn_eight.get_u_number()
        self.big[1][0] = black_pawn_one.get_u_number()
        self.big[1][1] = black_pawn_two.get_u_number()
        self.big[1][2] = black_pawn_three.get_u_number()
        self.big[1][3] = black_pawn_four.get_u_number()
        self.big[1][4] = black_pawn_five.get_u_number()
        self.big[1][5] = black_pawn_six.get_u_number()
        self.big[1][6] = black_pawn_seven.get_u_number()
        self.big[1][7] = black_pawn_eight.get_u_number()

    def __repr__(self):
        res = ""
        for y in range(8):
            res += " ".join(map(str, self.big[y])) + "\n"
        return res


class Figure:
    def __init__(self, color, view, price, u_number):
        self.set_color(color)
        self.set_view(view)
        self.set_price(price)
        self.set_u_number(u_number)

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_view(self, view):
        self.__view = view

    def get_view(self):
        return self.__view

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_u_number(self, u_number):
        self.__u_number = u_number

    def get_u_number(self):
        return self.__u_number


# class Game:
#     def moves(a):
#         if a.get_view() == "pawn":
#             if a.get_color() == "white":


white_pawn_one = Figure("white", "pawn", 1, chr(9823))
white_pawn_two = Figure("white", "pawn", 1, chr(9823))
white_pawn_three = Figure("white", "pawn", 1, chr(9823))
white_pawn_four = Figure("white", "pawn", 1, chr(9823))
white_pawn_five = Figure("white", "pawn", 1, chr(9823))
white_pawn_six = Figure("white", "pawn", 1, chr(9823))
white_pawn_seven = Figure("white", "pawn", 1, chr(9823))
white_pawn_eight = Figure("white", "pawn", 1, chr(9823))
black_pawn_one = Figure("black", "pawn", 1, chr(9817))
black_pawn_two = Figure("black", "pawn", 1, chr(9817))
black_pawn_three = Figure("black", "pawn", 1, chr(9817))
black_pawn_four = Figure("black", "pawn", 1, chr(9817))
black_pawn_five = Figure("black", "pawn", 1, chr(9817))
black_pawn_six = Figure("black", "pawn", 1, chr(9817))
black_pawn_seven = Figure("black", "pawn", 1, chr(9817))
black_pawn_eight = Figure("black", "pawn", 1, chr(9817))
black_rook_one = Figure("black", "rook", 5, chr(9814))
black_rook_two = Figure("black", "rook", 5, chr(9814))
white_rook_one = Figure("white", "rook", 5, chr(9820))
white_rook_two = Figure("white", "rook", 5, chr(9820))
white_horse_one = Figure("white", "horse", 3, chr(9822))
white_horse_two = Figure("white", "horse", 3, chr(9822))
black_horse_one = Figure("black", "horse", 3, chr(9816))
black_horse_two = Figure("black", "horse", 3, chr(9816))
white_elephant_one = Figure("white", "elephant", 3, chr(9821))
white_elephant_two = Figure("white", "elephant", 3, chr(9821))
black_elephant_one = Figure("black", "elephant", 3, chr(9815))
black_elephant_two = Figure("black", "elephant", 3, chr(9815))
black_queen = Figure("black", "queen", 9, chr(9813))
white_queen = Figure("white", "queen", 9, chr(9819))
black_king = Figure("black", "knig", 10, chr(9812))
white_king = Figure("white", "knig", 10, chr(9818))

board = [["◻", "◼"] * 4 for i in range(4)]
board1 = [["◼", "◻"] * 4 for i in range(4)]
big = []
for i in range(0, 4):
    big.append(board1[i])
    big.append(board[i])

print(Board(big))
# print(Game.moves(white_pawn_one))
