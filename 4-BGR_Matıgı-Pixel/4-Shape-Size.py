import cv2
import numpy as np
'burada asıl amaç resmimi değişkene aktarıyoruz'
new_image=cv2.imread('image.jpg')

'str() bize string olarak değer dönmekte ve buda print içerisinde ki d' \
'değerlerimizi string oalrak gösteermemizi sağlar =)'

'shape bize yükseklik genişlik ve renk kanalı sunar'
print('Burada resmimizin shpae ini öğreniyoruz',str(new_image.shape))
#Burada resmimizin shpae ini öğreniyoruz (251, 201, 3)

'size bize resmimizin büyüklüüğünü gösterir asıl amaç zaten' \
' büyüklükten daha cok pixel sayısını göstermektedir'
print('Burada resmimizin size ini öğreniyoruz',str(new_image.size))
#Burada resmimizin size ini öğreniyoruz 151353

'dtype ise bizim resmimizin tipini söyler'
print('Burada resmimizin ddtype ini öğreniyoruz',str(new_image.dtype))
#Burada resmimizin ddtype ini öğreniyoruz uint8


cv2.waitKey(0)
cv2.destroyAllWindows()