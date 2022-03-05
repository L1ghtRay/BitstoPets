# WELCOME TO BITS-TO-PETS
# ----------------------------
# Here we Upgrade Pets using Bits to earn Profit

import requests
import sys
import json

pets = ['Ammonite','Armadillo','Baby Yeti','Bal','Bat','Bee','Black Cat','Blaze','Blue Whale','Chicken','Dolphin','Elephant','Ender Dragon','Enderman','Endermite','Flying Fish','Ghoul','Giraffe','Golden Dragon','Golem','Grandma Wolf','Griffin','Guardian','Horse','Hound','Jellyfish','Jerry','Lion','Magma Cube','Megoladon','Mithril Golem','Monkey','Ocelot','Parrot','Phoenix','Pig','Pigman','Rabbit','Rat','Rock','Scatha','Sheep','Silverfish','Skeleton','Skeleton Horse','Snowman','Spider','Spirit','Squid','Tarantula','Tiger','Turtle','Wither Skeleton','Wolf','Zombie']

data = requests.get("https://api.hypixel.net/skyblock/auctions")
d = data.json()

sort = [items for items in d["auctions"] if items["bin"] and items["category"] == "misc" and "[Lvl" in items["item_name"]]

with open("F:\Coding\Python\BitstoPets\output.txt", "w") as f:
    print(str(sort).encode("ascii","ignore").decode(), file=f)
