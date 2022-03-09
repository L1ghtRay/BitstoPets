# WELCOME TO BITS-TO-PETS
# ----------------------------
# Here we Upgrade Pets using Bits to earn Profit

import requests
import sys
import json

pets = [{'name':"Armadillo",'RARE':[250000,None,0,2],'EPIC':[1000000,None,0,5],'LEGENDARY':[None]},{'name':"Baby Yeti",'EPIC':[20000000,None,16,12],'LEGENDARY':[None]},{'name':"Bat",'RARE':[190000,None,0,1],'EPIC':[250000,None,64,3],'LEGENDARY':[None]},{'name':"Bal",'EPIC':[2000000,None,100,10],'LEGENDARY':[None]},{'name':"Bee",'RARE':[150000,None,9,1],'EPIC':[450000,None,9,3],'LEGENDARY':[None]},{'name':"Blaze",'EPIC':[200000,None,64,12],'LEGENDARY':[None]},{'name':"Blue Whale",'RARE':[900000,None,1,7],'EPIC':[9000000,None,8,12],'LEGENDARY':[None]},{'name':"Chicken",'RARE':[190000,None,0,1],'EPIC':[250000,None,8,1],'LEGENDARY':[None]},{'name':"Dolphin",'RARE':[10000000,None,0,7],'EPIC':[50000000,None,16,14],'LEGENDARY':[None]},{'name':"Elephant",'RARE':[900000,None,0,5],'EPIC':[14000000,None,0,10],'LEGENDARY':[None]},{'name':"Ender Dragon",'EPIC':[400000000,None,8,20],'LEGENDARY':[None]},{'name':"Enderman",'RARE':[10000,None,0,6],'EPIC':[40000000,None,8,12],'LEGENDARY':[None]},{'name':"Endermite",'RARE':[190000,None,0,3],'EPIC':[250000,None,512,7],'LEGENDARY':[None]},{'name':"Flying Fish",'RARE':[200000,None,0,5],'EPIC':[1000000,None,64,10],'LEGENDARY':[None]},{'name':"Ghoul",'EPIC':[5000000,None,512,10],'LEGENDARY':[None]},{'name':"Giraffe",'RARE':[900000,None,128,7],'EPIC':[9000000,None,512,12],'LEGENDARY':[None]},{'name':"Golem",'EPIC':[10000000,None,8,20],'LEGENDARY':[None]},{'name':"Guardian",'RARE':[500000,None,0,2],'EPIC':[3000000,None,64,5],'LEGENDARY':[None]},{'name':"Horse",'RARE':[190000,None,0,1],'EPIC':[250000,None,8,1],'LEGENDARY':[None]},{'name':"Hound",'EPIC':[5000000,None,512,10],'LEGENDARY':[None]},{'name':"Jellyfish",'EPIC':[15000000,None,16,10],'LEGENDARY':[None]},{'name':"Jerry",'RARE':[40000,None,1,1],'EPIC':[100000,None,1,3],'LEGENDARY':[None]},{'name':"Lion",'RARE':[900000,None,0,7],'EPIC':[14000000,None,1024,14],'LEGENDARY':[None]},{'name':"Magma Cube",'RARE':[10000,None,0,5],'EPIC':[500000,None,16,10],'LEGENDARY':[None]},{'name':"Megalodon",'EPIC':[10000000,None,0,20],'LEGENDARY':[None]},{'name':"Mithril Golem",'RARE':[25000,None,0,5],'EPIC':[50000,None,0,20],'LEGENDARY':[None]},{'name':"Monkey",'RARE':[900000,None,0,7],'EPIC':[17000000,None,0,12],'LEGENDARY':[None]},]

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
        print("Page Fail:", y)
        y += 1
    x.extend(d["auctions"])
    print("Page Success:", a)

sort = [items for items in x if not items['claimed'] and items["bin"] and "[Lvl" in items["item_name"]]

filtr = [{k: v for k, v in l.items() if k in ('uuid', 'auctioneer', 'start', 'end', 'item_name', 'item_lore', 'tier', 'starting_bid')} for l in sort]

user = str(input("Enter the Full Path Location where you want the Output to be made (C:\\Users): "))

with open(user+"\output.txt", "w") as f:
    print(str(filtr).encode("ascii","ignore").decode(), file=f)

print("Total Number of Pet Bins:",len(filtr))
