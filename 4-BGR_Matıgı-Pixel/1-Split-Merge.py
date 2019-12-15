import  cv2
import numpy as np

'resimi okuyabilmek için imread methodunu tanımladık'
image=cv2.imread('image.jpg')
'okdugumuz resmi image adında bir değişkene tanımladık '

'''burada opencv kütüphanesi ile  split  methodunu kullanıyoruz 

---Split methodu ne işe yarar bize 3 tip veri gönderme işlemi yapar 

--ve bu değişkenler bize resimde ki renklermizin kanallarıdır

bgr şeklinde dönmektedir 

biz bu 3 değişkeni virgül şeklinde değişken tanımlama işlemi yapabiliriz 

'''
b,g,r=cv2.split(image)
'''
Biz blue değerine split ettiğimiz image den 0. parametresini atama
işlemi yapıyoruz ve sıra ile bu işlemleri yapıyoruz
'''

merge=cv2.merge((b,g,r))

'''burada ise opencv kğtğphanesinden aldıgımız merge fonksiyonu ile split ederek
aldıgımız 3 parametreyi birleştirmeyi sağlıyor ve bunu biz bir değişkene atayarak
resmimizi gösterebiliyoruz
'''


#burada merge değişkenini gösteiryoruz
cv2.imshow('Yeni Resmimiz Merge',merge)

cv2.waitKey(0)
cv2.destroyAllWindows()
