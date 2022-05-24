from turtle import speed
from main_libs import *
from pendulum import *
from animation import *

'''
def rand_c():
    rx = 0.1*random.randint(0,10)
    ry = 0.1*random.randint(0,10)
    rz = 0.1*random.randint(0,10)

    return np.array([rx,ry,rz]) 

r_c1 = rand_c()
r_c2 = rand_c()


d1pendulum = Pendule(np.pi-0.001,np.pi-0.001,1.0,1.0,5.0,10.0,0.009,0,globaltime,'1',r_c1,r_c2,'k')
d2pendulum = Pendule(np.pi-0.001,np.pi-0.001,1.0,1.0,5.0,10.0,0.002,0,globaltime,'2',r_c1,r_c2,'k')
d3pendulum = Pendule(np.pi-0.001,np.pi-0.001,1.0,1.0,5.0,10.0,0,0,globaltime,'3',r_c1,r_c2,'k')

dp_list=[d1pendulum,d2pendulum,d3pendulum]

'''
list_of_pendulums = []
'''

length_of_first_pendulum  = float(input())
length_of_second_pendulum = float(input())

mass_of_first_pendulum  = float(input())
mass_of_second_pendulum = float(input())

angle_of_first_pendulum  = float(input())
angle_of_second_pendulum = float(input())

speed_of_first_pendulum  = float(input())
speed_of_second_pendulum = float(input())

'''


#string_color = int(input())



def generator(ask):
    for i in range(ask):
        print("Provide data for pendulum number {}".format(i))
        print("The length of the inner pendulum and the length of the outer pendulum respectively")
        length_of_first_pendulum  = float(input())
        length_of_second_pendulum = float(input())

        print("The mass of the inner pendulum and the mass of the outer pendulum respectively")
        mass_of_first_pendulum  = float(input())
        mass_of_second_pendulum = float(input())

        print("The initial angle of the inner pendulum and the initial angle of the outer pendulum in radians respectively")
        angle_of_first_pendulum  = float(input())
        angle_of_second_pendulum = float(input())

        print("The velocity of the inner pendulum and the velocity of the outer pendulum respectively")
        speed_of_first_pendulum  = float(input())
        speed_of_second_pendulum = float(input())

        print("color R G B")

        random_color=np.array([int(input()), int(input()), int(input())])
        
        list_of_pendulums.append(Pendule(angle_of_first_pendulum,angle_of_second_pendulum,length_of_first_pendulum,length_of_second_pendulum,
                                         mass_of_first_pendulum,mass_of_second_pendulum, speed_of_first_pendulum,speed_of_second_pendulum,globaltime,i,random_color,random_color,'k'))

print(generator(1))
print(list_of_pendulums)