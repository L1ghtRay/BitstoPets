# WELCOME TO BITS-TO-PETS
# ----------------------------
# Here we Upgrade Pets using Bits to earn Profit

import requests
import json
import tabulate

pets = {
    'Armadillo': {
        'EPIC': {'AH': [None, 0], 'KAT': 5, 'COST': 1000000, 'MAT': [None,0,0]},
        'LEGENDARY': {'AH': [None, 0]}},
    'Bal': {
        'EPIC': {'AH': [None, 0], 'KAT': 10, 'COST': 2000000, 'MAT': ['YOGGIE', 100]},
        'LEGENDARY': {'AH': [None, 0]}},
    'Bat': {
        'RARE': {'AH': [None, 0], 'KAT': 1, 'COST': 190000, 'MAT': [None,0,0]},
        'EPIC': {'AH': [None, 0], 'KAT': 3, 'COST': 250000, 'MAT': ['ENCHANTED_RED_MUSHROOM', 64]},
        'LEGENDARY': {'AH': [None, 0]}},
    'Bee': {
        'EPIC': {'AH': [None, 0], 'KAT': 3, 'COST': 450000, 'MAT': ['ENCHANTED_GOLD_BLOCK', 9]},
        'LEGENDARY': {'AH': [None, 0]}},
    'Blaze': {
        'EPIC': {'AH': [None, 0], 'KAT': 12, 'COST': 250000, 'MAT': ['ENCHANTED_BLAZE_ROD', 64]},
        'LEGENDARY': {'AH': [None, 0]}},
    'Blue Whale': {
        'RARE': {'AH': [None, 0], 'KAT': 7, 'COST': 900000, 'MAT': ['ENCHANTED_COOKED_FISH', 1]},
        'EPIC': {'AH': [None, 0], 'KAT': 12, 'COST': 9000000, 'MAT': ['ENCHANTED_COOKED_FISH', 8]},
        'LEGENDARY': {'AH': [None, 0]}},
    'Chicken': {
        'EPIC': {'AH': [None, 0], 'KAT': 1, 'COST': 250000, 'MAT': ['ENCHANTED_RAW_CHICKEN', 8]},
        'LEGENDARY': {'AH': [None, 0]}},
    'Elephant': {
        'RARE': {'AH': [None, 0], 'KAT': 7, 'COST': 900000, 'MAT': [None,0,0]},
        'EPIC': {'AH': [None, 0], 'KAT': 12, 'COST': 14000000, 'MAT': [None,0,0]},
        'LEGENDARY': {'AH': [None, 0]}},
    'Endermite': {
        'EPIC': {'AH': [None, 0], 'KAT': 7, 'COST': 250000, 'MAT': ['ENCHANTED_ENDSTONE', 512]},
        'LEGENDARY': {'AH': [None, 0]}},
    'Flying Fish': {
        'EPIC': {'AH': [None, 0], 'KAT': 10, 'COST': 1000000, 'MAT': ['ENCHANTED_RAW_FISH', 64]},
        'LEGENDARY': {'AH': [None, 0], 'KAT': 1, 'COST': 1000000, 'MAT': ['Radioactive Vial', 1]},
        'MYTHIC': {'AH': [None, 0]}},
    'Guardian': {
        'RARE': {'AH': [None, 0], 'KAT': 2, 'COST': 500000, 'MAT': [None,0,0]},
        'EPIC': {'AH': [None, 0], 'KAT': 5, 'COST': 3000000, 'MAT': ['ENCHANTED_PRISMARINE_SHARD', 64]},
        'LEGENDARY': {'AH': [None, 0]}},
    'Horse': {
        'EPIC': {'AH': [None, 0], 'KAT': 1, 'COST': 250000, 'MAT': ['ENCHANTED_LEATHER', 8]},
        'LEGENDARY': {'AH': [None, 0]}},
    'Jellyfish': {
        'EPIC': {'AH': [None, 0], 'KAT': 10, 'COST': 15000000, 'MAT': ['ENCHANTED_SLIME_BALL', 16]},
        'LEGENDARY': {'AH': [None, 0]}},
    'Jerry': {
        'EPIC': {'AH': [None, 0], 'KAT': 3, 'COST': 100000, 'MAT': ['MOVE_JERRY_EGG', 1, 0]},
        'LEGENDARY': {'AH': [None, 0]}},
    'Lion': {
        'RARE': {'AH': [None, 0], 'KAT': 7, 'COST': 900000, 'MAT': [None,0,0]},
        'EPIC': {'AH': [None, 0], 'KAT': 12, 'COST': 14000000, 'MAT': ['ENCHANTED_RAW_BEEF', 1024]},
        'LEGENDARY': {'AH': [None, 0]}},
    'Magma Cube': {
        'RARE': {'AH': [None, 0], 'KAT': 5, 'COST': 10000, 'MAT': [None,0,0]},
        'EPIC': {'AH': [None, 0], 'KAT': 10, 'COST': 500000, 'MAT': ['ENCHANTED_MAGMA_CREAM', 16]},
        'LEGENDARY': {'AH': [None, 0]}},
    'Mithril Golem': {
        'EPIC': {'AH': [None, 0], 'KAT': 10, 'COST': 200000, 'MAT': [None,0,0]},
        'LEGENDARY': {'AH': [None, 0]}},
    'Monkey': {
        'RARE': {'AH': [None, 0], 'KAT': 7, 'COST': 900000, 'MAT': [None,0,0]},
        'EPIC': {'AH': [None, 0], 'KAT': 12, 'COST': 17000000, 'MAT': [None,0,0]},
        'LEGENDARY': {'AH': [None, 0]}},
    'Ocelot': {
        'EPIC': {'AH': [None, 0], 'KAT': 5, 'COST': 250000, 'MAT': ['ENCHANTED_JUNGLE_LOG', 512]},
        'LEGENDARY': {'AH': [None, 0]}},
    'Parrot': {
        'EPIC': {'AH': [None, 0], 'KAT': 10, 'COST': 15000000, 'MAT': ['ENCHANTED_FEATHER', 16]},
        'LEGENDARY': {'AH': [None, 0]}},
    'Pig': {
        'EPIC': {'AH': [None, 0], 'KAT': 1, 'COST': 250000, 'MAT': ['PORK', 512]},
        'LEGENDARY': {'AH': [None, 0]}},
    'Pigman': {
        'EPIC': {'AH': [None, 0], 'KAT': 10, 'COST': 250000, 'MAT': ['ENCHANTED_GRILLED_PORK', 8]},
        'LEGENDARY': {'AH': [None, 0]}},
    'Rabbit': {
        'EPIC': {'AH': [None, 0], 'KAT': 1, 'COST': 250000, 'MAT': ['RABBIT', 64]},
        'LEGENDARY': {'AH': [None, 0]}},
    'Sheep': {
        'EPIC': {'AH': [None, 0], 'KAT': 7, 'COST': 250000, 'MAT': ['ENCHANTED_MUTTON', 512]},
        'LEGENDARY': {'AH': [None, 0]}},
    'Silverfish': {
        'EPIC': {'AH': [None, 0], 'KAT': 3, 'COST': 250000, 'MAT': ['ENCHANTED_COBBLESTONE', 64]},
        'LEGENDARY': {'AH': [None, 0]}},
    'Skeleton': {
        'EPIC': {'AH': [None, 0], 'KAT': 3, 'COST': 250000, 'MAT': ['ENCHANTED_BONE', 128]},
        'LEGENDARY': {'AH': [None, 0]}},
    'Spider': {
        'EPIC': {'AH': [None, 0], 'KAT': 7, 'COST': 250000, 'MAT': ['ENCHANTED_STRING', 512]},
        'LEGENDARY': {'AH': [None, 0]}},
    'Squid': {
        'RARE': {'AH': [None, 0], 'KAT': 2, 'COST': 500000, 'MAT': [None,0,0]},
        'EPIC': {'AH': [None, 0], 'KAT': 5, 'COST': 3000000, 'MAT': ['ENCHANTED_INK_SACK', 64]},
        'LEGENDARY': {'AH': [None, 0]}},
    'Tiger': {
        'EPIC': {'AH': [None, 0], 'KAT': 12, 'COST': 14000000, 'MAT': ['ENCHANTED_RAW_CHICKEN', 1024]},
        'LEGENDARY': {'AH': [None, 0]}},
    'Wither Skeleton': {
        'EPIC': {'AH': [None, 0], 'KAT': 5, 'COST': 250000, 'MAT': ['ENCHANTED_COAL_BLOCK', 8]},
        'LEGENDARY': {'AH': [None, 0]}},
    'Wolf': {
        'EPIC': {'AH': [None, 0], 'KAT': 5, 'COST': 250000, 'MAT': ['ENCHANTED_SPRUCE_LOG', 512]},
        'LEGENDARY': {'AH': [None, 0]}},
    'Zombie': {
        'EPIC': {'AH': [None, 0], 'KAT': 10, 'COST': 250000, 'MAT': ["Zombie's Heart", 8]},
        'LEGENDARY': {'AH': [None, 0]}}
    }

