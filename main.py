from api_classifier import Genderize
genderize = Genderize()
while True:
    names = raw_input("Enter Names : (Break if you want to discontinue) ")
    names = names.split(' ')
    for name in names:
        flag, gender, prob = genderize.get_gender(name=name)
        if flag == 0:
            print "Name : " + name + "  ***  Gender : " + gender + "  *** probabilty : " + str(prob) + " *** "
        else:
            print "Sorry couldn't find the gender for the name : " + name
