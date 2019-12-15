import cv2
import numpy as np

def main():
    arka_plan=cv2.imread('arkaplan.jpg')
    zar=cv2.imread('zar.jpg')

    '''resmimizin etrafını sararak  remimizi e zar resmini dahil edeceğiz 
    ve böylelikle daha geniş bir resim elde edpi bazı hatalardan da 
    kurtulmuş olacagız'''

    sarılmıs_arkaplan=cv2.copyMakeBorder(arka_plan,# resmimiz
                                         100,#top
                                         100,#bottom
                                         100,#
                                         100,
                                         borderType=cv2.BORDER_CONSTANT#border
                                         # tipinşi etrafını sarmala dedik
                                         ,value=[255,255,255])#sarmalanmıs
                                        # resmimizin etrafını beyaz yap dedik

    yukseklik,genislik,kanal=zar.shape
    print(yukseklik,genislik,kanal,sep='-')
    zar_gri=cv2.cvtColor(zar,cv2.COLOR_BGR2GRAY) #resmimizi gri renge
    # dönüştürdük

    '''treshold yaparak resmimizi tresliyoruz ve rengimizi siyah veya 
    beyaz olarak treshlemesini sağlıyoruz
    kısaca maskeleme işlemi yapmış oluyoruz'''

    '''kısaca treshold sinüsal bir dalgayı karesel dalgaya çeviriyor 10 ile 255 o 
    aralıgı ayarlıyoruz'''

    ret,mask=cv2.threshold(zar_gri#maskelenecek resim
                           ,10#beyaz ayarı
                           ,255#siyah ayarı
                           ,cv2.THRESH_BINARY)#hangi cinste maskelem yapılacaksa

    'yukarıda maskeleme yaptıgımız resmi aşağıda değilini alarak' \
    'bu şekilde her iki türlü işlem yapabiliriz ' \
    'siyah beuyaz şeklinde'
    mask_inver=cv2.bitwise_not(mask)

    '''random_image e biz arkplanın belli bir kısımnı atayrak resmimizi kesiyoruz
    ve kestigimiz resme eklemeler yapacagız bitwise and ile'''
    random_image = sarılmıs_arkaplan[0:yukseklik, 0:genislik]

    '''resimimizi şimdi nirleştirme işlemşi yaparak üst üste ekleyecegiz
    maskemiz siyah bir nesne olamılı ki bir sonra ki ekleme de yani toplamada  
    resimimiz üst üste geldiğinde siyah etkisiz bir eleman olacagı için resmimizi 
    rahat bir şekilde eklemiş olucagız'''

    birlesik_resim=cv2.bitwise_and(random_image,random_image,mask=mask_inver)

    '''burada resimleri topluyoruz dikkat edilmesi gereken yer siyah 
    yerler etkisiz olacagı için üstüne hangi renk gelşiyor ise direk olarak 
    toplanacaktır ve ilgili pixelde siyahtan başka bir renk meudana gelecektir'''

    toplanmis_resim=cv2.add(birlesik_resim,zar)

    '''burada topladıgımız resmimizi en geniş resmimize ekleme yapıyoruz ancak
    bu ekleme işlemi resmin belli bir yerlerini boyutlandırma ile olmakta 
    aşağıda ki komutta 0 dan yüksekliğimiz kadar ekleme işlemi yap ve 0 dan genişlik
    kadar olan yerde topnlanmış pixelleri ata demiş oluyoruz
    ve böylelikle geniş kısımda ki resme ekleme işlemi yapmış oluyoruz'''

    sarılmıs_arkaplan[0:yukseklik,0:genislik]=toplanmis_resim

    #cv2.imshow('Arkaplan',arka_plan)
    #cv2.imshow('zar',zar)
    #cv2.imshow('zar gri',zar_gri)
    cv2.imshow('Mask',mask)
    cv2.imshow('Mask inver',mask_inver)
    cv2.imshow('Birleştirilmiş resim',birlesik_resim)
    #cv2.imshow('Toplanmis Resim',toplanmis_resim)
    cv2.imshow('Roi',random_image)
    cv2.imshow('Toplanmıs',toplanmis_resim)
    cv2.imshow('Sarilmiş Resim',sarılmıs_arkaplan)





if __name__ == '__main__':
    main()

cv2.waitKey(0)
cv2.destroyAllWindows()