ornament_set = 2
tree_skirt = 5
tree_arlands = 3
tree_lights = 15

quantity = int(input())
days = int(input())
budget = 0
crist_spirit = 0

if days % 2 == 0:
    budget += ornament_set * quantity
    crist_spirit += 5
if days % 3 == 0:
    pass
