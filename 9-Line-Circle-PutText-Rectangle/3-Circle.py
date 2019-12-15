import cv2
import numpy as np

resim=np.zeros((300,300,3),dtype="uint8")

'''fill fonksiyonu bize parametresine 0-255 arasında bir değer 
verdiğimizde verilen array dizisinin hepsini değerini o yapmakta'''

resim.fill(255)

print(str(resim.shape)+"\n"+str(resim))

'''Cirlce adında anlaşılacagı gibi bizim resmimize bir daire çizme işlemi
yapmakta bu dairenini çapı merkezi ve cizgi rengi , kalınlıgı gibi değerler
almakta'''

cv2.circle(resim#işlenecek resmimiz
           ,(150, 150)#dairemizin resim üzerinde ki merkezi
           ,50#dairemizin capı
           ,color=(0, 255, 0)#dairemizin çizgi rengi
           ,thickness=1)#dairemizin fizgi kalınglıgı

cv2.imshow('Kutu Resim', resim)


cv2.waitKey(0)
cv2.destroyAllWindows()