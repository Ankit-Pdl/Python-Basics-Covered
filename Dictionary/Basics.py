
#! List TUples Sets Dictionary

#! key values

# userInfo = ["abhinav", 21,"Pepsicola"]
# userInfo[0]

# users = {
#     "name":"Abhinav",
#     "Age": 21,
#     "address":"anamnagar"
# }

# print(users["name"])

# users ={
#     "name":"Anamika",
#     "passion":{
#         "outdoor": "football",
#         "indoor":"CHess"
#     }

# }
# print(users["passion"]["outdoor"])

response ={
    "status": "success",
    "user":{
        "id":578,
        "username": "Anamika",
        "email":"abc@yahoo.com"
    }
}


name = response["user"]["username"]
print(name)

response["user"]["username"]= "Ankit"
print(response["user"]["username"])