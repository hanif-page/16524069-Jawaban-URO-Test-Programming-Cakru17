# markdown live preview
# https://dillinger.io/

import random
from time import sleep
from modules.clearAndLoading import Loading, Typing

# loading animation object
clearLoad = Loading(0, 3, 0.3)

class Robot:
    def __init__(self, name, health, attackPowerRange):
        self.name = name
        self.health = health
        self.attackPowerRange = attackPowerRange

    def showSpecification(self):
        # code
        clearLoad.loadingAnimation()

        print("Specs:")

        print(f"Name: {self.name}, Health: {self.health}, Attack Power Range: {self.attackPowerRange}")

    def upgradeShield(self):
        # code
        clearLoad.loadingAnimation()

        self.health += 5

        print(f"Upgraded Shield Robot {self.name}, +{self.health} health")

    def increaseStrenth(self):
        # code
        clearLoad.loadingAnimation()

        self.attackPowerRange[0] += 3
        self.attackPowerRange[1] += 2

        print(f"Upgraded Attack Robot {self.name}, Min Attack: {self.attackPowerRange[0]}, Max Attack: {self.attackPowerRange[1]}")


class Battle: 
    def __init__(self, robot1, robot2):
        self.robot1 = robot1 
        self.robot2 = robot2

    def start_fight(self):
        clearLoad.loadingAnimation()

        # assume robot1 attack first
        print("Fight Start!")
        print()

        while (self.robot1.health > 0 and self.robot2.health > 0):

            # robot1 attack robot2
            attack1 = random.randrange(self.robot1.attackPowerRange[0], self.robot1.attackPowerRange[1])
            self.robot2.health -= attack1
            print(f"Robot {self.robot2.name} -{attack1} health (Remaining health: {self.robot2.health})")
            print()

            # robot2 attack robot1
            attack2 = random.randrange(self.robot2.attackPowerRange[0], self.robot2.attackPowerRange[1])
            self.robot1.health -= attack2
            print(f"Robot {self.robot1.name} -{attack2} health (Remaining health: {self.robot1.health})")
            print()

        if self.robot1.health <= 0:
            print(f"Robot {self.robot1.name} Defeated")
            print(f"Robot {self.robot2.name} WIN")

        if self.robot2.health <= 0:
            print(f"Robot {self.robot2.name} Defeated")
            print(f"Robot {self.robot1.name} WIN")
        
        print("\nBattle Finished\n")

        # back to the main screen
        next = input("Press ENTER to return")
        if next == "":
            Game().start_game()
        else:
            exit()
class Game:
    def __init__(self, items=[]):
        self.l = items # the Game class didn't require any argument because it's a general object to start the game, or adding a new robot

    @staticmethod
    def add_robot():
        clearLoad.loadingAnimation()

        robotName = input("Robot Name : ")
        robotHealth = int(input("Robot Health : "))
        robotMinAttack = int(input("Robot Minimal Attack Damage : "))
        robotMaxAttack = int(input("Robot Maximal Attack Damage : "))
        
        # saving robot data
        robotsList.append(Robot(robotName, robotHealth, [robotMinAttack, robotMaxAttack]))

        # print(robotsList)

        print(f"\nRobot {robotName} added!")

        sleep(1)        

        Game().start_game()

    @staticmethod
    def display_robot():

        clearLoad.loadingAnimation()

        if len(robotsList) == 0:
            print("Please add new robot first!")

            sleep(1)

            Game().start_game()
        else:
            for i in range(0, len(robotsList)):
                # print(i)
                print(f"{i+1}. Robot Name: {robotsList[i].name}\nRobot Health: {robotsList[i].health}\nRobot Damage Attack Range: {robotsList[i].attackPowerRange[0]}-{robotsList[i].attackPowerRange[1]}")
                print()


    def start_game(self):
        clearLoad.loadingAnimation()

        frontScreen = """
        Battle of Robot by Hanif

        1. Add Robot
        2. Display Robot
        3. Start a Fight
        4. Exit
        
        (Input the number you want to continue)
"""
        print(frontScreen)
        choice = int(input(">> "))
        print()

        if choice == 1:
            self.add_robot()
        elif choice == 2:
            self.display_robot()

            next = input("Press ENTER to return")
            if next == "":
                Game().start_game()
            else:
                exit()
        elif choice == 3:
            
            if len(robotsList) < 2:
                clearLoad.loadingAnimation()

                print("Please add more than one robot first!")

                sleep(1)

                Game().start_game()
            else:
                self.display_robot()
                print()
                robot1 = robotsList[int(input("Pick robot 1 (input its number) = ")) - 1]
                robot2 = robotsList[int(input("Pick robot 2 (input its number) = ")) - 1]

                battle = Battle(robot1, robot2)

                # starting the fight
                battle.start_fight()
        elif choice == 4:
            exit()
        else:
            print("Please only input the available option!")
            print()
            sleep(1)
            Game().start_game()

# for robot in robotsList:
#     if robot.name == "B":
#         print(robot.name)

# robotsList = [Robot("Putra", 100, [10, 15]), Robot("Jalinda", 200, [10, 12])]
robotsList = []

if __name__ == "__main__":
    Game().start_game()

# CREATE A CLEAR AND LOADING ANIMATION FOR THIS PROGRAM!