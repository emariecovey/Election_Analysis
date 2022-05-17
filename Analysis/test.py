

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
print(type(voting_data))
#print all dictionary
for i in voting_data:
    if i["registered_voters"] == 463353:
        print(i["county"])