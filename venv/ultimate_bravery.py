import random

import champions
import items
import runes
import champions as champs
import summoner_spells
import summoner_spells as sums

# --- fix ---

# -------------- Global Variables --------------
mode = None
role = None
champ = None
sums = []
trees = []
keystone = None
general_runes1 = []
general_runes2 = []
starting_items = []
boots = ""
mythic_item = ""
support_item = ""
finish_items = []
# ----------------------------------------------

#main function
def ultimate_bravery():
    #get the game mode (aram or sr)
    get_mode()
    #get players role and select a random champion if in summoners rift
    if mode == "sr":
        get_role()
        select_champ()
    #choose random summoner spells
    select_sums()
    #choose random runes(trees, keystone, and runes)
    select_runes()
    #insert the keystone into the list of runes
    general_runes1.insert(0, keystone)
    select_items()


    if mode == "sr":
        print("\nChampion: " + champ)
        print("\nSpells:   " + sums[0] + " and " + sums[1])
        print("\nRunes:    " + str(general_runes1))
        print("          " + str(general_runes2))
        print("\nStarting Items: " + str(starting_items))
        print("\nFull Build:     " + str(finish_items))
    elif mode == "aram":
        print("\nSpells: " + sums[0] + " and " + sums[1])
        print("\nRunes:  " + str(general_runes1))
        print("        " + str(general_runes2))
        print("\nStarting Items: " + str(starting_items))
        print("\nFull Build:     " + str(finish_items))


#get game mode
def get_mode():
    #global vars
    global mode
    #what game mode?
    user_input = input("Are you playing ARAM or Summoner's Rift? ")
    game_mode = user_input.lower()
    #false by default to run the check
    valid = False
    #all of the possible inputs
    valid_inputs = ["aram", "howling abyss", "sr", "summoner's rift", "summoners rift", "rift"]
    # make sure it is a valid input
    while not valid:
        if game_mode in valid_inputs:
            valid = True
        else:
            game_mode = input("Invalid Input. Are you playing ARAM or Summoner's Rift? ")
    #set mode based on what player entered
    if game_mode == "aram" or game_mode == "howling abyss":
        mode = "aram"
    elif game_mode == "sr" or game_mode == "summoner's rift" or game_mode == "summoners rift" or game_mode == "rift":
        mode = "sr"
    return


#get lane
def get_role():
    #global vars
    global role
    #select lane
    user_input = input("What lane are you in? ")
    lane = user_input.lower()
    #input check
    valid = False
    valid_inputs = [
        "top", "t",
        "jungle", "jung", "jg", "j",
        "middle", "mid", "m",
        "bottom", "bot", "b", "adc", "a",
        "support", "supp", "sup", "s"]
    while not valid:
        if lane in valid_inputs:
            valid = True
        else:
            lane = input("Invalid input. What lane are you in? ")
    #set role based on what user entered
    if lane == "top" or lane == "t":
        role = "top"
    elif lane == "jungle" or lane == "jung" or lane == "jg" or lane == "j":
        role = "jungle"
    elif lane == "middle" or lane == "mid" or lane == "m":
        role = "mid"
    elif lane == "bottom" or lane == "bot" or lane == "b" or lane == "adc" or lane == "a":
        role = "adc"
    elif lane == "support" or lane == "supp" or lane == "sup" or lane == "s":
        role = "support"
    return


#select a random champion
def select_champ():
    #global vars
    global champ
    #select a random champion and store it in champ variable
    champ = random.choice(champions.champions)
    return


#select random summoner spells
def select_sums():
    #global vars
    global sums
    global role
    global mode
    a = ""
    b = ""
    #if it is aram, use aram sums
    if mode == "aram":
        #make sure choices aren't the same
        while a == b:
            a = random.choice(summoner_spells.aram_spells)
            b = random.choice(summoner_spells.aram_spells)
        #add to sums[]
        sums.append(a)
        sums.append(b)
    elif mode == "sr":
        # jungler take smite
        if role == "jungle":
            sums.append("Smite")
            sums.append(random.choice(summoner_spells.summoner_spells))
        else:
            #make sure choices aren't the same
            while a == b:
                a = random.choice(summoner_spells.summoner_spells)
                b = random.choice(summoner_spells.summoner_spells)
            #add to sums[]
            sums.append(a)
            sums.append(b)
    return


