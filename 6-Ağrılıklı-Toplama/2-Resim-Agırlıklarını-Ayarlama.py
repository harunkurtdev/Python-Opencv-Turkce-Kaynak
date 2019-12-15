import  cv2

on=cv2.imread('on.jpg')
arka=cv2.imread('arka.jpg')


'buradası bizim resmizizi ağırlıklı olarak birleiştirdiğimiz yer'
newimage=cv2.addWeighted(on# burası resmilerimizden birincisi olan
                         ,0.6 #burada 1. reime düsen ağırlık
                         ,arka # 2. resmimiz
                         ,0.4 #burası ise  2. resmin ağrlıgı
                         ,0)# burası da gama yerimiz burada
                            # kesinlikle gama vermeyi unutmayın!

'Resimleri gösteriyoruz'
cv2.imshow('On Resim',on)
cv2.imshow('Arka Resim',arka)
cv2.imshow('Ağrılıgı alınmış resim',newimage)

cv2.waitKey(0)
cv2.destroyAllWindows()