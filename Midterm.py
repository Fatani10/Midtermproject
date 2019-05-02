# -*- coding: utf-8 -*-
"""
Created on Wed May 1 14:24:22 2019

@author: sarifuddin awae
"""
import numpy as np
import matplotlib.pyplot as plt
import os
import os.path

Insert_airfoil = str(input('Write the name of airfoil '))
      
#calling airfoil data in text file 
directory = os.getcwd()
if os.path.isfile(Insert_airfoil+'.txt') == False:
    print('ERROR')
else:
    print('Yes, It is')
        

#100 Airfoils selected
Airfoils_Name = ['AG03', 'AG04', 'AG08', 'AG09', 'AG10', 'AG11', 'AG12', 'AG13', 'AG14', 'AG16', 'AG17', 'AG18'
                 , 'ESA40', 'GLENMARTIN2', 'HAWKER37', 'LC141', 'NACA0009', 'NACA0011', 'NACA0012', 'NACA2414'
                 , 'NACA64108', 'AG44CT', 'AG455CT', 'AG45C', 'AG45CT', 'AH21-7', 'NACA66021', 'NACA-M1'
                 , 'NACA-M10', 'NACA-M11', 'NACA-M12', 'NACA-M27', 'NPL1372', 'NPL9615', 'NPL9626', 'NPL9627', 'RAF32'
                 , 'OA206', 'AH88K130', 'AH88K136', 'AH80136', 'OA206', 'OA212', 'OAF095', 'OAF102', 'OAF117'
                 , 'OAF128', 'OAF139', 'HH02', 'GEMINI','2032c', 'cast102', 'e171', 'e554','e557', 'e1212mod' 
                 , 'eh1590' , 'eh2070' , 'fx84w218' , 'fx6617a2' , 'fx049915' , 'fx60100', 'fx63120','fx63143'
                 , 'giiig', 'glennmartin2' , 'glennmartin3', 'naca1410','naca2410' , 'naca2421', 'naca4415','naca16006'
                 ,'naca16018' , 'naca643218','naca643418','naca644221' ,'naca651212' , 'naca651412' , 'naca654221'
                 ,'naca654421a05','naca663418','nacam6','p51htip','pfcm','psu94097','r140sm','rae100','rae5212','s1223rtl','s2046'
                 ,'s2055','s3002','s3016','usa25','usa27','usa31','usa50','v43012','waspsm','ys930']

#define as a list
x_indicies = 0
y_indicies = 0
x_normalized = []
y_normalized = []
plotX = []
plotY = []
mc = [] #mean chamber
x_mc = [] 
a = []
b = []
teta = [1]


xydatas = np.loadtxt(Insert_airfoil+'.txt', dtype=float);
x_coordinates = xydatas[:-1, 0]
y_coordinates = xydatas[:-1, 1]


#compute the points that needed for each airfoil
for loop, item in enumerate(range(0,1)):
    while(xydatas[x_indicies,0] != 99):
        plotX = np.append(plotX, xydatas[x_indicies,0])
        plotY = np.append(plotY, xydatas[y_indicies,1])
        y_indicies = y_indicies+1
        x_indicies = x_indicies+1

    print("Points X", x_indicies)
    print("Points Y", y_indicies)

