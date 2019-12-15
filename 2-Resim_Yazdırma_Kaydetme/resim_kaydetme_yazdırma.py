import cv2
import numpy as np

# author: @harunlakodla (Harun KURT)

#burada biz kendi local yerimizden yani kodun kayıtlı oldugu yerden
# resim okuma işlemi yapmaktayız
resim=cv2.imread('resim.jpg',#1. parametre olarak keni localdeki resmi
                 #mimizi yazıoyoruz
                 0)#burada ise 0-1 girmemizin sebebi ise rengimizi
                  # gri veya kendi rengiini elde edebilmek için

#resmin yeni ismi ile kayıt edebilmek için
# imwrite yöntemi bulunmakta

cv2.imwrite('yeni_yerim.jpg',#burada biz yeni resim ismimizi giriyoruz
            resim)#ve burada isse hangi resmi kaydetmek istiyorsak onu kullanıyoruz

#resmimizi ekrkanda gösteriyoruz
cv2.imshow('Gri Resmimiz',resim)
#ve görüldüğü gibi remimiz gri olarak cıkıyor...

cv2.waitKey(0)
cv2.destroyAllWindows()