def create_inventory(list):
    mapa = dict()
    for item in list:
        if item in mapa:
            mapa[item] += 1
        else:
            mapa[item] = 1
    return mapa

def add_items(inventory, items):
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory

def decrement_items(inventory, items):
    for item in items:
        if item in inventory:
            inventory[item] -= 1
            if inventory[item] < 1:
                inventory[item] = 0
        else:
            inventory[item] = 0
    return inventory

def remove_item(inventory, item):
    if item in inventory:
        del inventory[item]
    else:
        inventory
    return inventory

def list_inventory(inventory):
    tup = []
    for clave, valor in inventory.items():
        if valor > 0:
            tup.append((clave, valor))
    return tup

