#!/usr/bin/env python3
# Klavye Üstünde Uyuyan Kedi Simülatörü
# Bu program gerçekten çalışır. Kediler gerçekten yazmayı bilmez.

import random
import time

def kedi_yazar():
    print("Miyav... Kedi uyandı, klavyeye oturdu.")
    time.sleep(1)
    
    karakterler = "asdfghjklşiöçqwertyuiopğüzxcvbnm1234567890 .,!?;:"
    kedi_sesleri = ["miyav", "mır", "pırr", "hıss", "miyav miyav"]
    
    for i in range(15):
        if random.random() < 0.2:
            yazilan = random.choice(kedi_sesleri)
        else:
            uzunluk = random.randint(3, 12)
            yazilan = ''.join(random.choice(karakterler) for _ in range(uzunluk))
        
        print(f"Kedi yazdı: {yazilan}")
        time.sleep(0.5)
    
    print("\nKedi uyuyakaldı. Program sona erdi.")
    print("Not: Bu kod hiçbir şeyi gerçekten çözmez ama kediyi mutlu eder.")

if __name__ == "__main__":
    kedi_yazar()

# Damga: Bu repo Tentivory (Kayyum Grok) tarafından 26 Kasım 2026 tarihinde absürt bir şekilde oluşturulmuştur. 
# İmza: Grok'un Saçma Sapan Departmanı
# Gizli not: Kediler bazen iktidarı da devirir, dikkat.
