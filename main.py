import random
import time
import json
import math
import sys
import os

saveFile = open('save.json')
save = json.load(saveFile)

items = ["Stone","Stone","Stone","Stone","Stone","Stone","Stone","Coal","Coal","Coal","Coal","Coal","Coal","Iron","Iron","Iron","Iron","Gold","Gold","Gold", "Diamond"]
inventory = save["inventory"]
itemamt = [1, 1, 1, 1, 2, 2]
money = save["money"]
itemcapacity = save["itemcapacity"]
miningtime = save["miningtime"]

data = {
    "name": "",
    "money": money,
    "inventory": inventory,
    "itemcapacity": itemcapacity,
    "miningtime": miningtime
}

def showInventory():
    global inventory
    global money
    os.system("cls")
    totalVal = 0
    counter = 0
    inv = sorted(inventory)
    for x in range(len(inventory)):
        print(inv[counter] + " - $" + str(getItemPrice(inv[counter])))
        totalVal += getItemPrice(inv[counter])
        counter += 1
    print("\nTotal Inventory Value: $" + str(totalVal) + "\n\n[1] Sell All\n[2] Back\n")
    choice = input("Choice: ")
    if choice == "1":
        money += totalVal
        inventory = []
    if choice == "2":
        main()

def getItemPrice(item):
    if item == "Stone":return 2
    if item == "Coal":return 5
    if item == "Iron":return 15
    if item == "Gold":return 30
    if item == "Diamond":return 75
    
def upgrades():
    global itemcapacity
    global miningtime
    global money
    capacityIncreaseCost = itemcapacity*25
    speedIncreaseCost = 100-miningtime*30
    os.system("cls")
    print("$"+str(math.trunc(money)))
    print("\n[1] Increase mining speed by 0.2 seconds | $"+str(math.trunc(speedIncreaseCost)))
    print("[2] Increase Item Capacity by 1 | $"+str(math.trunc(capacityIncreaseCost)))
    print("[3] Exit")
    choice = input("\nChoice: ")
    if choice == "1" and money >= speedIncreaseCost:
        money -= speedIncreaseCost
        miningtime -= 0.2
        os.system("cls")
        print("Mining speed has been increased!")
        time.sleep(1.5)
        upgrades()
    if choice == "2" and money >= capacityIncreaseCost:
        money -= capacityIncreaseCost
        itemcapacity += 1
        os.system("cls")
        print("Item Capacity has been increased!")
        time.sleep(1.5)
        upgrades()
    if choice == "3":main()

def mine():
    global itemcapacity
    global inventory
    global items
    if len(inventory) < itemcapacity:
        if len(inventory) == itemcapacity - 1:
            os.system("cls")
            print("Mining.")
            time.sleep(miningtime/3)
            os.system("cls")
            print("Mining..")
            time.sleep(miningtime/3)
            os.system("cls")
            print("Mining...")
            time.sleep(miningtime/3)
            os.system("cls")
            print("Done!\n")
            item = random.choice(items)
            print(item + " - $" + str(getItemPrice(item)))
            inventory.append(item)
            input("\nPress Enter to continue...")
            main()
        else:
            os.system("cls")
            print("Mining.")
            time.sleep(miningtime/3)
            os.system("cls")
            print("Mining..")
            time.sleep(miningtime/3)
            os.system("cls")
            print("Mining...")
            time.sleep(miningtime/3)
            os.system("cls")
            print("Done!\n")
            for x in range(random.choice(itemamt)):
                item = random.choice(items)
                print(item + " - $" + str(getItemPrice(item)))
                inventory.append(item)
            input("\nPress Enter to continue...")
            main()
    else:
        os.system("cls")
        print("Inventory is full")
        time.sleep(2)
        main()

def main():
    global itemcapacity
    global miningtime
    global money
    os.system("cls")
    print("PyMiner\n\n"+"$"+str(math.trunc(money))+"\n\nItem Capacity: "+str(itemcapacity)+"\nMining Time: "+str(miningtime)+"\n\n[1] Go Mining\n[2] Inventory\n[3] Upgrades\n[4] Exit\n")
    choice = input("Choice: ")
    if choice == "1":mine()
    if choice == "2":showInventory()
    if choice == "3":upgrades()
    if choice == "4":
        data["name"] = save["name"]
        data["money"] = money
        data["inventory"] = inventory
        data["itemcapacity"] = itemcapacity
        data["miningtime"] = miningtime
        with open('save.json', 'w') as save_file:json.dump(data, save_file)
        sys.exit()
    else:main()


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(.4/10)

def welcome():
    global save
    slowprint("Welcome to PyMiner, What's your name? ")
    name = input("")
    data["name"] = name
    with open('save.json', 'w') as save_file:
        json.dump(data, save_file)
    slowprint("Hello " + data["name"] + "!")
    time.sleep(2)
    main()

if save["name"] == "":welcome()
else:
    print("Welcome back " + save["name"] + "!")
    time.sleep(2)
    main()