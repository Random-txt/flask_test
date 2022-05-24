from main_libs import *

class Pendule:
    def __init__(self, theta1, theta2,l1,l2,m1,m2,v1,v2,t,file,colour1,colour2,rodcol):
        self.theta1 = theta1
        self.theta2 = theta2
        self.t = t
        self.l1 = l1
        self.l2 = l2
        self.g = 9.81
        self.m1 = m1
        self.m2 = m2
        self.v1 = v1
        self.v2 = v2
        self.y_in = [self.theta1, self.theta2, self.v1, self.v2]
        self.y = odeint(self.eqdif,self.y_in,self.t)
        self.file = file
        self.colour1 = colour1
        self.colour2 = colour2
        self.rodcol = rodcol


    def eqdif(self,y,t):               # Methode intermediaire utilisé par ODEint pour sortir les sol dynamqiue de mvt
        theta1 = y[0]                   
        theta2 = y[1]
        theta1pt = y[2]
        theta2pt = y[3]
        g = self.g
        l1 = self.l1
        l2 = self.l2
        m1 = self.m1
        m2 = self.m2

        s1, s2 = np.cos(theta1 - theta2), np.sin(theta1 - theta2)

        theta12pt = (m2 * g * np.sin(theta2) * s1 - m2 * s2 * (l1 * theta1pt ** 2 * s1 + l2 * theta2pt ** 2)
                     - (m1 + m2) * g * np.sin(theta1)) / (l1 * (m1 + m2 * s2 ** 2))

        theta22pt = ((m1 + m2) * (l1 * theta1pt ** 2 * s2 - g * np.sin(theta2) + g * np.sin(theta1) * s1)
                     + m2 * l2 * theta2pt ** 2 * s2 * s1) / (l2 * (m1 + m2 * s2 ** 2))

        return theta1pt, theta2pt, theta12pt, theta22pt

    def energie(self):                                  # renvoie une liste qui contient les energies mecanique, cinetique et potentielle 
        theta1 = self.y[:, 0]
        theta2 = self.y[:, 1]
        theta1pt = self.y[:, 2]
        theta2pt = self.y[:, 3]

        g = self.g
        l1 = self.l1
        l2 = self.l2
        m1 = self.m1
        m2 = self.m2

        V = -(m1 + m2) * l1 * g * np.cos(theta1) - m2 * l2 * g * np.cos(theta2)
        T = 1/2 * m1 * (l1 * theta1pt) ** 2 + 0.5 * m2 * ((l1 * theta1pt) ** 2 + (l2 * theta2pt) ** 2 +
                                                          2 * l1 * l2 * theta1pt * theta2pt * np.cos(theta1 - theta2))
        M = T + V
        return [M, T, V]
    
    def motionplot(self):     
                                          # L'evolution de mvt de theta1(t) et theta2(t) 
        time = self.t

        fig= plt.figure(figsize=(8,8))
        plt.plot(time, self.y[:, 0], 'b', label='theta 1(t)')
        plt.plot(time, self.y[:, 1], 'g', label='theta 2(t)')
        plt.legend(loc='best')
        plt.xlabel('t')
        plt.grid()
        plt.show()

    def shift(self,t1, t2):                                        # Faire une translation temporelle de mvt de t1 à t2.
        plt.plot(t1, self.y[:, 0], 'dimgray', label='theta 1(t)')
        plt.plot(t1, self.y[:, 1], 'k', label='theta 2(t)')
        plt.plot(t2, self.y[:, 0], 'r', label='theta 1(t) decalé')
        plt.plot(t2, self.y[:, 1], 'c', label='theta 2(t) decalé')
        plt.legend(loc='best')
        plt.xlabel('t')
        plt.grid()
        plt.show()
    
    
    def tcompare(self,t1):                                         # Permet de mettre en evidence le mvt chaotique (l'impredictibilité, l'irregularité 
                                                                   #                                                      et la sensibilite aux CI)
        

        t_n=self.t+t1
        n=np.where(self.t==t1)

        theta1_n=self.y[n[0][0],0]

        theta2_n=self.y[n[0][0],1]
        v1_n=self.y[n[0][0],2]
        v2_n=self.y[n[0][0],3]

        pend=Pendule(theta1_n,theta2_n,self.l1,self.l2,self.m1,self.m2,v1_n,v2_n,t_n,self.file,self.colour1,self.colour2,self.rodcol)

        plt.plot(t_n, pend.y[:, 0], 'r', label='theta_n 1(t)')
        plt.plot(t_n, pend.y[:, 1], 'c', label='theta_n 2(t)')
        plt.plot(self.t, self.y[:, 0], 'b', label='theta 1(t)')
        plt.plot(self.t, self.y[:, 1], 'g', label='theta 2(t)')

        plt.legend(loc='best')
        plt.xlabel('t')
        plt.grid()
        plt.show()



        x1_n = self.l1 * np.sin(pend.y[:, 0])
        y1_n = -self.l1 * np.cos(pend.y[:, 0])

        x2_n = x1_n + self.l2 * np.sin(pend.y[:, 1])
        y2_n = y1_n - self.l2 * np.cos(pend.y[:, 1])

        theta1 = self.y[:, 0]
        theta2 = self.y[:, 1]

        x1 = self.l1 * np.sin(theta1)
        y1 = -self.l1 * np.cos(theta1)

        x2 = x1 + self.l2 * np.sin(theta2)
        y2 = y1 - self.l2 * np.cos(theta2)


        fig= plt.figure(figsize=(16,16))

        plt.polar(pend.y[:, 1], np.sqrt(x2_n ** 2 + y2_n** 2),c = self.colour2,
                  label="masse {}, longueur {} et l'angle {}".format(self.m2, self.l2, theta2_n))
        
        plt.polar(pend.y[:, 0], np.sqrt(x1_n ** 2 + y1_n ** 2),c = self.colour1,
                  label="masse {}, longueur {} et l'angle {}".format(self.m1, self.l1, theta1_n))
        
        plt.polar(theta1, np.sqrt(x1 ** 2 + y1 ** 2),
          label="mvt initial,masse {}, longueur {} et l'angle {}".format(self.m1, self.l1, self.y_in[0]))
        
        plt.polar(theta2, np.sqrt(x2 ** 2 + y2 ** 2),
                  label="mvt initial,masse {}, longueur {} et l'angle {}".format(self.m2, self.l2, self.y_in[1]))
        plt.legend(loc='upper right')
        plt.savefig('Polar plot compare ')
        plt.show()

   
    
    def energieplot(self):                                        # l'evolution energetique du systeme, pour verifier la coherence physique
        time = self.t                                            
        MTV = self.energie()

        plt.plot(time, MTV[0], 'r', label='Energie Mecanique')
        plt.plot(time, MTV[1], 'b', label='Energie cinetique')
        plt.plot(time, MTV[2], 'g', label='Energie potentiel')
        plt.legend(loc='best')
        plt.xlabel('t')
        plt.grid()
        plt.show()


    def polplot(self):                                                        ## On trace une graphe polaire
                                                                              ## pour bien voir le trajectoire du systeme.
        theta1 = self.y[:, 0]                                                 ## On peut observer le trajectoire avec le trail après dans l'animation
        theta2 = self.y[:, 1]

        x1 = self.l1 * np.sin(theta1)
        y1 = -self.l1 * np.cos(theta1)

        x2 = x1 + self.l2 * np.sin(theta2)
        y2 = y1 - self.l2 * np.cos(theta2)

        

        fig, axe = plt.subplots(figsize=(8,8))

        plt.polar(theta2, np.sqrt(x2 ** 2 + y2 ** 2),c = self.colour2,
                  label="masse {}kg, longueur {}m et l'angle {} rad".format(self.m1, self.l1, self.y_in[0]))
        plt.polar(theta1, np.sqrt(x1 ** 2 + y1 ** 2),c = 'k',
                  label="masse {}kg, longueur {}m et l'angle {} rad".format(self.m2, self.l2, self.y_in[1]))
        plt.legend(loc='best')
        plt.savefig('Polar plot of the Pendulum'+self.file,transparent=True)
        plt.show()








