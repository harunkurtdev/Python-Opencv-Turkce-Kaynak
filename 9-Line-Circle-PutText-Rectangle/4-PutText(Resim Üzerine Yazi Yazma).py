import cv2
import numpy as  np

resim = np.zeros((300, 300, 3), dtype="uint8")

'Resmimize Yazmak istediğimiz yazıları putText fonk ile girebiliyoruz' \
'Font_... bilmem ne denilen ise bizim yazımzın'

cv2.putText(resim, 'Merhaba Ben Resim'#girilecek yazimiz
            , (75, 75)#burası yazımızın başlayacagı pixel sol alt köşeden
            #pixel yazımız başlamakta
            , cv2.FONT_HERSHEY_COMPLEX#burada yazımızın font tipini
            #belirliyoruz
            ,0.6#yazımızın büyüklüğü
            , color=(0, 0, 255)#yazmızın rengi
            , thickness=1)#yazımızın cizgi kalınlıgı

cv2.imshow('Resim',resim)

cv2.waitKey(0)
cv2.destroyAllWindows()