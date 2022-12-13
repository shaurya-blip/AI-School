# To print all pythagorean triplets from 1 to 20

print('Pythagorean triplets from 1 to 20 are: \n')

for x in range(1,20):
    for y in range(1,20):
        for z in range(1,20):
            if x**2+y**2==z**2:
                print(x,y,z)