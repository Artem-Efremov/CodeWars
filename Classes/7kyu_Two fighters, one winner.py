"""
Create a function that returns the name of the winner in a fight between two fighters.

Each fighter takes turns attacking the other and whoever kills the other first is victorious. Death is defined as having health <= 0.

Each fighter will be a Fighter object/instance. See the Fighter class below in your chosen language.

Both health and damagePerAttack (damage_per_attack for python) will be integers larger than 0. You can mutate the Fighter objects.

##Example:

  declareWinner(new Fighter("Lew", 10, 2), new Fighter("Harry", 5, 4), "Lew") => "Lew"

  // Python
  declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew") => "Lew"

  Lew attacks Harry; Harry now has 3 health.
  Harry attacks Lew; Lew now has 6 health.
  Lew attacks Harry; Harry now has 1 health.
  Harry attacks Lew; Lew now has 2 health.
  Lew attacks Harry: Harry now has -1 health and is dead. Lew wins.

##

Javascript

function Fighter(name, health, damagePerAttack) {
        this.name = name;
        this.health = health;
        this.damagePerAttack = damagePerAttack;
        this.toString = function() { return this.name; }
}

Python

class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack


"""


def declare_winner(f1, f2, first_attacker):
    i = {f1.name: 1, f2.name: 2}[first_attacker]     
    while f1.health > 0 and f2.health > 0:
        if i % 2:
            f2.health -= f1.damage_per_attack
        else:
            f1.health -= f2.damage_per_attack
        i += 1
    return f1.name if f2.health <= 0 else f2.name






from math import ceil
from operator import attrgetter


def declare_winner(fighter1, fighter2, first_attacker):
    fighter1.turns = ceil(fighter1.health / float(fighter2.damage_per_attack))
    fighter2.turns = ceil(fighter2.health / float(fighter1.damage_per_attack))
    if fighter1.turns == fighter2.turns:
        return first_attacker
    return max(fighter1, fighter2, key=attrgetter('turns')).name


















import random

# Example test cases

test.describe("Example test cases")

test.assert_equals(declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Lew"), "Lew")

test.assert_equals(declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Harry"),"Harry")

test.assert_equals(declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harry"),"Harald")

test.assert_equals(declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harald"),"Harald")

test.assert_equals(declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Jerry"), "Harald")
    
test.assert_equals(declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Harald"),"Harald")

# 200 Random test cases

def correct(fighter1, fighter2, first_attacker):
    SWITCH = {fighter1: fighter2,
              fighter2: fighter1}

    current_attacker = fighter1 if fighter1.name == first_attacker else fighter2

    while True:

        # Attack
        SWITCH[current_attacker].health -= current_attacker.damage_per_attack

        #Check if dead
        if SWITCH[current_attacker].health <= 0:
            return current_attacker.name

        #Change who the attacker is - time for revenge!
        current_attacker = SWITCH[current_attacker]

test.describe("200 Random test cases")

names = ["Willy", "Johnny", "Max",
             "Lui", "Marco", "Bostin",
             "Loyd", "Mark", "Cuban",
             "Lew", "Rocky", "Mario",
             "David", "Patrick", "Michael"]

for trial in range(200):
    name1 = random.choice(names)
    name2 = random.choice(names)
    while name1 == name2:
        name2 = random.choice(names)
    
    health1, damagePerAttack1 = random.randint(1,1000), random.randint(1,100)
    health2, damagePerAttack2 = random.randint(1,1000), random.randint(1,100)
    first = random.choice((name1, name2))
    
    test.assert_equals(declare_winner(Fighter(name1, health1, damagePerAttack1),
                                      Fighter(name2, health2, damagePerAttack2),
                                      first),
                        correct(Fighter(name1, health1, damagePerAttack1),
                                      Fighter(name2, health2, damagePerAttack2),
                                      first))
