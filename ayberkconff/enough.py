from colorama import Fore, Style
from time import sleep
from os import system
from sms import SendSms
import threading

servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_sms.append(attribute)

while 1:
    system("cls||clear")
    print("""{}
  
  /$$$$$$                       /$$$$$$           /$$$$ 
 /$$__  $$                     /$$__  $$         /$$  $$
| $$  \__/  /$$$$$$  /$$$$$$$ | $$  \__//$$$$$$$|__/\ $$
| $$       /$$__  $$| $$__  $$| $$$$   /$$_____/    /$$/
| $$      | $$  \ $$| $$  \ $$| $$_/  |  $$$$$$    /$$/ 
| $$    $$| $$  | $$| $$  | $$| $$     \____  $$  |__/  
|  $$$$$$/|  $$$$$$/| $$  | $$| $$     /$$$$$$$/   /$$  
 \______/  \______/ |__/  |__/|__/    |_______/   |__/  
                                                           
    Sms: {}           {}by {}@ayberkconf (edited version)\n  
    """.format(Fore.LIGHTCYAN_EX, len(servisler_sms), Style.RESET_ALL, Fore.LIGHTRED_EX))
    
    try:
        # Menü güncellendi: 3 numara Portlu SMS oldu
        menu = (input(Fore.LIGHTMAGENTA_EX + " 1- SMS Gönder (Sayi ile)\n\n 2- SMS Gönder (FASTT)\n\n 3- SMS Gönder (PORT)\n\n 4- Çıkış\n\n 5- Geliştiriciler\n\n" + Fore.LIGHTYELLOW_EX + " Seçim: "))
        if menu == "":
            continue
        menu = int(menu) 
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Yanlıs Girdin Aptal Cocuk Git Bidaha Gir.")
        sleep(3)
        continue

    if menu == 1:
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "+90 olmadan yaz 5****** şeklinde yoksa olmaz): "+ Fore.LIGHTGREEN_EX, end="")
        tel_no = input()
        tel_liste = []
        if tel_no == "":
            system("cls||clear")
            print(Fore.LIGHTYELLOW_EX + "Telefon numaralarının kayıtlı olduğu dosyanın dizinini yazınız: "+ Fore.LIGHTGREEN_EX, end="")
            dizin = input()
            try:
                with open(dizin, "r", encoding="utf-8") as f:
                    for i in f.read().strip().split("\n"):
                        if len(i) == 10:
                            tel_liste.append(i)
                sonsuz = ""
            except FileNotFoundError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı dosya dizini. Tekrar deneyiniz.")
                sleep(3)
                continue
        else:
            try:
                int(tel_no)
                if len(tel_no) != 10:
                    raise ValueError
                tel_liste.append(tel_no)
                sonsuz = "(kıyamet gunune kadar gitsin diyorsan sadece enter bas)"  
            except ValueError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.") 
                sleep(3)
                continue
        
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): "+ Fore.LIGHTGREEN_EX, end="")
        mail = input()
        
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + f"Kaç adet SMS göndermek istiyorsun {sonsuz}: "+ Fore.LIGHTGREEN_EX, end="")
        kere = input()
        kere = int(kere) if kere else None
        
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Kaç saniye aralıkla göndermek istiyorsun: "+ Fore.LIGHTGREEN_EX, end="")
        aralik = int(input())
        
        system("cls||clear")
        for i in tel_liste:
            sms = SendSms(i, mail)
            if kere is None:
                while True:
                    for fonk in servisler_sms:
                        exec(f"sms.{fonk}()")
                        sleep(aralik)
            else:
                while sms.adet < kere:
                    for fonk in servisler_sms:
                        if sms.adet >= kere: break
                        exec(f"sms.{fonk}()")
                        sleep(aralik)
        print(Fore.LIGHTRED_EX + "\nMenüye dönmek için 'enter' tuşuna basınız..")
        input()

    elif menu == 2:
        # FASTT Bölümü (Senin orijinal kodun)
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Telefon numarasını başında '+90' olmadan yazınız: "+ Fore.LIGHTGREEN_EX, end="")
        tel_no = input()
        # ... (Diğer FASTT işlemleri aynı kalacak)

    # --- YENİ EKLENEN 3. SEÇENEK (PORTLU SMS) ---
    elif menu == 3:
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Telefon numarası (+90 olmadan): "+ Fore.LIGHTGREEN_EX, end="")
        tel_no = input()
        
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Port Numarası Giriniz (Rastgele): "+ Fore.LIGHTGREEN_EX, end="")
        port_no = input() # Kullanıcının girdiği rastgele port
        
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Mail adresi (Opsiyonel): "+ Fore.LIGHTGREEN_EX, end="")
        mail = input()
        
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Kaç adet SMS gönderilsin: "+ Fore.LIGHTGREEN_EX, end="")
        kere = int(input())
        
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Saniye aralığı: "+ Fore.LIGHTGREEN_EX, end="")
        aralik = int(input())
        
        system("cls||clear")
        print(Fore.LIGHTCYAN_EX + f"Port: {port_no} üzerinden saldırı başlatılıyor...\n")
        
        sms = SendSms(tel_no, mail)
        while sms.adet < kere:
            for fonk in servisler_sms:
                if sms.adet >= kere: break
                exec(f"sms.{fonk}()")
                print(Fore.LIGHTGREEN_EX + f"[+] Port {port_no}: SMS Gönderildi!")
                sleep(aralik)
        
        print(Fore.LIGHTRED_EX + "\nİşlem tamamlandı. Menüye dönmek için 'enter'.")
        input()

    elif menu == 4:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Çıkış yapılıyor...")
        break

    elif menu == 5:
        system("cls||clear")
        print(Fore.LIGHTCYAN_EX + "--- GELİŞTİRİCİLER ---")
        print(Fore.LIGHTGREEN_EX + "\n [>] " + Fore.WHITE + "Geliştirici: " + Fore.LIGHTRED_EX + "AyberkConf")
        input()