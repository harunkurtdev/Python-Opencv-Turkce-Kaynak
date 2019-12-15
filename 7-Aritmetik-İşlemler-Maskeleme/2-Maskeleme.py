import cv2
'burada resmimizi açtık'
zar=cv2.imread('zar.jpg')

'burada resmimizi gri haline getiriyoruz ve gri adında ki değişkene atıyoruz ' \
'yada dire olarak imread fonksşyonunda 2. parametreye 0 vermemiz yeterli id'

gri_zar=cv2.cvtColor(cv2.UMat(zar),cv2.COLOR_BGR2GRAY)

'burada ise maskeleme işlemi yapıyoruz resmimizi girdilkten sonra biz ' \
'2. parametre olarak beyazlık dengesini ayarlıyoruz sayı 255 e arttıkça ' \
'resmimiz siyahlaşmakta 3. parametre olarakta resmimizi siyajlık dengesini ' \
'ayarlıyoruz 4. parametrede ise maskleme işleminin tipini belirliyoruz'
ret,mask=cv2.threshold(gri_zar#resim
                       ,100,#beyazlık dengesi
                       255,#siyahlık dengesi
                       cv2.THRESH_BINARY)#maskeleme tipi

'bitwise_not ise bizim maskeleme yaptıgımız işlemi tersini aliyoruz siyahlar' \
'beyaz ,beuazlar siyah oluyor'

mask_inver=cv2.bitwise_not(mask)#maskemizin tersini alıyoruz

'burada maskeleme işlemlerini yaptıktan sonra resmimize nasıl entegre edebiliriz' \
'yaptıgımız maskleme işlemini bitwise_and ile resimimize entegre ediyoruz ' \
'mask veya mask inver kullanabilirsiniz projenize göre ' \
'eğer ki mask kullanırsanız resminizde , beyaz yerlere deki pixelleri' \
'resminizin pixellerini eklemiş olursunuz' \
'eğerki mask_inver kullanırsanız yine aynısı olucaktır ancak resminizde ki mask' \
'işleminin tam tersi olucaktır '

birlesik_maske=cv2.bitwise_and(zar,zar,mask=mask_inver)

'burada ise resiminizi' \
'add ile 2 resmimizi birleştirme işlmei yapmaktayız ve birleştirdiğimiz resimleri' \
'toplam adında bir değişkene atamaktayız siyah rengin 0 değeri oldugnu' \
'bilmekteyiz yani etkisiz bir eleman diyebiliriz onun için siyah pixellerin oldugu' \
'yerler bizim diğer pixellerimizin yerini aldırdıgımız yer'

toplam_resim=cv2.add(gri_zar,mask)

'burada resimlerimizi gösteriyoruz'

cv2.imshow('Zar',zar)
cv2.imshow('Gri Zar',gri_zar)
cv2.imshow('Mask',mask)
cv2.imshow('Mask Inver',mask_inver)
cv2.imshow('Birlesik Maske',birlesik_maske)
cv2.imshow('Toplam Resim',toplam_resim)

cv2.waitKey(0)
cv2.destroyAllWindows()