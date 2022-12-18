class String:
    def get_str():
        return "hello"


class Integer:
    def get_int():
        return 123

class Adapter(Integer):
    def cast(self):
        return str(self.get_int())

class Main:
    def get_result(obj):
        print("result:" + obj)


if __name__ == "__main__":
    obj = String.get_str()
    obj1 = Adapter.cast(Integer)
    Main.get_result(obj1)