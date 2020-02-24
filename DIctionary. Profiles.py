dic = {"Zhassulan": 18, "Dastan":17, 
       "Siakhan":15, "Ansagan": 16}
dic1 = {"Zhassulan" : [18, 'male', 'programmer'],
        "Dastan": [17, 'male', 'graduate student'],
        "Siakhan": [15, 'female', 'college student'],
        "Ansagan": [16, 'female', 'highschool student']}

for key in dic1:
    print "Name: "+key
    print "Age: "+str(dic1[key][0])
    print "Gender: "+str(dic1[key][1])
    print "Occupation: "+str(dic1[key][2])
