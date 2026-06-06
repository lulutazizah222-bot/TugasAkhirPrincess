import sys
import time

def jalanin_lirik ():
    lirik = [
        ("Ceeeeriiiita kita tak jauh berbeda", 0.20),
        ("Got beat down by the world", 0.12),
        ("sometimes I wanna fold", 0.12),
        ("Namun suratmu kan kuceritakan", 0.1),
        ("Ke anak-anakku nanti", 0.12),
        ("Bahwa aku pernah dicintai", 0.13),
        ("With everything you are", 0.2)
        
    ] 
    delay = [1.1, 1.4, 1.3, 1.6, 1.25, 1.1, 1, 1.56]
    print("\n======everything you are - hindia======")
    time.sleep(2)

    for baris in lirik:
        for karakter in baris:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(0)
            print()
    

jalanin_lirik() 