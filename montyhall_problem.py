import random
import matplotlib.pyplot as plt

'''Here we are trying to get the answer of the world famous Monty Hall Problem
(There are goat behind 2 doors and car behind 1 door)'''

switch_wins=0
stay_wins=0
samples=10**6

def rem_door(choose_door,open_door):
    n1=[k for k in range(0,3) if ((k!=choose_door) and (k!=open_door))] #n1 has the door which is neither opened by Monty nor chosen by the person
    return n1[0]


for j in range(samples):
    Doors=['A','B','C']
    car_door=random.randint(0,2) #Car is behind Doors[car_door]
    choose_door=random.randint(0,2)

    if car_door==choose_door:
        n=[i for i in range (0,3) if i!=car_door] #n has the 2 Doors which Monty can open as both have goat
        open_door=int(random.choice(n)) #open_door generates random door which can be opened by Monty
        switch_door=rem_door(choose_door,open_door) #final_door depicts the door chosen after switching

    else:
        open_door=[i for i in range (0,3) if i!=choose_door and i!=car_door] #open_door has the door which would be opened by Monty as he can only open the door with goat
        switch_door=rem_door(open_door[0],choose_door) #final_door depicts the door chosen after switching

    if switch_door==car_door:
        switch_wins += 1
    else:
        stay_wins +=1

print(f"Switch Win Rate: {100 * switch_wins / samples:.2f}%")
print(f"Stay Win Rate: {100 * stay_wins / samples:.2f}%")

# Plot
labels = ['Switch', 'Stay']
values = [switch_wins / samples, stay_wins / samples]

plt.bar(labels, values, color=['green', 'red'])
plt.ylabel('Win Probability')
plt.title('Monty Hall Simulation (Switch vs Stay)')
plt.ylim(0, 1)
plt.grid(axis='y')
plt.show()


