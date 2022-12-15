class Board:
    def __init__(self, big, pawns):
        self.big = big
        index = -1
        element_one = 0
        for i in pawns[0]:  # TODO(
            index += 1
            if index == 1:
                self.big[6][element_one] = i.get_u_number()
            self.big[6][index] = i.get_u_number()
            if index == 7:
                index = -1
        for i in pawns[1]:
            index += 1
            if index == 1:
                self.big[1][element_one] = i.get_u_number()
            self.big[1][index] = i.get_u_number()  # )
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

    # @staticmethod
    # def check(board, walking_coordinates_y,walking_coordinates_x, element):
    #     total = board[walking_coordinates_y][walking_coordinates_x] not in element
    #     return total

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


class Check:
    @staticmethod
    def check_walking_coordinates(walking_coordinates, element):
        total = walking_coordinates not in element
        return total

    @staticmethod
    def check_img(location_element, element):
        total = location_element == element
        return total

    @staticmethod
    def check_coordinates(itr):
        for element in itr:
            if 0 > element or element > 7:
                raise IndentationError(
                    "You should not be right coordinates '{}'".format(element)
                )
        return True

    @staticmethod
    def check_tpye(itr):
        for element in itr:
            if type(element) != int:
                raise IndentationError(
                    "You should not be right coordinates '{}'".format(element)
                )
        return True


class Game:
    def walk(
        self,
        old_bard,
        location_y,
        location_x,
        walking_coordinates_y,
        walking_coordinates_x,
    ):  # TODO(
        if Check.check_coordinates(
            (location_y, location_x, walking_coordinates_y, walking_coordinates_x)
        ):
            if Check.check_tpye(
                (location_y, location_x, walking_coordinates_y, walking_coordinates_x)
            ):
                pass
        if Check.check_img(self.big[location_y][location_x], "♙"):
            if Check.check_walking_coordinates(
                self.big[walking_coordinates_y][walking_coordinates_x], "♔♕♖♗♘♙"
            ):
                self.big[walking_coordinates_y][walking_coordinates_x] = "♙"
                self.big[location_y][location_x] = old_bard[location_y][location_x]
                return self
        else:
            pass  # )


class Make:
    @staticmethod
    def make_pawn():
        tpl_name_pawn = (
            "white_pawn_one",
            "white_pawn_two",
            "white_pawn_three",
            "white_pawn_four",
            "white_pawn_five",
            "white_pawn_six",
            "white_pawn_seven",
            "white_pawn_eight",
            "black_pawn_one",
            "black_pawn_two",
            "black_pawn_three",
            "black_pawn_four",
            "black_pawn_five",
            "black_pawn_six",
            "black_pawn_seven",
            "black_pawn_eight",
        )
        set_white_pawn = set({})
        set_black_pawn = set({})
        for i in tpl_name_pawn:
            if i[0] == "w":
                i = Figure("white", "pawn", 1, chr(9823))
                set_white_pawn.add(i)
            else:
                i = Figure("black", "pawn", 1, chr(9817))
                set_black_pawn.add(i)
        return set_white_pawn, set_black_pawn

    @staticmethod
    def make_board():
        board = [["◻", "◼"] * 4 for i in range(4)]
        board1 = [["◼", "◻"] * 4 for i in range(4)]
        big = []
        for i in range(0, 4):
            big.append(board1[i])
            big.append(board[i])
        return big


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


board = Board(Make.make_board(), Make.make_pawn())
print(Game.walk(board, Make.make_board(), 1, 3, 3, 3))
