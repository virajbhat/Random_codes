door_name = [x for x in range(1,101)]
door_state = []
list_of_monkeys = [x for x in range(1,101)]
for x in range(1,101):
    door_state.append('Close')


door_dict =dict(zip(door_name, door_state))

for monkey in list_of_monkeys:
    for door in door_dict:
        if door%monkey == 0 and door_dict[door] == 'Close':
            door_dict[door] = 'Open'
        elif door%monkey == 0 and door_dict[door] == 'Open':
            door_dict[door] = 'Close'
        

print(door_dict)