#part a nomalization of an airfoil   
    for loop, item in enumerate(plotY):
        if(xydatas[0, 0] < int(1)):
            if(plotY.size % 2 != 0):
                if(loop == int((plotY.size + 1)/2)):
                    break
                y_normalized = np.append(y_normalized, (item))
                y_normalizedorm = y_normalized[::-1]
                for loop, item in enumerate(y_normalizedorm):
                    if(item < 2):
                        plotY[loop] = item
                        
    for loop, item in enumerate(plotY):
        if(xydatas[0, 0] < int(1)):
            if(plotY.size % 2 == 0):
                if(loop == int(plotY.size/2)):
                    break
                y_normalized = np.append(y_normalized, (item))
                y_normalizedorm = y_normalized[::-1]
                for loop, item in enumerate(y_normalizedorm):
                    if(item < 2):
                        plotY[loop] = item
        
    for loop, item in enumerate(plotX):   
        if(xydatas[0, 0] < int(1)):
            if(plotX.size % 2 != 0):
                if(loop == int((plotX.size + 1)/2)):
                    break
                x_normalized = np.append(x_normalized, (item))
                x_normalizedorm = x_normalized[::-1]
                for loop, item in enumerate(x_normalizedorm):
                    if(item < 2):
                        plotX[loop] = item
                        
    for loop, item in enumerate(plotX):
        if(xydatas[0, 0] < int(1)):
            if(plotX.size % 2 == 0):
                if(loop == int(plotX.size/2)):
                    break
                x_normalized = np.append(x_normalized, (item))
                x_normalizedorm = x_normalized[::-1]
                for loop, item in enumerate(x_normalizedorm):
                    if(item < 2):
                        plotX[loop] = item    
                        
#part b   
#calculate mean camber and chordline       
    for loop, item in enumerate(plotX):
        if(loop == int(plotX.size/2)):
            break
        x_mc = np.append(x_mc,(item))

    for loop, item in enumerate(plotY):
        if(loop == int(plotY.size/2)):
            break
        mc = np.append(mc,(plotY[loop]+plotY[(plotY.size-1-loop)])/2)
        x = [0, 1]
        y = [0, 0]

    
#calculate a max thickness and its position     
    for loop, item in enumerate(plotY):
        line_y = [np.max(plotY), np.min(plotY)]
        line_x = [plotX[plotY.argmax()], plotX[plotY.argmax()]]
    
    
#part c
#calculate the panel #20 panels
    panel = 0
    while panel <= plotX.size-1:
        a = np.append(a,plotX[panel])
        b = np.append(b,plotY[panel])
        panel = panel + plotX.size//40
    for loop, item in enumerate(range(0,b.size-1)):

        DY = b[loop+1]-b[loop] 
        DX = a[loop+1]-a[loop]
        M1 = DY/DX
        M2 = -1/M1
        teta = np.append(teta, (np.arctan(M2)))
        u = np.cos(teta)
        v = np.sin(teta)
        
#Define kutta condition
    def kutta_condition(a,b):
        xu = []
        yu = []
        for loop, item in enumerate(b):
            if(loop == int(1)):
                break
            dyu = b[loop+1]-b[loop]
            dxu = a[loop+1]-a[loop]
            m1u = dyu/dxu
        n = a[::-1]
        m = b[::-1]
        for i in range(0, 2):
            xu = np.append(xu, n[i])
            yu = np.append(yu, m[i])
        for i, item in enumerate(xu):
            if(i == int(1)):
                break
            dyl = yu[i]-yu[i+1]
            dxl = xu[i]-xu[i+1]
            m1l = dyl/dxl
            if(abs(m1u) == abs(m1l)):
                condition = print('It is pointed')
            else:
                condition = print('It is cusped')
            return condition
        
#Combined everything here
    plt.figure(figsize=(10,5))
    plt.xlabel('x coordinates', fontsize=16)
    plt.ylabel('y coordinates', fontsize=16)
    plt.ylim(-0.15, 0.15)
    plt.grid()
    plt.title(Insert_airfoil) #put a title of each airfoil
    plt.plot(plotX, plotY, label='Upper and Lower Surface',color='red')
    plt.plot(x, y, label='Chord Line' , color = 'orange' )
    plt.plot(line_x, line_y, label='Maximum Thickness' , color = 'green')
    plt.plot(x_mc, mc, label='Mean Camber Line', color = 'blue')
    plt.legend(loc='best')
    plt.quiver(a,b,u,v)
    plt.plot(a,b, 'o')
    kutta_condition(a,b)  
    plt.show()  
    mc = []
    x_mc = []
    y_normalized = []
    x_normalized = []

        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