#select random runes
def select_runes():
    global general_runes1
    global general_runes2
    select_trees()
    select_keystone()
    select_general_runes()
    if "Flash" not in sums:
        while "Hextech Flashtraption" in general_runes1 or "Hextech Flashtraption" in general_runes2:
            general_runes1 = []
            general_runes2 = []
            select_general_runes()
    return


#select random 2 trees for runes
def select_trees():
    #global vars
    global trees
    a = ""
    b = ""
    #make sure they aren't the same
    while a == b:
        a = random.choice(runes.rune_tree)
        b = random.choice(runes.rune_tree)
    #add the random trees to trees[]
    trees.append(a)
    trees.append(b)
    return


#select a random keystone from the first tree
def select_keystone():
    #global var
    global keystone
    #choose a random keystone depending on the first random tree selected in select_trees()
    if trees[0] == "Precision":
        keystone = random.choice(runes.precision_keystones)
    elif trees[0] == "Domination":
        keystone = random.choice(runes.domination_keystones)
    elif trees[0] == "Sorcery":
        keystone = random.choice(runes.sorcery_keystones)
    elif trees[0] == "Resolve":
        keystone = random.choice(runes.resolve_keystones)
    elif trees[0] == "Inspiration":
        keystone = random.choice(runes.inspiration_keystones)
    return


#select random general runes for both trees
#domination and sorcery trees require seperate aram runes, due to some options not being available
def select_general_runes():
    #global vars
    global general_runes1
    global general_runes2
    # ------ First Tree ------------
    if trees[0] == "Precision":
        get_precision(general_runes1)
    elif trees[0] == "Domination":
        if mode == "aram":
            get_domination_aram(general_runes1)
        else:
            get_domination(general_runes1)
    elif trees[0] == "Sorcery":
        if mode == "aram":
            get_sorcery_aram(general_runes1)
        else:
            get_sorcery(general_runes1)
    elif trees[0] == "Resolve":
        get_resolve(general_runes1)
    elif trees[0] == "Inspiration":
        get_inspiration(general_runes1)
    # ---------  Second Tree ------------
    if trees[1] == "Precision":
        get_precision(general_runes2)
    elif trees[1] == "Domination":
        if mode == "aram":
            get_domination_aram(general_runes2)
        else:
            get_domination(general_runes2)
    elif trees[1] == "Sorcery":
        if mode == "aram":
            get_sorcery_aram(general_runes2)
        else:
            get_sorcery(general_runes2)
    elif trees[1] == "Resolve":
        get_resolve(general_runes2)
    elif trees[1] == "Inspiration":
        get_inspiration(general_runes2)
    return


def get_precision(list):
    list.append(random.choice(runes.precision_runes[0]))
    list.append(random.choice(runes.precision_runes[1]))
    list.append(random.choice(runes.precision_runes[2]))


def get_domination(list):
    list.append(random.choice(runes.domination_runes[0]))
    list.append(random.choice(runes.domination_runes[1]))
    list.append(random.choice(runes.domination_runes[2]))


def get_domination_aram(list):
    list.append(random.choice(runes.domination_aram[0]))
    list.append(random.choice(runes.domination_aram[1]))
    list.append(random.choice(runes.domination_aram[2]))


def get_sorcery(list):
    list.append(random.choice(runes.sorcery_runes[0]))
    list.append(random.choice(runes.sorcery_runes[1]))
    list.append(random.choice(runes.sorcery_runes[2]))


def get_sorcery_aram(list):
    list.append(random.choice(runes.sorcery_aram[0]))
    list.append(random.choice(runes.sorcery_aram[1]))
    list.append(random.choice(runes.sorcery_aram[2]))


def get_resolve(list):
    list.append(random.choice(runes.resolve_runes[0]))
    list.append(random.choice(runes.resolve_runes[1]))
    list.append(random.choice(runes.resolve_runes[2]))


def get_inspiration(list):
    list.append(random.choice(runes.inspiration_runes[0]))
    list.append(random.choice(runes.inspiration_runes[1]))
    list.append(random.choice(runes.inspiration_runes[2]))


