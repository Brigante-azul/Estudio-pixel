# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 18:02:13 2021

@author: Azul
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt 

cap=cv2.VideoCapture('VID_20210329_124815.mp4')
frame_rate=cap.get(5)
#%%
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH )
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT )
fps =  cap.get(cv2.CAP_PROP_FPS)
print( length, width, height, fps )
#%%
#voy a plotear una imagen con el cuadrado que quiero recortar 
x1, x2, y1, y2= 950, 1100, 150, 300
d=4#ancho de linea
color=(0,255,0)

cap.set(1, 50) #fijo el frame 50
ret, frame=cap.read()#lo leo 
frame[y1:y1+d,x1:x2], frame[y2:y2+d,x1:x2], frame[y1:y2, x1:x1+d], frame[y1:y2, x2:x2+d]=color, color, color, color #creo el cuadro 
cv2.imshow('frame', frame)

#selecciono un pixel
pixel_x, pixel_y=1100, 200
cap.set(1, 50) #fijo el frame 50
ret, frame=cap.read()#lo leo 
frame[pixel_y-2:pixel_y+2,pixel_x-2:pixel_x+2]=color
cv2.imshow('frame', frame)
#%%
R_t=[]
G_t=[]
B_t=[]

for i in range(0, length):
    cap.set(1, i)
    ret, frame=cap.read()
    R, G, B=frame[pixel_y,pixel_x, 0], frame[pixel_y,pixel_x, 1], frame[pixel_y,pixel_x, 2]
    R_t.append(R)
    G_t.append(G)
    B_t.append(B)
    print(i)
    
#%%
intensidad = np.loadtxt('gris.txt', delimiter=' ')

#%%
lista=[R_t, G_t, B_t]
for i in lista:
    plt.figure()
    plt.hist(i)
    plt.ylabel('Cantidad de pixeles',fontsize=15)
    plt.xlabel('Intensidad', fontsize=15)
    plt.legend()    
#%%
#histaagrama grises 
plt.figure()
plt.hist(intensidad)
plt.ylabel('Cantidad de pixeles',fontsize=15)
plt.xlabel('Intensidad gris', fontsize=15)
plt.legend()
    
#%%
#intensidad en funcion del tiempo
duracion=length/30
t=np.linspace(0, duracion, length)
for i in lista:
    plt.figure()
    plt.plot(t, i, 'o-')
    plt.xlabel('Tiempo [seg]',fontsize=15)
    plt.ylabel('Intensidad ', fontsize=15)
    plt.legend()
#%%
cap.set(1, 50)
ret, frame=cap.read()
cv2.imshow('frame', frame[:,:,1])





    