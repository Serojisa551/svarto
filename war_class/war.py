class Weapon:
    def __init__(self, name, bullet, damage):
        self.set_name(name)
        self.set_bullet(bullet)
        self.set_damage(damage)

    def set_damage(self, damage):
        self.__damage = damage

    def get_damage(self):
        return self.__damage

    def set_bullet(self, bullet):
        self.__bullet = bullet
        if self.__name == "TT":
            if bullet > 100:
                print("shat")
                return
            else:
                pass

    def get_bullet(self):
        return self.__bullet

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Warrior:
    number = 0

    def __init__(self, name, nationality, weapon, live):
        self.set_name(name)
        self.set_nationality(nationality)
        self.set_weapon(weapon)
        self.set_live(live)
        Warrior.number += 1

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_nationality(self, nationality):
        self.__nationality = nationality

    def get_nationality(self):
        return self.__nationality

    def set_weapon(self, weapon):
        self.__weapon = weapon

    def get_weapon(self):
        return self.__weapon

    def set_live(self, live):
        self.__live = live

    def get_live(self):
        return self.__live

    def shot(self, warrior):
        warrior.set_live(self.get_live() - warrior.get_weapon().get_damage())
        warrior.get_weapon().set_bullet(warrior.get_weapon().get_bullet() - 1)
        # self.set_live(self.get_live() - warrior.get_weapon().get_damage())
        # warrior.get_weapon().set_bullet(warrior.get_weapon().get_bullet() - 1)


class War:
    def __init__(self, weapon, warrior):
        self.set_weapon(weapon)
        self.set_warrior(warrior)

    def set_warrior(self, warrior):
        self.__warrior = warrior

    def get_warrior(self):
        return self.__warrior

    def set_weapon(self, weapon):
        self.__weapon = weapon

    def get_weapon(self):
        return self.__weapon

    def shoting(target, shooter):

        quentity = 0
        for i in range(500):

            target.shot(shooter)
            # print("shooter.get_live()",shooter.get_live())
            # print("shooter.get_warrior().get_naem()",  )
            quentity += 1
            if shooter.get_live() < 1:
                # print("shooter.get_live()",shooter.get_live())
                print("R.I.P.")
                break
            elif shooter.get_weapon().get_bullet() == 0:
                # print("quentity", quentity)
                print("recharge")
                shooter.get_weapon().set_bullet(quentity)
                quentity = 0


tt = Weapon("TT", 5, 15)
revolver = Weapon("revolver", 7, 25)
aka_47 = Weapon("aka 47", 30, 10)
aka_47_2 = Weapon("aka 47", 30, 10)
viserion = Weapon("dragon", 1, 100)
jemas_bond = Warrior("Jemas Bond", "UAS", tt, 100)
rembo = Warrior("Rembo", "UAS", aka_47, 100)
daenerys_targaryen = Warrior("Daenerys Targaryen", "Dragon Stone", viserion, 100)
tony_montana = Warrior("Tony Montana", "Italy", aka_47_2, 100)
thomas_shelby = Warrior("Thomas Shelby", "Gypsies", revolver, 100)

War.shoting(jemas_bond, thomas_shelby)
# print(Warrior.number)
