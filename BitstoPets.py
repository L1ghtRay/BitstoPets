# WELCOME TO BITS-TO-PETS
# ----------------------------
# Here we Upgrade Pets using Bits to earn Profit

import requests
import sys
import json

pets = ['Ammonite','Armadillo','Baby Yeti','Bal','Bat','Bee','Black Cat','Blaze','Blue Whale','Chicken','Dolphin','Elephant','Ender Dragon','Enderman','Endermite','Flying Fish','Ghoul','Giraffe','Golden Dragon','Golem','Grandma Wolf','Griffin','Guardian','Horse','Hound','Jellyfish','Jerry','Lion','Magma Cube','Megoladon','Mithril Golem','Monkey','Ocelot','Parrot','Phoenix','Pig','Pigman','Rabbit','Rat','Rock','Scatha','Sheep','Silverfish','Skeleton','Skeleton Horse','Snowman','Spider','Spirit','Squid','Tarantula','Tiger','Turtle','Wither Skeleton','Wolf','Zombie']

user = str(input("Enter the name of your User (From C:\\Users\\ Folder): "))

url = "https://api.hypixel.net/skyblock/auctions?page="
ini = requests.get(url+"0")
ini_d = ini.json()
totalpg = ini_d['totalPages']
print('Total Number of Pages:',totalpg)
x = []
for a in range(totalpg):
    data = requests.get(url+str(a))
    d = data.json()
    if d['success'] == False:
        data = requests.get(url+str(a))
        d = data.json()
        print("Fail 1")
        if d['success'] == False:
            data = requests.get(url+str(a))
            d = data.json()
            print("Fail 2")
            if d['success'] == False:
                data = requests.get(url+str(a))
                d = data.json()
    x.extend(d["auctions"])
    print("Page:", a)

sort = [items for items in x if not items['claimed'] and items["bin"] and "[Lvl" in items["item_name"]]

with open("C:\\Users\\" + user + "\\output.txt", "w") as f:
    print(str(sort).encode("ascii","ignore").decode(), file=f)

print("Number of Pet Bins:",len(sort))
