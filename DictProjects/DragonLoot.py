dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]

inventory = {"arrow": 12, "gold coin": 42, "rope": 1, "torch": 6, "dagger": 1}


def addToInventory(inventory, loot):
    for item in loot:
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory[item] = 1
    print(inventory)


print(inventory)
addToInventory(inventory, dragonLoot)