url = "https://api.hypixel.net/skyblock/auctions?page="
ini = requests.get(url+"0")
ini_d = ini.json()
totalpg = ini_d['totalPages']
print('Total Number of Pages: 0 ->',totalpg-1)
ah = []
for a1 in range(totalpg):
    data = requests.get(url+str(a1))
    d = data.json()
    c = 1
    while not d['success']:
        data = requests.get(url+str(a1))
        d = data.json()
        print("[FAIL] :", c)
        c += 1
    if c>100:
        ah = []
        c = 1
        a1 = 0
        data = requests.get(url+"0")
        totalpg = data['totalPages']
    ah.extend(d["auctions"])
    print("[SUCCESS] Page:", a1)

def ahitem(i):
    global ah
    l = None
    y = [items for items in ah if not items['claimed'] and items["bin"] and i in items["item_name"]]
    z = [{key: d[key] for key in ['item_name', 'tier', 'starting_bid', 'uuid']} for d in y]
    for j in z:
        if l==None or l>j['starting_bid']:
            l = j['starting_bid']
    return l
    
sort = [items for items in ah if not items['claimed'] and items["bin"] and "[Lvl" in items["item_name"]]

fltr = [{key: val[key] for key in ['item_name', 'tier', 'starting_bid', 'uuid']} for val in sort]

