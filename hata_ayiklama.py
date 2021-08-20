for i in range(3):
    ilk_sayı=input("ilk sayı:(Programdan çıkmak için q tuşuna basınız.")
    if ilk_sayı=="q":
        print("çıkılıyor...")
        break
    
    elif i ==2:
        print("bu alanı 3 kez yanlış doldurdunuz."
        "lütfen daha sonra yeniden deneyiniz.")
    ikinci_sayı= input("ikinci sayı:")
    try:
        sayı1=int(ilk_sayı)
        sayı2=int(ikinci_sayı)
    except ValueError:
        print("Sadece sayı girin!")
    else:
        try:
            print(sayı1/sayı2)
        except ZeroDivisionError:
            print("bir sayıyı 0'a bölemezsiniz.")