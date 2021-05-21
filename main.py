# İçe aktarmalar
# Ekran görüntüsü almak için kütüpahe
import pyscreenshot as ImageGrab
# Matris işlemleri için kütüphane
import numpy as np
# Fare işlemleri için kütüphane
from pynput.mouse import Button, Controller
# Zaman işlemleri için kütüphane
from time import time
from time import sleep

# Ekran görüntüsü alıp matris olarak veren fonksiyon
def grab():
    # (300, 245) ile (630, 575) aralığındaki bölgenin ekran görüntüsünü al
    image = ImageGrab.grab(bbox=(300, 245, 630, 575))
    # Görüntüyü RGB'den gri tonlamaya çevir
    grayscaled = image.convert("L")
    # Görüntüyü matrise çevir
    grayscaled_m = np.array(grayscaled)
    # Matrisi return et
    return grayscaled_m


# Verilen matirs üzerindeki 4x4'lük 80 piksel genişlik ve yüksekliğe sahip
# bölgelerin orta noktasındaki piksel'in siyah olması durumunda koordinatı veren fonksiyon
def find(matris):
    # Boş bir koordinatlar dizisi
    coordinates = []
    # İç içe [0, 3] tamsayılarında dönen iki döngü
    for i in range(4):
        for u in range(4):
            # x koordinatının hesaplanması
            x = i * 82 + 41
            # y koordinatının hesaplanması
            y = u * 82 + 41
            # Söz konusu (x, y) koordinatı siyah mıdır
            if matris[y][x] == 0:
                # (x, y) koordinatındaki piksel siyah ise koordinatı listeye ekle
                coordinates.append([x, y])

    # Koordinatlar listesini return et
    return coordinates


# Verilen koordinatlar listesine tıkla
def click(coordinates):
    # Mouse objesi oluştur
    mouse = Controller()
    # Tüm koordinatlarda döngü oluştur
    for coord in coordinates:
        # Fare işaretçisini n. koordinata taşı ((300, 245) ofsetine dikkat)
        mouse.position = (300 + coord[0], 245 + coord[1])
        # Tıklama işlemini 1 defa yap
        mouse.click(Button.left, 1)


# Kodu çalıştır
if __name__ == '__main__':
    # Şimdiki zamanı al (İlk zaman)
    t = time()
    # Şimdiki zaman ile ilk zaman (t) arasındaki farkı al (muhtemelen 0 veya 0'a çok yakın)
    t_che = time() - t
    # Şimdiki zaman ile t (İlk zaman) arasındaki fark 200'den daha az olduğu sürece devam et
    while t_che < 200:
        # Görüntüyü al -> Siyah koordinatları algıla -> koordinatlara tıkla
        click(find(grab()))
        # Zaman farkını güncelle
        t_che = time() - t
        # 0.0001 saniye bekle
        sleep(0.0001)
