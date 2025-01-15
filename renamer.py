'''
phonetic hash
just add your own adj, verbs and names
it will rename every file with a unique (not guaranteed but highly likely) filename with the same structure
'''

import random
import os

def main():
    formatname = input(">> which file format? enter such: txt \n")
    for file in os.listdir():
        if file.endswith(formatname):
            os.rename(file, f"{rndfilename()}.{formatname}")


def rndfilename():
    adjectives = ["Brave", "Clever", "Fierce", "Quick", "Bold", "Quiet", "Loyal", "Noble", "Strong", "Sharp", "Calm", "Daring", "Gentle", "Wise", "Mighty", "Cunning", "Swift", "Brilliant", "Fearless", "Honest", "Patient", "Agile", "Diligent", "Radiant", "Vigilant", "Sturdy", "Fiery", "Bold", "Curious","Humble", "Jovial", "Keen", "Luminous", "Majestic", "Persistent", "Resilient", "Serene", "Tenacious","Unwavering", "Valiant", "Zesty", "Eager", "Inventive", "Prudent", "Sincere", "Truthful", "Vibrant", "Witty"]
    verbs = ["Running","Jumping", "Flying", "Dashing", "Exploring", "Building", "Guarding", "Crafting", "Hunting", "Searching","Swimming", "Climbing", "Dancing", "Hiding", "Sprinting", "Riding", "Lifting", "Writing", "Fighting","Shouting", "Singing", "Speaking", "Teaching", "Learning", "Painting", "Drinking", "Celebrating", "Escaping","Helping", "Marching", "Baking", "Weaving", "Forging", "Drawing", "Rescuing", "Healing", "Discovering", "Scouting", "Crafting", "Chasing", "Repairing", "Organizing", "Plotting", "Planning", "Training", "Dodging", "Casting"]
    names = ["Hermione", "Gonagall", "Missandei", "Daenerys", "Cersei","Sansa", "Brienne", "Ygritte", "Bellatrix", "Cho", "Fleur", "Ginny", "Parvati","Luna","Minerva","Lily", "Narcissa","Sybill","Helga","Katie","Bathilda","Irma","Romilda","Angelina","Alicia"]
    return f"{random.choice(adjectives)}{random.choice(verbs)}{random.choice(names)}"



#main()
if __name__ == "__main__":
    main()
