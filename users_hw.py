users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# Add a new user to the dictionary
users.update({"Steven": {
    "twitter": "flarephotos",
    "lottery_numbers": [2, 5, 7, 9, 21, 45],
    "home_town": "Haddington",
    "pets": [
      {
        "name": "Callie",
        "species": "dog"
      }
    ]
  }})


# users.update({"Steven"})

# Add a dog to Erik called Fluffy
# users["Erik"]["pets"][0]["dog"] = "Fluffy"
# print(users["Erik"]["pets"][0]["dog"])


# Change home town to Edinburgh for Erik
# users["Erik"]["home_town"] = "Edinburgh"
# print(users["Erik"]["home_town"])


# Amend lottery numbers for Erik to add the number 7
# ltamend = users["Erik"]["lottery_numbers"]
# print(ltamend)
# ltamend = ltamend + [7]
# print(ltamend)
# users["Erik"]["lottery_numbers"] = ltamend
# print(users["Erik"]["lottery_numbers"])

# Print Avril's even lottery numbers
# for num in users["Avril"]["lottery_numbers"]:
#     if num % 2 == 0:
#         print(num)


# Get Erik's smallest lottery number
# smallest = users["Erik"]["lottery_numbers"]
# smallest.sort()
# print(f"The smallest number in Erik's Lottery is {smallest[:1]}")