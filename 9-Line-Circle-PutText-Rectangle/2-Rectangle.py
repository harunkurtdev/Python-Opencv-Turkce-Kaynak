import cv2
import numpy as np

'''Siyah bir resim olusturmak için zeros fonksiyonunu ve her bir pixelimizin
    [0,0,0] olması için kullanıyoruz'''

resim = np.zeros((300, 300, 3), dtype="uint8")

'resmimizin boyutunu öğrenmek için shape fonk kullanıyoruz'

print(resim.shape)

'''burada önemli bir şekilde dikkatli olmalıyız çünkü burada ki fonksiyon 
bize kare dikdörgen gibi simetrik olabilecek şeyleri  işlemini sunuyor'''

'''---------------- pt2
   |              |
   | pt1          |
   ---------------- '''

cv2.rectangle(resim#işlecek resmimizi seçiyoruz
              ,(75,75)#pt1 bizim en aşağıdan başlayan köşemiz
              ,(100,200)#pt2 ise sağ üstten başlayan
              #yani kısaca pt1 den pt 2 ye kadar pixelleri işliyor
              ,color=(255,255,255)#cizdigimiz cizginin rengi
              ,thickness=2)#cizdigimiz cizginin kalınlıgı

'Resmimizi gösteriyoruz'

cv2.imshow('Kutu Resim',resim)


cv2.waitKey(0)
cv2.destroyAllWindows()