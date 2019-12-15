import cv2
import numpy as np

# author: @harunlakodla (Harun KURT)

#resimleri okummak için imread methodunu tanımlıyoruz
resim=cv2.imread('opencv_stablizator_rov.png')

# resmimiz den gelen datayı yazdıralım... bize matris şeklinde dönüyor
# dikkat edelim
print(type(resim))
#görüldüğü gibi bize <class 'numpy.ndarray'> bu şekilde array şeklinde
# dönüyor

#okunan resmi yazdırma işlemi yapabilmek için imshow u kullanıyoruz
cv2.imshow('Resmimiz',resim)

'''aşağıda ki methodlarımız cok önemlidir hata almamak için 
ve her seferinde bunları kullanacagız 
waitkey bizlere döngümüzü gösteriyor
destroyAllWindows ise cv2 deki bilgileri ekrana dökmemizi sağlıyor
'''
cv2.waitKey(0)
cv2.destroyAllWindows()



