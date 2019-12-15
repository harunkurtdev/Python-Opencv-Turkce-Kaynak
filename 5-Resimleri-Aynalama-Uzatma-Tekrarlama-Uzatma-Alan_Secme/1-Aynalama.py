import cv2
import numpy as np
'burada asıl amaç resimden okudugmuz arrayleri image atamak'
image=cv2.imread('image.jpg')

'ayna_resim adında bir değiken atıyoru ve bu değikene copyMakeBorder ' \
'fonksiyonunu kullanarak image ten edilen resmi copy ederek değiştir gibi' \
'sıfat kullanımış oluyyoruz' \
'cv2.border-reflect ise bize resmimizi yansıtma yapmamızı yani ' \
'aynalama yapmamızı ssağlıyor kısaca '
ayna_resim=cv2.copyMakeBorder(image #hangi resim ile uğraşacaksak onu yazıoruz
                              ,100 # burası resmimize yukarıdan 100 margin vermemizi sağlar
                              ,100 #burası botom kısmıdır zaten bunlar kısaca copyMakeBorder da yazar
                              ,100,100,
                              cv2.BORDER_REFLECT)# Burası bizim resmimizi nasıl ayarlacagımızla ilgidir

cv2.imshow('Orjinal resim',image)#normal resmimiizi göstermesini istedik
cv2.imshow('Aynalanmış resim',ayna_resim)#burada ise aynalama yaptıgımız resmi göstermesini isteidk

cv2.waitKey(0)
cv2.destroyAllWindows()