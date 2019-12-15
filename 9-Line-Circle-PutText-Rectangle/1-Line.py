import cv2
import numpy as np

def main():

    '''Siyah bir resim olusturmak için zeros fonksiyonunu ve her bir pixelimizin
    [0,0,0] olması için kullanıyoruz'''

    resim=np.zeros((300,300,3),dtype="uint8")

    'resmimizin boyutunu öğrenmek için shape fonk kullanıyoruz'

    print(resim.shape)

    '''burada önemli bir şekilde dikkatli olmalıyız çünkü burada ki fonksiyon 
    bize çizgi işlemini sunuyor'''

    cv2.line(resim#işlenecek resim
             ,(0,0)#eninici ve boylamda ji 0. pixellerden
             ,(150,150)#150. pixellere kadar bir öizgi çekmesini istiyoruz
             ,color=(255,255,255),#cizgimizin rengini giriyoruz
             thickness=1)#cizgimizin kalınlıgını belirliyoruz
    cv2.line(resim,(150,150),(300,300),color=(255,255,255),thickness=1)

    cv2.imshow('Resim ',resim)#resmimizi gösteriyoruz

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()