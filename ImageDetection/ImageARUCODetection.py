import cv2
import cv2.aruco as aruco
import numpy as np
import math
import os

def findAruco(img,markerSize=5,totalMarkers=1000,draw=True):
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    key=getattr(aruco,f'DICT_{markerSize}X{markerSize}_{totalMarkers}')
    arucoDict=aruco.Dictionary_get(key)
    arucoParam=aruco.DetectorParameters_create()
    bboxes,ids,rejected=aruco.detectMarkers(imgGray,arucoDict,parameters=arucoParam)
    return [bboxes,ids]

def point(image,x,y,bl,gr,re):
    cv2.circle(image,(int(x),int(y)),6,(bl,gr,re),thickness=-1)

def lines(image,x1,y1,x2,y2,bl,gr,re):
    cv2.line(image,(int(x1),int(y1)),(int(x2),int(y2)),(bl,gr,re),thickness=3)

def Mark_ArUco():
    img=cv2.VideoCapture(0)
    while True:
        isTrue,cap=img.read()
        arucofound=findAruco(cap)
        cv2.imshow("image",cap)
    # cap=cv2.imread("test_image2.png")
    # arucofound=findAruco(cap)
        t=0
        for Ar in arucofound[0]:
            
            Tlx=int(Ar[0][0][0])
            Tly=int(Ar[0][0][1])
            Trx=int(Ar[0][1][0])
            Try=int(Ar[0][1][1])
            Brx=int(Ar[0][2][0])
            Bry=int(Ar[0][2][1])
            Blx=int(Ar[0][3][0])
            Bly=int(Ar[0][3][1])
            cenx=int((Tlx+Brx)*0.5)
            ceny=int((Tly+Bry)*0.5)
            Tmx=(Tlx+Trx)*0.5
            Tmy=(Tly+Try)*0.5
            slope=((math.atan2(Tmx-cenx,Tmy-ceny))*180/math.pi)-90
            if slope<0:
                slope=slope+360
            # print(slope)
            # if slope<0:
            #     angle=360-(math.atan(slope)*180/math.pi)
            # else:
            #     angle=(math.atan(slope)*180/math.pi)

            point(cap,Tlx,Tly,128,128,128)
            point(cap,Trx,Try,0,255,0)
            point(cap,Brx,Bry,180,105,255)
            point(cap,Blx,Bly,255,255,255)
            lines(cap,int((Tlx+Trx)*0.5),int((Tly+Try)*0.5),cenx,ceny,255,0,0)
            point(cap,cenx,ceny,0,0,255)
            cv2.putText(cap,str(arucofound[1][t][0]),(cenx+10,ceny),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),thickness=2)
            cv2.putText(cap,f"{str(round(slope,1))}",(cenx-120,ceny-30),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),thickness=2)
            
            

            t+=1
            

        

            
        # os.chdir(r'D:\python projects')
        # cv2.imwrite("markerdetected2.jpg", cap) 
        # print(arucofound[1])   
        cv2.imshow("image",cap)
        if cv2.waitKey(1)==ord('q'):
            break

if __name__=="__main__":
    Mark_ArUco()