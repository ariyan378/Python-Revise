day = ['sat','sun','monday','tues','wed','thu', 'fri']
temp = [21,23,26,21,27,25,29]

for day , temp in zip(day,temp):
    print(f'The Temp of the {day} is {temp}')