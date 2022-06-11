# WELCOME TO BITS-TO-PETS
# ----------------------------
# Here we Upgrade Pets using Bits to earn Profit

import requests
import sys
import json

pets = [{'name':"Armadillo",'RARE':[250000,None,0,2,None,None],'EPIC':[1000000,None,0,5,None,None],'LEGENDARY':[None,None]},{'name':"Baby Yeti",'EPIC':[20000000,None,16,12,None,None],'LEGENDARY':[None,None]},{'name':"Bat",'RARE':[190000,None,0,1,None,None],'EPIC':[250000,None,64,3,None,None],'LEGENDARY':[None,None]},{'name':"Bal",'EPIC':[2000000,None,100,10,None,None],'LEGENDARY':[None,None]},{'name':"Bee",'RARE':[150000,None,9,1,None,None],'EPIC':[450000,None,9,3,None,None],'LEGENDARY':[None,None]},{'name':"Blaze",'EPIC':[200000,None,64,12,None,None],'LEGENDARY':[None,None]},{'name':"Blue Whale",'RARE':[900000,None,1,7,None,None],'EPIC':[9000000,None,8,12,None,None],'LEGENDARY':[None,None]},{'name':"Chicken",'RARE':[190000,None,0,1,None,None],'EPIC':[250000,None,8,1,None,None],'LEGENDARY':[None,None]},{'name':"Dolphin",'RARE':[10000000,None,0,7,None,None],'EPIC':[50000000,None,16,14,None,None],'LEGENDARY':[None,None]},{'name':"Elephant",'RARE':[900000,None,0,5,None,None],'EPIC':[14000000,None,0,10,None,None],'LEGENDARY':[None,None]},{'name':"Ender Dragon",'EPIC':[400000000,None,8,20,None,None],'LEGENDARY':[None,None]},{'name':"Enderman",'RARE':[10000,None,0,6,None,None],'EPIC':[40000000,None,8,12,None,None],'LEGENDARY':[None,None]},{'name':"Endermite",'RARE':[190000,None,0,3,None,None],'EPIC':[250000,None,512,7,None,None],'LEGENDARY':[None,None]},{'name':"Flying Fish",'RARE':[200000,None,0,5,None,None],'EPIC':[1000000,None,64,10,None,None],'LEGENDARY':[None,None]},{'name':"Ghoul",'EPIC':[5000000,None,512,10,None,None],'LEGENDARY':[None,None]},{'name':"Giraffe",'RARE':[900000,None,128,7,None,None],'EPIC':[9000000,None,512,12,None,None],'LEGENDARY':[None,None]},{'name':"Golem",'EPIC':[10000000,None,8,20,None,None],'LEGENDARY':[None,None]},{'name':"Guardian",'RARE':[500000,None,0,2,None,None],'EPIC':[3000000,None,64,5,None,None],'LEGENDARY':[None,None]},{'name':"Horse",'RARE':[190000,None,0,1,None,None],'EPIC':[250000,None,8,1,None,None],'LEGENDARY':[None,None]},{'name':"Hound",'EPIC':[5000000,None,512,10,None,None],'LEGENDARY':[None,None]},{'name':"Jellyfish",'EPIC':[15000000,None,16,10,None,None],'LEGENDARY':[None,None]},{'name':"Jerry",'RARE':[40000,None,1,1,None,None],'EPIC':[100000,None,1,3,None,None],'LEGENDARY':[None,None]},{'name':"Lion",'RARE':[900000,None,0,7,None,None],'EPIC':[14000000,None,1024,14,None,None],'LEGENDARY':[None,None]},{'name':"Magma Cube",'RARE':[10000,None,0,5,None,None],'EPIC':[500000,None,16,10,None,None],'LEGENDARY':[None,None]},{'name':"Megalodon",'EPIC':[10000000,None,0,20,None,None],'LEGENDARY':[None,None]},{'name':"Mithril Golem",'RARE':[25000,None,0,5,None,None],'EPIC':[50000,None,0,20,None,None],'LEGENDARY':[None,None]},{'name':"Monkey",'RARE':[900000,None,0,7,None,None],'EPIC':[17000000,None,0,12,None,None],'LEGENDARY':[None,None]},{'name':"Ocelot",'RARE':[190000,None,0,2,None,None],'EPIC':[250000,None,512,5,None,None],'LEGENDARY':[None,None]},{'name':"Parrot",'EPIC':[15000000,None,16,14,None,None],'LEGENDARY':[None,None]},{'name':"Phoenix",'EPIC':[100000000,None,1024,20,None,None],'LEGENDARY':[None,None]},{'name':"Pig",'RARE':[190000,None,0,1,None,None],'EPIC':[250000,None,512,1,None,None],'LEGENDARY':[None,None]},{'name':"Pigman",'EPIC':[250000,None,8,10,None,None],'LEGENDARY':[None,None]},{'name':"Rabbit",'RARE':[190000,None,0,1,None,None],'EPIC':[250000,None,64,1,None,None],'LEGENDARY':[None,None]},{'name':"Rock",'RARE':[10000000,None,0,7,None,None],'EPIC':[50000000,None,64,14,None,None],'LEGENDARY':[None,None]},{'name':"Scatha",'RARE':[125000000,None,64,7,None,None],'EPIC':[250000000,None,256,14,None,None],'LEGENDARY':[None,None]},{'name':"Sheep",'RARE':[190000,None,0,3,None,None],'EPIC':[250000,None,512,7,None,None],'LEGENDARY':[None,None]},{'name':"Silverfish",'RARE':[190000,None,0,1,None,None],'EPIC':[250000,None,64,3,None,None],'LEGENDARY':[None,None]},{'name':"Skeleton",'RARE':[190000,None,0,1,None,None],'EPIC':[250000,None,128,3,None,None],'LEGENDARY':[None,None]},{'name':"Spider",'RARE':[190000,None,0,3,None,None],'EPIC':[250000,None,512,7,None,None],'LEGENDARY':[None,None]},{'name':"Spirit",'EPIC':[5000000,None,64,10,None,None],'LEGENDARY':[None,None]},{'name':"Squid",'RARE':[500000,None,0,2,None,None],'EPIC':[3000000,None,64,5,None,None],'LEGENDARY':[None,None]},{'name':"Tarantula",'EPIC':[5000000,None,512,10,None,None],'LEGENDARY':[None,None]},{'name':"Tiger",'RARE':[900000,None,0,7,None,None],'EPIC':[14000000,None,1024,12,None,None],'LEGENDARY':[None,None]},{'name':"Turtle",'EPIC':[15000000,None,16,10,None,None],'LEGENDARY':[None,None]},{'name':"Wither Skeleton",'EPIC':[250000,None,8,5,None,None],'LEGENDARY':[None,None]},{'name':"Wolf",'RARE':[190000,None,0,2,None,None],'EPIC':[250000,None,512,5,None,None],'LEGENDARY':[None,None]},{'name':"Zombie",'RARE':[190000,None,0,5,None,None],'EPIC':[250000,None,8,10,None,None],'LEGENDARY':[None,None]}]

url = "https://api.hypixel.net/skyblock/auctions?page="
ini = requests.get(url+"0")
ini_d = ini.json()
totalpg = ini_d['totalPages']
print('Total Number of Pages: 0 ->',totalpg-1)
x = []
for a in range(totalpg):
    data = requests.get(url+str(a))
    d = data.json()
    y = 1
    while not d['success']:
        data = requests.get(url+str(a))
        d = data.json()
        print("[FAIL] :", y)
        y += 1
    x.extend(d["auctions"])
    print("[SUCCESS] Page:", a)

sort = [items for items in x if not items['claimed'] and items["bin"] and "[Lvl" in items["item_name"]]

fltr = [{key: d[key] for key in ['item_name', 'item_lore', 'tier', 'starting_bid', 'uuid', 'auctioneer']} for d in sort]

print("Total Number of Pet Bins:",len(fltr))

user = str(input("Enter the Full Path Location where you want the Output to be made (C:\\Users): "))

with open(user+"\output.txt", "w+") as f:
    print(str(fltr).encode("ascii","ignore").decode(), file=f)
