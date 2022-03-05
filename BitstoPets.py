# WELCOME TO BITS-TO-PETS
# ----------------------------
# Here we Upgrade Pets using Bits to earn Profit

import requests
import sys
import json

pets = {'Ammonite':1,'Armadillo':5,'Baby Yeti':2,'Bal':2,'Bat':6,'Bee':5,'Black Cat':1,'Blaze':2,'Blue Whale':5,'Chicken':5,'Dolphin':5,'Elephant':5,'Ender Dragon':2,'Enderman':6,'Endermite':5,'Flying Fish':3,'Ghoul':2,'Giraffe':5,'Golden Dragon':1,'Golem':2,'Grandma Wolf':5,'Griffin':5,'Guardian':5,'Horse':5,'Hound':2,'Jellyfish':2,'Jerry':6,'Lion':5,'Magma Cube':5,'Megoladon':2,'Mithril Golem':5,'Monkey':5,'Ocelot':5,'Parrot':2,'Phoenix':2,'Pig':5,'Pigman':2,'Rabbit':5,'Rat':1,'Rock':5,'Scatha':5,'Sheep':5,'Silverfish':5,'Skeleton':5,'Skeleton Horse':1,'Snowman':1,'Spider':5,'Spirit':2,'Squid':5,'Tarantula':2,'Tiger':5,'Turtle':2,'Wither Skeleton':2,'Wolf':5,'Zombie':5}

data = requests.get("https://api.hypixel.net/skyblock/auctions?page=0")
d = data.json()

listings = ["item_name","item_lore"]
for l in d["auctions"]:
    if l["bin"]:
        for i in listings:
            print(i+" : ",l[i])
        print("-"*24)
