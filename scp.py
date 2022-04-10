import sqlite3
import time
import random

conn = sqlite3.connect('scp.db')
c = conn.cursor()
id = 0

def dynamic_data_entry():

    name = input ("Name: ")
    type = input ("Type: ")
    containmentClass = input ("Containment class:")
    disruptionClass = input("Disruption Class: ")
    riskClass = input ("Risk Class: ")
    groupsofinterest = input ("groups of interest: ")
    strength = input ("strength: ")
    dexterity = input ("dexterity: ")
    constitution = input ("constitution: ")
    wisdom = input ("Wisdom: ")
    intelligence = input("Intelligence: ")
    charisma = input("Charisma:  ")
    realityb = input("realityb:  ")
    mindb = input("Mindb:  ")
    egob = input("Egob:  ")
    descrition  = input("Descrition:  ")
    c.execute("INSERT INTO scp VALUES ( ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,? )",
          (id,name,type,containmentClass,disruptionClass,riskClass,groupsofinterest,strength,dexterity,constitution,wisdom,intelligence,charisma,realityb,mindb,egob,descrition))

    conn.commit()

    
for i in range(600):
    dynamic_data_entry()
    time.sleep(1)
    id += 1

c.close
conn.close()
