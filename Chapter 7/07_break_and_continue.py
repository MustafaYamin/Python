# break

# lets say I want to exit the loop after a certain value what we can do is

for i in range(100):
    if(i == 35):
        break   # This condition says that if the value of i get to 35 break the loop/ exit the loop right away
    print(i)

print('---------------------------------------------')

# continue

# lets say I want to skip a certain value fron the loop but don't want to break the loop

for i in range(100):
    if(i == 35):
        continue   # This condition says that if the value of i get to 35 skip that value and mov to the rest of the code
    print(i)