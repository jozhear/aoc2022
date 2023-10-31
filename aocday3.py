# v 1.0

values = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,
          'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26,
          'A':27,'B':28,'C':29,'D':30,'E':31,'F':32,'G':33,'H':34,'I':35,'J':36,'K':37,'L':38,'M':39,
          'N':40,'O':41,'P':42,'Q':43,'R':44,'S':45,'T':46,'U':47,'V':48,'W':49,'X':50,'Y':51,'Z':52}

def rucksacks(rucksacks):
    allRucksacks = []
    matchingLetters = []
    numbers = []
    sum = 0

    with open('values.txt') as f:
        for line in f.readlines():
            length = len(line)
            halfLine = length / 2
            firstHalf = line[:int(halfLine)]
            secondHalf = line[int(halfLine):]
            
            is_Looping = True
            for letter in firstHalf:
                for secondLetter in secondHalf:
                    if letter == secondLetter:
                        matchingLetters.append(letter)
                        is_Looping = False
                        break
                    else:
                        continue
                if not is_Looping:
                    break
        
        numbers = [values[letters] for letters in matchingLetters]
        
        for number in numbers:
            sum = sum + number
        return sum
        