import cv2
'burada image den alınan array dizisini image atıyoruz'
image=cv2.imread('image.jpg')

'burada kesme işlemi yapıyoruz diyoruz ki ' \
'x in 0. pixelinden 100. pixeline kadar alanı al' \
'sonra y için diyoruz ,y ekseninde 0 dan başla 100 cü pixele kadar git' \
've böylekle kesitiğmiz alanı newimage atadık'
newimage=image[0:100,#0. pixel den 100. pxel e kes
         0:100]#buda y ekseni için

'kesme yönteminin farklı bir yöntemide vardır rectangle dediğimiz' \
'ingilizce de kare yöntemine gelmekte ya da dikdörtgen'

rectanglekesme=cv2.rectangle(image,(0,10),(10,50),[0,100,100])# buraya sonra değinilecektir
'krımızı bir renkte ufak bir kesme olusturduk ancak ççok ince bir çizgidir' \
'ilerleyen dönemlerde dersleri işlenecektir'

'Resimleri gösterdik'
cv2.imshow('Orjnal resim',image)
cv2.imshow('Kesilmiş resim',newimage)
cv2.imshow('Rectangle kesme',rectanglekesme)

cv2.waitKey(0)
cv2.destroyAllWindows()
