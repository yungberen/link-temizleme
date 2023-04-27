import re
import webbrowser

links = []

print("""

  ____   _______     __
 |  _ \ / ____\ \   / /
 | |_) | |  __ \ \_/ / 
 |  _ <| | |_ | \   /  
 | |_) | |__| |  | |   
 |____/ \_____|  |_|   
                       
                       
 
""")
print("Link temizleyiciye hoş geldiniz! Temizlenmesini istediğiniz linki girin veya 'q' tuşuna basarak çıkın.")

while True:
    link = input("\nLink: ")
    if link == "q":
        break
    cleaned_link = re.sub(r'[^\x00-\x7F]+|\s', '', link)
    links.append(cleaned_link)
    webbrowser.open(cleaned_link)
    with open("cleaned_links.txt", "a") as file:
        file.write(cleaned_link + "\n")

print("\nProgram sonlandırıldı. Temizlenmiş linkler 'cleaned_links.txt' dosyasında kaydedildi.")
