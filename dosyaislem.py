def dosyayaz(metin):
    with open("output.txt", "a") as f:
        f.write(f"{metin}\n")

def dosyaoku():
    with open("output.txt", "r") as f:
        print(f.read())