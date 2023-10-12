inventory = {"arrow": 12, "gold coin": 42, "rope": 1, "torch": 6, "dagger": 1}


def displayInventory(inventory):
    totalItems = 0
    print("Inventory:")
    for name, number in inventory.items():
        print(str(number) + " " + name)
        totalItems += number

    print("total items = " + str(totalItems))


displayInventory(inventory)
