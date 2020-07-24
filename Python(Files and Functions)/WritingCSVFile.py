jobs=[("Joy", "25", "Machine Learning Engineer"), ("Alvee", "22","Student"),
        ("Piyal","35","Graduate")]
fhandle=open("Friends.csv", "w")
fhandle.write("Name,Age,Job"+'\n')
for job in jobs:
    fhandle.write("{},{},{}".format(job[0],job[1],job[2])+'\n')
fhandle.close()
