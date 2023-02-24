def dosyayaz(metin):
    with open("output.txt", "a") as f:
        f.write("\n"+metin)

def dosyaoku():
    with open("output.txt", "r") as f:
        print(f.read())