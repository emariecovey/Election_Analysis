

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

#data is a list of dictionaries
print(type(voting_data))

#If there are 463353 registered voters, the county is denver
for i in voting_data:
    if i["registered_voters"] == 463353:
        print(i["county"])

#Print county name and number of registered voters
for key in voting_data:
    print(f"{key['county']} county has {key['registered_voters']} registered voters.")





