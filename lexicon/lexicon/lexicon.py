# thought: API call to dictonary service to test words instead of using a local tuple
myTuple = [('direction', 'north'),('direction', 'south'),('direction', 'east'),('verb','go'),
                        ('verb','kill'),('verb','eat'),('stop','the'),
                        ('stop','in'),('stop','of'),('noun','bear'),('noun','princess'),
                        ('number',3),('number',1234)]

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return s.lower()

def scan(stuff):
    words = stuff.split()
    r = []
    e = []
    rx =[]
    cWords = []
    for word in words:
       
        cWords.append(convert_number(word))
       
    r = list(filter(lambda w: w[1] in cWords, myTuple))  #THIS WORKS, but is unordered.
   
    
    if len(r) < len(cWords):
        for i in range(0,len(r)):
            rx.append(r[i][1])
        e = [i for i in cWords if not i in rx]
    else:
        if len(r) > len(cWords):
            print('I see you')
    for i in range(0,len(e)):
        r.append(('error',e[i]))   

    r.sort(key=lambda x: cWords.index(x[1]))  # had to sort r based on cWords for automated tests to pass

    return r           
stuffing = input('$> ')
result = scan(stuffing)
print(result)

#'kill the asdf north princess 3'