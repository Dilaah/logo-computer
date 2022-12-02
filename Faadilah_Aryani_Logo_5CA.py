#Faadilah Aryani
#061930700727
#Kelas 5CA
#Logo Kelas 5CA

import cv2
import numpy as np

gambar = 255 * np.ones((512,512,3), np.uint8)
cv2.rectangle(gambar, (0,0), (600, 600), (0,0,0), cv2.FILLED)
cv2.rectangle(gambar, (35,35), (473, 475), (255,255,255), cv2.FILLED)
cv2.rectangle(gambar, (40,40), (468, 470), (0,0,0), cv2.FILLED)
cv2.rectangle(gambar, (45,45), (465, 467), (255,255,255), cv2.FILLED)
cv2.rectangle(gambar, (50,50), (460, 462), (0,0,0), cv2.FILLED)
cv2.rectangle(gambar, (60,60), (450, 450), (180,180,0), cv2.FILLED)

cv2.rectangle(gambar, (10,10), (70, 70), (255,0,255), cv2.FILLED)
cv2.rectangle(gambar, (440,10), (500, 70), (255,0,255), cv2.FILLED)
cv2.rectangle(gambar, (10,440), (70, 500), (255,0,255), cv2.FILLED)
cv2.rectangle(gambar, (440,440), (500, 500), (255,0,255), cv2.FILLED)

cv2.rectangle(gambar, (32,20), (43, 60), (255,255,255), cv2.FILLED)
cv2.rectangle(gambar, (18,35), (58, 45), (255,255,255), cv2.FILLED)
cv2.rectangle(gambar, (466,20), (477, 60), (255,255,255), cv2.FILLED)
cv2.rectangle(gambar, (450,35), (492, 45), (255,255,255), cv2.FILLED)

cv2.rectangle(gambar, (32,453), (43, 490), (255,255,255), cv2.FILLED)
cv2.rectangle(gambar, (18,467), (58, 478), (255,255,255), cv2.FILLED)
cv2.rectangle(gambar, (466,453), (477, 490), (255,255,255), cv2.FILLED)
cv2.rectangle(gambar, (450,467), (492, 478), (255,255,255), cv2.FILLED)

cv2.circle(gambar, (270,255), 180, (180,0,180), -1)
cv2.circle(gambar, (270,255), 140, (255,255,255), -1)
cv2.circle(gambar, (270,255), 130, (180,0,180), -1)
cv2.circle(gambar, (270,255), 95, (180,180,0), -1) 
cv2.circle(gambar, (440,255), 105, (180,180,0), -1)
cv2.rectangle(gambar, (460,120), (515, 385), (180,180,0), cv2.FILLED)
cv2.rectangle(gambar, (451,126), (500, 380), (0,0,0), cv2.FILLED)

font = cv2.FONT_HERSHEY_SIMPLEX
gambar = cv2.putText(gambar, 'A', (200, 325), font, 8, (180,0,180), 7, cv2.LINE_AA)
gambar = cv2.putText(gambar, 'FAADILAH ARYANI 5 CA', (200, 500), font, 0.5, (255,0,255), 1, cv2.LINE_AA)

gambar = cv2.putText(gambar, 'C', (460, 160), font, 1, (255,0,255), 2, cv2.LINE_AA)
gambar = cv2.putText(gambar, 'O', (460, 190), font, 1, (255,0,255), 2, cv2.LINE_AA)
gambar = cv2.putText(gambar, 'M', (460, 220), font, 1, (255,0,255), 2, cv2.LINE_AA)
gambar = cv2.putText(gambar, 'P', (460, 250), font, 1, (255,0,255), 2, cv2.LINE_AA)
gambar = cv2.putText(gambar, 'U', (460, 280), font, 1, (255,0,255), 2, cv2.LINE_AA)
gambar = cv2.putText(gambar, 'T', (462, 310), font, 1, (255,0,255), 2, cv2.LINE_AA)
gambar = cv2.putText(gambar, 'E', (460, 340), font, 1, (255,0,255), 2, cv2.LINE_AA)
gambar = cv2.putText(gambar, 'R', (460, 370), font, 1, (255,0,255), 2, cv2.LINE_AA)


print(gambar)
cv2.imshow('Logo 5CA', gambar)
cv2.waitKey(0)
cv2.destroyAllWindows()
