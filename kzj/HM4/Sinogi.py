import os,random,numpy
from cv2 import cv2

print('Sinogi:还就内个一头攒死')
score=0

def Q_B(event,x,y,flag,param):
	global score,img,QB
	if event==cv2.EVENT_LBUTTONDOWN:
		if not QB[y][x].any()==0:
			stp_x=y//img.shape[0]
			stp_y=x//img.shape[1]
			for a in range(1,img.shape[0]):
				for b in range(1,img.shape[1]):
					QB[stp_x*img.shape[0]+a][stp_y*img.shape[1]+b]=(0,0,0)
			score+=1

path=os.getcwd()
img=cv2.imread(path+'\\QB.jpg')
cv2.namedWindow('QB')
cv2.setMouseCallback('QB',Q_B)
while(1):
	QB=numpy.zeros((img.shape[0]*3,img.shape[1]*3+139,img.shape[2]),dtype=numpy.uint8)
	for a in range(0,3):
		for b in range(0,3):
			stp=random.randint(0,1)
			if(stp):
				for c in range(0,img.shape[0]):
					for d in range(0,img.shape[1]):
						QB[a*img.shape[0]+c][b*img.shape[1]+d]=img[c][d]
			cv2.rectangle(QB,(b*img.shape[1],a*img.shape[0]),((b+1)*img.shape[1],(a+1)*img.shape[0]),(187,197,57),1)
	for a in range(0,39):
		cv2.putText(QB,'Sinogi',(img.shape[1]*3+13,39),cv2.FONT_HERSHEY_COMPLEX,1,(187,197,57),2)
		for b in range(img.shape[1]*3+1,img.shape[1]*3+139):
			for c in range(39+10,39*3):
				QB[c][b]=(0,0,0)
		cv2.putText(QB,str(score),(img.shape[1]*3+13,39*2),cv2.FONT_HERSHEY_COMPLEX,1,(187,197,57),2)
		cv2.imshow('QB',QB)
		cv2.waitKey(1)
