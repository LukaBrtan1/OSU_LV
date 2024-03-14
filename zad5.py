data = open('SMSSpamCollection.txt')
lines_ham = 0
lines_spam = 0
broj_rijeci_ham = 0
broj_rijeci_spam = 0
broj_usklicnika = 0

for line in data:
       line = line.strip()
       line = line.lower()
       words = line.split()

       if words[0] == "ham":
            broj_rijeci_ham = broj_rijeci_ham + (len(words)-1)
            lines_ham = lines_ham + 1
       elif words[0] == "spam":
            broj_rijeci_spam = broj_rijeci_spam + (len(words)-1)
            lines_spam = lines_spam + 1
            if words[-1].endswith('!'):
                    broj_usklicnika = broj_usklicnika + 1

data.close()
                   
print('Prosjecan broj rijeci ham poruke: ', broj_rijeci_ham/lines_ham)
print('Prosjecan broj rijeci spam poruke:', broj_rijeci_spam/lines_spam)
print('Broj spam poruka koje zavrsavaju usklicnikom', broj_usklicnika)
