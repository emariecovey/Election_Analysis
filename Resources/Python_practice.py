from re import L


counties = ["Arapahoe","Denver","Jefferson"]
#for county in counties:
 #   print(county)
#for i in range(len(counties)):
 #   print(counties[i])

#if "Arapahoe" in counties:
#    print("Arapahoe is in counties")
#else:
#    print("Arapahoe is not in countries")

counties_tuple = ("Arapahoe","Denver","Jefferson")
#for county in counties_tuple:
   # print(county)

#for i in range(len(counties_tuple)):
    #print(counties_tuple[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#for county in counties_dict:
    #print(counties_dict[county])

#for county in counties_dict:
   # print(counties_dict.get(county))

#for county,voters in counties_dict.items():
 #   print (county + 'county has ' + str(voters) + ' registered voters.')

#for county,voters in counties_dict.items():
 #   print (f"{county} county has {voters} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

#for i in range(len(voting_data)):
 #   print(voting_data[i]["county"])

#for county_dict in voting_data:
 #  print(county_dict["registered_voters"])

#candidate_votes = int(input("How many votes did the candidate get in the election? "))
#total_votes = int(input("What is the total number of votes in the election? "))
#message_to_candidate = (
 #   f"You recieved {candidate_votes:,} number of votes."
  #  f"The total number of votes in the election was {total_votes:,}."
   # f"You recieved {candidate_votes / total_votes * 100:.2f}% of the total votes.")
#print(message_to_candidate)

#for county in counties_dict:
 #   print(counties_dict.get(county))

fruitdict= {"banana":1, "apple":2, "orange":3}
#print(len(fruitdict))
fruitdict ["kiwi"]=4
fruitdict["guava"]=5
fruitdict.pop("guava")
#print(fruitdict)
#print(fruitdict.keys())
#print(fruitdict.values())
#print(fruitdict["banana"])
#print(fruitdict.get("banana"))
#print(fruitdict.items())

#THIS IS HOW YOU DECLARE A LIST OF DICTIONARIES
food_data = [{"fruit":"banana", "veg":"celery"}, {"fruit":"apple", "veg":"pepper"}, {"fruit":"orange", "veg":"bean"}]

#CHECKING LENGTH OF LIST OF DICTIONARIES
#print(len(food_data))

#THIS IS HOW YOU ADD TO A LIST OF DICTIONARIES:
food_data.append({"fruit":"kiwi", "veg":"broccoli"})

#THIS IS HOW YOU TAKE AWAY FROM A LIST OF DICTIONARIES
food_data.remove({"fruit":"kiwi", "veg":"broccoli"})
#print(food_data)

#THIS IS HOW YOU SEE KEYS IN DICTIONARY

#ELSE IF EXAMPLE
#happiness = int(input("How happy are you on a scale of 1 to 10?"))
#if happiness >= 8:
#    print("great")
#else:
#    if happiness >=4:
#        print("ok")
#    else:    
#        if happiness <4:
#            print("not good")

#ELIF EXAMPLE
#hunger = int(input("How hungry are you on a scale of 1 to 10?"))
#if hunger >=8:
#    print("famished")
#elif hunger >=4:
#    print ("somewhat hungry")
#elif hunger <4:
#    print ("not hungry")

#WHILE LOOP PRACTICE
#x = 0
#while x<=5:
#   print(x)
#    x = x + 1

#FOR LOOP PRACTICE with list
#for i in counties:
#    print(i)

#FOR LOOP PRACTICE with list and range
#for i in range(len(counties)):
#    print(counties[i])

#FOR LOOP PRACTICE WITH TUPLES AND RANGE
#for i in range(len(counties_tuple)):
#    print (counties_tuple[i]) 

#PRINTING KEYS FOR DICTIONARY (works in this one or the next set of code)
#for i in counties_dict:
#    print (i)

#for i in counties_dict.keys():
#    print(i)

#PRINTING VALUES OF DICTIONARY (works in this one or the next 2 sets of code)
#for i in counties_dict.values():
#    print(i)

#for i in counties_dict.keys():
#    print(counties_dict[i])

#for i in counties_dict.keys():
#    print(counties_dict.get(i))

#PRINTING KEYS AND VALUES OF DICTIONARY (works in this one or the next)
#for i in counties_dict.items():
#    print(i)

#for key,value in counties_dict.items():
#    print(key,value)

#HOW TO PRINT KEY,VALUE IN NICE WAY FROM DICTIONARY
#for key,value in counties_dict.items():
#    print(key + " county has " + str(value) + " registered voters.")

#HOW TO PRINT WHOLE LIST OF DICTIONARIES
#for i in food_data:
#    print(i)

#HOW TO GET JUST LIST OF VALUES FROM ONE KEY in a list of dictionaries
#for i in range(len(food_data)):
#    print(food_data[i]["fruit"])

#HOW TO GET ALL VALUES IN LIST in a list of dictionaries
#for i in food_data: #going into one of the individual dictionaries
#    for j in i.values(): #looking at values in individual dictionaries
#        print(j) #printing all the values in each dictionary

#print(fruitdict.items())

#PRINTING KEYS AND VALUES IN STATEMENT FORM WITH F-STRINGS (also next block of code)
#for fruit, preference in fruitdict.items():
#    print(f"{fruit} preference is {preference:,.3f}.")

#for i,j in counties_dict.items():
#    print(f"{i} county has {j:,} registered voters.")

#LAST SKILL DRILL ANSWER:
for i in voting_data:
    print (f"{i['county']}") #have to have f string when printing in list of dictionaries
    print(f"{i['county']} county has {i['registered_voters']:,} registered voters.")

#HOW TO GET JUST VALUE FOR ONE KEY AND THEN JUST VALUE FOR ANOTHER KEY
#go through each line, for each line (i) print the value of the county and print value of the voters
#if we wanted the key names, don't put brackets around county and registered voters
for i in voting_data:
    print (i["county"], i["registered_voters"])



