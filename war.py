class Weapon:
    def __init__ (self, name, bullet):
        self.name = name
        self.bullet = bullet


class Warrior:
    def __init__(self, name, nationality, weapon, live):
        self.name = name 
        self.nationality = nationality
        self.weapon = weapon
        self.live = live
    def shot(self, warrior):
        warrior.live-= 1
        self.weapon.bullet -= 1


class War:
    def shoting(target, shooter):
        quentity = 0
        for i in range(500):
            target.shot(shooter)
            quentity += 1
            if shooter.live == 0:
                print("R.I.P.")
                break
            elif target.weapon.bullet == 0:
                print("recharge")
                target.weapon.bullet = quentity
                quentity = 0

tt = Weapon("TT",9)
revolver = Weapon("revolver", 7)
aka_47 = Weapon("aka 47", 30)
aka_47 = Weapon("aka 47", 30)
viserion = Weapon("dragon", 100)
jemas_bond = Warrior("Jemas Bond", "UAS", tt, 100)
rembo = Warrior("Rembo", "UAS", aka_47, 100)
daenerys_targaryen = Warrior("Daenerys Targaryen","Dragon Stone", viserion, 100)
tony_montana = Warrior("Tony Montana", "Italy", aka_47, 100)
thomas_shelby = Warrior("Thomas Shelby", "Gypsies", revolver, 100)
War.shoting(thomas_shelby, tony_montana)