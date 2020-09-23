# key value

# 41 => kocaeli 34 => istanbul

sehirler = ["kocaeli","istanbul"]

plakalar = [41,34]

print(plakalar[sehirler.index("istanbul")])

#print(plakaler["istanbul"]) => 34

plakalar= {"kocaeli": 41 , "istanbul":34 }

print(plakalar["kocaeli"])
print(plakalar["istanbul"])

plakalar["ankara"] = 6

print(plakalar)

plakalar["kocaeli"] = "kırk bir"

print(plakalar)

users = {"omer can durmus":{"age":20 , "mail":"omeardurmus@gmail.com" , "adres":"bursa" } ,

        "taha polat":{"age":21,"mail":"tahapol06@gmail.com","adres":"bursa"}

}

print(users)
print(users["omer can durmus"])
print(users["omer can durmus"]["mail"])
 