#kütüphaneyi çağırıyoruz
import pyttsx3
import random
 
 
def konus(metin):
    #pyttsx3.Engine'i referans olarak alır
    engine = pyttsx3.init()
    print("**************************************************************************")
    print(dizi[random.randint(0, 2)])
    
    
    #say() metodu, okunacak metinleri alır
    engine.say(metin)
    
    
    #rate ile ses hızını belirliyoruz.
    #rate=100 demek,dakikada 100 kelime okunacak demek
    #rate, default olarak 200 değerine sahiptir
    engine.setProperty("rate",100)
    
    
    #volume ile ses yüksekliğini belirliyoruz(maksimum=1.0)
    #volume default olarak 1.0 değerine sahiptir
    engine.setProperty("volume", 0.9)
    
    
    #metinlerin okunması için gereklidir
    engine.runAndWait()

metin1 = """ Donec rutrum congue leo eget malesuada. Curabitur arcu erat, accumsan id imperdiet et, 
porttitor at sem. Vivamus magna justo, lacinia eget consectetur sed, 
convallis at tellus. Curabitur arcu erat, accumsan id imperdiet et, porttitor at sem."""
metin2 = """Cras ultricies ligula sed magna dictum porta. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed porttitor lectus nibh.  """
metin3 = """ Nulla porttitor accumsan tincidunt. Sed porttitor lectus nibh. Quisque velit nisi, pretium ut lacinia in,
elementum id enim. Curabitur aliquet quam id dui posuere blandit. Quisque velit nisi, pretium ut lacinia in, elementum id enim."""

dizi = [metin1, metin2, metin3]

if __name__=='__main__':
    konus("deneme metni")