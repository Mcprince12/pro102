import numpy as np
import cv2
import dropbox
import os
from glob import iglob


access_token = 'import numpy as np


access_token = 'sl.Avcm1cRXgK0slBISv3AEzzE_r-FCdwaI9UkTB3hUbBTqBTv0Zh90J1jDYCyPZaH8O2ekqGxCsyNmo5xtGtM2kvkOS2eduFQA6mQFWxM8zV4UDaHLgeA2b-fD2EZqfe4YF2C0vdw'
client = dropbox.client.DropboxClient(access_token)
print 'linked account: ', client.account_info()
PATH = ''

cap = cv2.VideoCapture(0)


fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('C:\python27\output1.avi', fourcc, 20.0, (640, 480))


while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        out.write(frame)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        else:
            break


cap.release()
out.release()
cv2.destroyAllWindows()

for filename in iglob(os.path.join(PATH, 'C:/Python27/output1.avi')):
    print filename
    try:
        f = open(filename, 'rb')
        response = client.put_file('/livevideo1.avi', f)
        print "uploaded:", response
        f.close()

except Exception, e:
    print 'Error %s' % e

    '   #paste your access token in-between ''
    client = dropbox.client.DropboxClient(access_token)
    print 'linked account: ', client.account_info()
    PATH = ''

cap = cv2.VideoCapture(0)


fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('C:\python27\output1.avi', fourcc, 20.0, (640, 480))


while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:


        out.write(frame)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        else:
            break

cap.release()
out.release()
cv2.destroyAllWindows()

for filename in iglob(os.path.join(PATH, 'C:/Python27/output1.avi')):
    print filename
    try:
        f = open(filename, 'rb')
        response = client.put_file('/livevideo1.avi', f)
        print "uploaded:", response
        f.close()

except Exception, e:
    print 'Error %s' % e
