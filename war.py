class Weapon:
    def __init__(self, name, bullet):  # damage
        self.set_name(name)
        self.set_bullet(bullet)
        # self.damage = damage

    def set_bullet(self, bullet):
        self.__bullet = bullet
        if self.__name == "TT":
            if bullet > 7:
                print("shat")
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
        self.name = name
        self.nationality = nationality
        self.weapon = weapon
        self.live = live
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

    def git_live(self):
        return self.__live

    def shot(self, warrior):
        warrior.live -= 1  # self.damage
        self.weapon.set_bullet(self.weapon.get_bullet() - 1)


class War:
    def shoting(target, shooter):
        quentity = 0
        for i in range(500):
            target.shot(shooter)
            quentity += 1
            if shooter.live == 0:
                print("R.I.P.")
                break
            elif target.weapon.get_bullet() == 0:
                print("recharge")
                target.weapon.bullet = quentity
                quentity = 0


tt = Weapon("TT", 7)
revolver = Weapon("revolver", 7)
aka_47 = Weapon("aka 47", 30)
aka_47_2 = Weapon("aka 47", 30)
viserion = Weapon("dragon", 100)
jemas_bond = Warrior("Jemas Bond", "UAS", tt, 100)
rembo = Warrior("Rembo", "UAS", aka_47, 100)
daenerys_targaryen = Warrior(
    "Daenerys Targaryen", "Dragon Stone", viserion, 100)
tony_montana = Warrior("Tony Montana", "Italy", aka_47_2, 100)
thomas_shelby = Warrior("Thomas Shelby", "Gypsies", revolver, 100)

War.shoting(jemas_bond, tony_montana)
print(Warrior.number)