def select_items():
    #global vars
    global finish_items
    select_starting_items()
    select_legendary()
    select_boots()
    select_mythic()


    #generate a random number between 1 and 50
    a = random.randint(1,50)

    finish_items[0] = mythic_item
    finish_items[1] = boots
    if "Tear of the Goddess" in starting_items:
        x = random.choice(items.unique_mana_charge)
        finish_items[2] = x
    if "Dark Seal" in starting_items:
        finish_items[2] = "Mejai's Soulstealer"
    if role == "support":
        finish_items[2] = support_item
        if a == 22 and mode == "sr":
            finish_items[3] = "Watchful Wardstone"


def select_starting_items():
    #global vars
    global starting_items
    global support_item
    a = ""
    x = random.randint(1, 25)
    if mode == "sr":
        if role == "support":
            item = random.choice(items.support_items)
            starting_items.append(item)
            support_item = item
            if x == 5:
                starting_items.append("Control Ward")
            else:
                starting_items.append("Health Potion x2")
        elif role == "jungle":
            starting_items.append(random.choice(items.jungle_items))
            if x == 5:
                starting_items.append("Control Ward")
                starting_items.append("Health Potion")
            elif x == 10:
                starting_items.append("Control Ward x2")
            else:
                starting_items.append("Refillable Potion")
        else:
            if x == 22:
                starting_items.append("Corrupting Potion")
            else:
                a = random.choice(items.starting_items)
                if a == "Dark Seal":
                    starting_items.append(a)
                    if x == 5:
                        starting_items.append("Control Ward")
                        starting_items.append("Health Potion")
                    elif x == 10:
                        starting_items.append("Control Ward x2")
                    else:
                        starting_items.append("Refillable Potion")
                elif a == "Tear of the Goddess" or a == "Doran's Ring":
                    starting_items.append(a)
                    if x == 7:
                        starting_items.append("Control Ward")
                    else:
                        starting_items.append("Health Potion x2")
                else:
                    starting_items.append(a)
                    starting_items.append("Health Potion")
    else:
        starting_items.append(random.choice(items.aram_items))
        starting_items.append("Boots")
        starting_items.append("Refillable Potion")
    return


def select_boots():
    global boots
    boots = random.choice(items.boots)
    return


def select_mythic():
    global mythic_item
    mythic_item = random.choice(items.mythic_items)
    return


def select_legendary():
    global finish_items
    count = 1
    sr_only_items = ["Guardian Angel", "Mejai's Soulstealer"]
    if mode == "aram":
        while count <= 6:
            a = random.choice(items.legendary_items)
            while a in finish_items:
                a = random.choice(items.legendary_items)
            while a in items.unique_hydra and items.unique_hydra in finish_items:
                a = random.choice(items.legendary_items)
            while a in items.unique_qss and items.unique_qss in finish_items:
                a = random.choice(items.legendary_items)
            while a in items.unique_lifeline and items.unique_lifeline in finish_items:
                a = random.choice(items.legendary_items)
            while a in items.unique_crit_modifier and items.unique_crit_modifier in finish_items:
                a = random.choice(items.legendary_items)
            while a in items.unique_last_whisper and items.unique_last_whisper in finish_items:
                a = random.choice(items.legendary_items)
            if a not in sr_only_items:
                finish_items.append(a)
                count += 1
    else:
        while count <= 6:
            x = random.choice(items.legendary_items)
            while x in finish_items:
                x = random.choice(items.legendary_items)
                while x in finish_items:
                    x = random.choice(items.legendary_items)
                while x in items.unique_hydra and items.unique_hydra in finish_items:
                    x = random.choice(items.legendary_items)
                while x in items.unique_qss and items.unique_qss in finish_items:
                    x = random.choice(items.legendary_items)
                while x in items.unique_lifeline and items.unique_lifeline in finish_items:
                    x = random.choice(items.legendary_items)
                while x in items.unique_crit_modifier and items.unique_crit_modifier in finish_items:
                    x = random.choice(items.legendary_items)
                while x in items.unique_last_whisper and items.unique_last_whisper in finish_items:
                    x = random.choice(items.legendary_items)
            finish_items.append(x)
            count += 1

    return

ultimate_bravery()


# aram mode?    /
# if not, user selects a role   /
# select a random champion   /
# select random summoner spells   /
# select random keystone     /
# select random runes     /
# add necessary support item
# add random boots
# select random items