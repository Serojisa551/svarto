class Decorator:
    @staticmethod
    def decorator(f):
        def inner():
            print("start decorator...")
            f()
            print("finish decorator...")

        return inner


class Hello(Decorator):
    @staticmethod
    def hW():
        print("Hello World")


hw = Decorator.decorator(Hello.hW)
hw()
