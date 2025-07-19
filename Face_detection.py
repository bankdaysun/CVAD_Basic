import cv2
img_path="path"

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
img=cv2.imread(img_path)
img = cv2.resize(img,(_,_))##############
if img is None:
    print("No Picture")
gray = cv2.cvtColor(img,_)####################
faces= face_cascade.detectMultiScale(gray,scaleFactor=_,minNeighbors=_,minSize=(_,_))######
for(x,y,w,h)in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(_,_,_),_)#########
    cv2.putText(img,"_____",(x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)#####
    cv2.putText(img, ("face ="+str(len(faces))), (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

print(len(faces))
cv2.imshow("raw",___)
cv2.waitKey(0)
cv2.destroyAllWindows()