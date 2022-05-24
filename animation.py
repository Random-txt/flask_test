from main_libs import *


class Animation:

    def __init__(self,doublependulum_list,fps,t,file):
        '''self.pendulum=Pendule(1.5,0.8,np.arange(0,10,0.01))'''
        self.fps = fps
        self.doublependulum_list = doublependulum_list                                               ### prend une liste de pendule qu'on va generer après
        self.y = [odeint(pendule.eqdif, pendule.y_in,pendule.t) for pendule in doublependulum_list]
        self.t = t
        self.dp = int(1/fps/0.01)
        self.file = file

    def make_plot(self,p ):                                                                   ## Trace les trajectoires et les objets 
        # Plot and save an image of the double pendulum configuration for time                ## de pendule à chaque instant p.
        # point p.
               

        fig, axe = plt.subplots()

        # Plot a trail of the m2 bob's position for the last trail_secs seconds.
        trail_secs = 10

        # This corresponds to max_trail time points.
        max_trail = int(trail_secs / 0.01)


        for pend, y in zip (self.doublependulum_list, self.y ):            

            th1 = y[:, 0]
            th2 = y[:, 1] 

            x1 = pend.l1*np.sin(th1)
            y1 = -pend.l1* np.cos(th1)

            x2 = x1 + pend.l2 * np.sin(th2)
            y2 = y1 - pend.l2 * np.cos(th2)

            r2 = 0.01*5+ 0.02*(pend.m2)
            r1 = 0.01*5+ 0.02*(pend.m1) # rayon des pendules

            # Le tracé sera divisé en ns segments et tracé comme une ligne .
            ns = 100

            s = max_trail // ns  

            for j in range(ns):
                imin = p - (ns-j)*s    
                if imin < 0:           
                    continue
                imax = imin + s + 1    
                alpha = (j/ns)**2
                # les tracés commecent en centre des pendules.
                axe.plot(x1[imin:imax], y1[imin:imax], c=pend.colour1, solid_capstyle='butt',
                        lw=2, alpha=alpha)
                axe.plot((x2[imin:imax]),(y2[imin:imax]),c=pend.colour2, solid_capstyle='butt', lw=2, alpha=alpha)

            



            axe.plot([0, x1[p] , x2[p]], [0, y1[p], y2[p]], lw=2, c=pend.rodcol)

            # Les cercles représentant le point d'ancrage de la tige 1, 
            # et les bobs 1 et 2 ou peuvent être interprétés comme les pendules
            
            c0 = Circle((0, 0), 0.05 / 2, fc='k', zorder=10)

            c1 = Circle((x1[p] , y1[p]), r1, fc=pend.colour1, ec=pend.colour1, zorder=10,
                        label="masse {}, longueur {} et l'angle {}".format(pend.m1, pend.l1, pend.theta1))

            c2 = Circle((x2[p], y2[p] ), r2, fc=pend.colour2, ec=pend.colour2, zorder=10,
                        label="masse {}, longueur {} et l'angle {}".format(pend.m2, pend.l2, pend.theta2))


            axe.add_patch(c0)
            axe.add_patch(c1)
            axe.add_patch(c2)



        

        axe.set_xlim((-pend.l1 - pend.l2 - r2-r1),(pend.l1 + pend.l2+r1+r2))      
        axe.set_ylim((-pend.l1 - pend.l2- r2-r1), (pend.l1 + pend.l2+r1+r2))
        axe.set_aspect('equal', adjustable='box')                            
        plt.axis('off')
        fig.savefig(self.file + '/_img{:04d}.png'.format(p // self.dp), dpi=144)     
        plt.clf()  ## clear figure
        plt.cla()  ## Clear axis

    def compiler(self):                                                             ## Le compiler genere et sauvegarde les images de makeplot() 
                                                                                    ## dans un dossier et à la fin produit un gif.                  
        
        # Make an image every di time points, corresponding to a frame rate of fps     

        for p in range(0, self.t.size, self.dp):
            print(p // self.dp, '/', self.t.size // self.dp)
            self.make_plot(p)

        gif_name = 'Double_Pendulum'+self.file
        file_list = glob.glob(self.file + '/*.png')  # Get all the pngs in the current directory
        
        clip = mpy.ImageSequenceClip(self.file, fps=self.fps)
        clip.write_gif('{}.gif'.format(gif_name), fps=self.fps)
    