for flt in fltr:
    for ptn in pets.keys():
        if ptn in flt['item_name']:
            if flt['tier'] in pets[ptn].keys():
                if pets[ptn][flt['tier']]['AH'][1]==0 or (flt['starting_bid'] / pets[ptn][flt['tier']]['AH'][0])<=1.1:
                    ahc = pets[ptn][flt['tier']]['AH'][1]+1
                    pets[ptn][flt['tier']]['AH'][1] = ahc
                    if pets[ptn][flt['tier']]['AH'][0]==None or flt['starting_bid'] < pets[ptn][flt['tier']]['AH'][0]:
                        pets[ptn][flt['tier']]['AH'][0] = flt['starting_bid']
print('[SUCCESS] Pet Prices')

pets['Flying Fish']['LEGENDARY']['MAT'].append(ahitem('Radioactive Vial'))
pets['Zombie']['EPIC']['MAT'].append(ahitem("Zombie's Heart"))

bz = requests.get("https://api.hypixel.net/skyblock/bazaar")
bzs = bz.json()
while not bzs['success']:
    bz = requests.get("https://api.hypixel.net/skyblock/bazaar")
    bzs = bz.json()
bz = bzs['products']

p1 = {}
for bzi in bz:
    if bzi in ['ENCHANTED_RAW_SALMON','YOGGIE','ENCHANTED_RED_MUSHROOM','ENCHANTED_COAL_BLOCK','ENCHANTED_GOLD_BLOCK','ENCHANTED_BLAZE_ROD','ENCHANTED_COOKED_FISH','ENCHANTED_RAW_CHICKEN','SUMMONING_EYE','ENCHANTED_ENDSTONE','ENCHANTED_RAW_FISH','REVENANT_FLESH','ENCHANTED_PRISMARINE_SHARD','ENCHANTED_LEATHER','ENCHANTED_SLIME_BALL','ENCHANTED_RAW_BEEF','ENCHANTED_MAGMA_CREAM','ENCHANTED_JUNGLE_LOG','ENCHANTED_FEATHER','PORK','ENCHANTED_GRILLED_PORK','RABBIT','ENCHANTED_MUTTON','ENCHANTED_COBBLESTONE','ENCHANTED_BONE','ENCHANTED_STRING','ENCHANTED_INK_SACK','ENCHANTED_SPRUCE_LOG']:
        p1.update({bzi :bz[bzi]['quick_status']['buyPrice']})

for pr in p1:
    for ptn in pets:
        for ptr in pets[ptn]:
            if 'MAT' in pets[ptn][ptr].keys() and len(pets[ptn][ptr]['MAT'])>0 and pets[ptn][ptr]['MAT'][0]==pr:
                pets[ptn][ptr]['MAT'].append(p1[pr])
print('[SUCCESS] Material Prices\n')

pettab = []

def bits(nam,rar):
    global pets
    global pettab
    if 'MAT' in pets[nam][rar].keys() and pets[nam][rar]['AH'][1]!=0 and pets[nam][rar]['MAT'][2]!=None:
        if rar=='RARE':
            rar1 = 'EPIC'
        if rar=='EPIC':
            rar1 = 'LEGENDARY'
        if rar=='LEGENDARY':
            rar1 = 'MYTHIC'
        matc = pets[nam][rar]['MAT'][1]
        matp = pets[nam][rar]['MAT'][2]
        matn = pets[nam][rar]['MAT'][0]
        petc1 = pets[nam][rar]['AH'][1]
        petc2 = pets[nam][rar1]['AH'][1]
        basp = pets[nam][rar]['COST']
        ktf = pets[nam][rar]['KAT']
        ahp1 = pets[nam][rar]['AH'][0]
        ahp2 = pets[nam][rar1]['AH'][0]
        vwah = pets[nam][rar]['AH'][1]
        bit = (ahp2-((ahp1+basp)+(matc*matp)))/(ktf*500)
        if matn==None:
            temptab = [nam,rar1,round(bit,1),ahp1,ahp2,str(petc1)+' | '+str(petc2),'-']
        else:
            temptab = [nam,rar1,round(bit,1),ahp1,ahp2,str(petc1)+' | '+str(petc2),str(matc)+' x '+matn+' = '+str(round(matc*matp))+' | '+str(ktf)]
        pettab.append(temptab)

for nam in pets:
    for rar in pets[nam]:
        bits(nam,rar)

pettab.sort(key=lambda x:x[2],reverse=True)
head = ['Pet','Rarity','Coins/Bit','Pet Buy Price','Pet Sell Price','BPC | SPC','Materials | Roses']

print(tabulate.tabulate(pettab,headers=head,tablefmt='grid'))
