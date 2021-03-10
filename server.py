import select
import random
import time
import socket

no_clients = 3
score_max = 5
SERVER_PORT = 1644

Question = [" Name the currency used in Japan ? \n a.Taka b.Dinar c.Yen d.Ngultrum",
    " Which colors must be mixed together to make green ? \n a.Orange blue b.Red blue c.Blue yellow d.Black yellow",
    " In which country is Leaning tower of Pisa loctaed ? \n a.Italy b.England c.Spain d.France",
    " Which animal is the tallest in the world ? \n a.Elephant b.Giraffe c.Kangaroo d.Zebra",
    " How many bones does an adult human have? \n a.212 b.208 c.201 d.206",
    " How many dots are on one six sided die? \n a.17 b.18 c.21 d.14",
    " What element does not exist? \n a.Xf b.Re c.Si d.Pa",
    " How many states are there in India? \n a.24 b.29 c.30 d.31",
    " What is the day after Christmas commonly known as ? \n a.Boxing day b.Shopping day c.Prayer day d.Caroling day",
    " Name the fictional city batman calls home ? \n a.Springfield b.Metropolis c.Gotham d.Star city",
    " Who was the first Indian female astronaut ? \n a.Sunita Williams b.Kalpana Chawla c.Barbara Morgan d.Both of them ",
    " What is the smallest continent? \n a.Asia b.Antarctic c.Africa d.Australia",
    " The beaver is the national embelem of which country? \n a.Zimbabwe b.Iceland c.Argentina d.Canada",
    " How many players are on the field in baseketball? \n a.6 b.7 c.5 d.8",
    " He stands for? \n a.Helium b.Hulgerium c.Argenine d.Halfnium",
    " Can octopuses change their color ? \n a.NO b.YES c.Depends d.Don't know",
    " Which planet is closest to the sun? \n a.Mercury b.Pluto c.Earth d.Jupiter",
    " Who wrote Hamlet ? \n a.Walt Whitman b.Leonardo Da Vinci c.Franz Kafka d.William Shakespeare",
    " In what year did World War II end ? \n a.1942 b.1943 c.1945 d.1947",
    " What do paleontologists study ? \n a.Mountains b.Animals c.Lost Civilisations d.Fossils",
    " Ottawa is the capital of which country ? \n a.Bolivia b.India c.Canada d.Australia",
    " Which chess piece can not move in a straight line ? \n a.Rook b.Knight c.King d.Bishop",
    " What is a supernova ? \n a.An underwater volcano b.The eye of a tornado c.The explosion of a star d.None of the above",
    " How are bats able to fly in the dark ? \n a.X-ray vision b.Sixth sense c.Echolocation d.Inter-species communication",
    " Which car company makes the Corolla ? \n a.Nissan b.Toyota c.Subaru d.Honda",
    " What is the technical term for a lie detector ? \n a.Polygraph b.Seismograph c.Teragraph d.Omnigraph",
    " Which country is Amsterdam located in ? \n a.Germany b.Albania c.Netherlands d. Finland",
    " Babe Ruth is a legend of which sport ? \n a.Basketball b.Soccer c.Baseball d.Football",
    " Who is the Fresh Prince of Bel Air ? \n a.Wesley Snipes b.Will Smith c.Chris Rock d.Chris Tucker",
    " What is the smallest country in the world ? \n a.Monaco b.Vatican City c.San Marino d.Liechtenstein",
    " Where is Mount Everest located ? \n a.Tibet b.Nepal c.Switzerland d.On the border between Tibet and Nepal",
    " Who is officially credited with the invention of the light bulb? \n a.Thomas Edison b.Alexander Graham Bell c.Henry Ford d.Samuel Morse",
    " Who is Kylie Minogue? \n a.A Finnish scientist b.A Scottish reality TV star c.A Dutch-German actress d.An Australian-British singer",
    " The Hunchback of Notre Dame is named... \n a.Luffy b.Edwing c.Quasimodo d.Bartholomew",
    " What's the capital of Kenya? \n a.Asmara b.Dakar c.Nairobi d.Johannesburg",
    " Which of the following countries is closest to the South Pole? \n a.South Africa b.Finland c.Libya d.Mexico",
    " What's the correct term for a baby cod? \n a.Kit b.Codling c.Fingerling d.Polliwog",
    " In Greek mythology, who is the Goddess of Agriculture? \n a.Rha b.Persephone c.Hygiela d.Demeter",
    " When is International Women's Day? \n a.March 8 b.Jan 12 c.Aug 23 d.Dec 5",
    " Which country is Dubrovnik located in? \n a.Macedonia b. Crotia c.Bulgaria d.Romania",
    " What was the official name of Thailand before 1939? \n a.Ankara b.Burma c.Ceylon d.Siam",
    " How many bones are there in an elephant's trunk? \n a.0 b.12 c.14 d.16",
    " What's the longest river in the world? \n a.Nile b.Yangtze c.Mississippi d.Amazon",
    " Which philosopher said I think, therefore I am? \n a.Rene Descartes b.Immanuel Kant c.John Locke d.Friedrich Nietzsche",
    " Choose the chemical symbol for potassium \n a.Pt b.Ts c.Ag d.K",
    " What's the Spanish word for fox? \n a.Perro b.Zorro c.Lobo d.Ballena",
    " When is Children's day celebrated? \n a.Nov 16 b.Jan 5 c.Nov 14 d.Oct 14",
    " Which of these things do mycologists study? \n a.Stars b.Doors c.Mushrooms d.Whales",
    " The Frank Worrell Trophy is a test-match (cricket) series played between Australia and \n a.West Indies b.South Africa c.New Zealand d.England",
    " The Green Park Stadium, which hosted the 500th International test cricket match played by India in 2016, is situated in the Indian city of \n a.Kanpur b.Indore c.Gwalior d.Rajkot"]

Answer = ['c', 'c', 'a', 'b', 'd', 'c', 'a', 'b', 'a', 'c', 'b', 'd', 'd', 'c', 'a', 'b', 'a', 'd', 'c', 'd', 'c', 'b', 'c', 'c', 'b', 'a', 'c', 'c', 'b', 'b', 'd', 'a', 'd', 'c', 'c', 'a', 'b', 'd', 'a', 'b', 'd', 'a', 'c', 'a', 'd', 'b', 'c', 'c', 'a', 'a']

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = SERVER_PORT
s.bind(('',port))
s.listen(no_clients) 

Client = [0] * no_clients

for i in range(no_clients): 
    Client[i], addr = s.accept()
    Client[i].send(str(i))
    print ("Connection has been established to client",i)

time.sleep(0.001) 

for i in range(no_clients):
    Client[i].send(str(score_max))
score_keep = [0] * no_clients 
time.sleep

def question_get():
    value = random.randint(0,10000)%len(Question)
    ques_tion = Question[value]
    ans_wer = Answer[value]
    Question.pop(value)
    Answer.pop(value)
    return ques_tion,ans_wer

def game_end():           
    time.sleep(0.01)
    for i in range(no_clients):
        if score_keep[i] == score_max or score_keep[i]== score_max + 0.5:
            Client[i].send("You won the game")
        else:
            Client[i].send("You lost the game")
    exit()

def none_pressed(correctSTR):

    for i in range(no_clients):
        s = Client[i]
        s.send("No one has pressed the buzzer")
    
    for s in Client:
        s.setblocking(1)
    time.sleep(0.1)
    Ans_provided = "None given"

    for i in range(no_clients):
        Client[i].send(Ans_provided)
    time.sleep(0.01)

    Ans_provided = (Ans_provided.lower()).split()

    answeredCorrectly = False

    for s in Client:
        s.send("Incorrect")
    

    score_keepStr = '' 
    time.sleep(0.01)

    for i in score_keep:
        score_keepStr += ' ' + str(i)

    for s in Client:
        s.send(correctSTR)
        time.sleep(0.01)
        s.send(score_keepStr)
        
    time.sleep(0.01)
    
    for s in Client:
        s.send("1")



def game_begin():
    while True: 
        
        time.sleep(0.001)
        buzzed = -1
        
        question,correctSTR = question_get()
        trueAnswer = (correctSTR.lower()).split()

        for s in Client:
            s.send(question)
        for s in Client:
            s.setblocking(0)

        initial_time=int(time.time())
        while True:

            r, w, x = select.select(Client, [], [], 0)
            if r:
                s = r[0]
                buzzed = s.recv(1024)
                break
            elif (int(time.time())-initial_time>=10):
                none_pressed(correctSTR)
                game_begin()
                game_end()

                
            
        
        buzzed = int(buzzed)
        print "Player", buzzed, "has pressed the buzzer."

        for i in range(no_clients):
            s = Client[i]
            if i != buzzed:
                s.send(str(buzzed) + " buzzed.")
            else:
                s.send("You have pressed the buzzer")
        
        for s in Client:
            s.setblocking(1)
        time.sleep(0.1)
        Ans_provided = (Client[buzzed]).recv(1024)
        print "Selected answer is : ", Ans_provided

        for i in range(no_clients):
            if i != buzzed:
                Client[i].send(Ans_provided)
        time.sleep(0.01)

        Ans_provided = (Ans_provided.lower()).split()

        answeredCorrectly = True

        print trueAnswer, Ans_provided

        for i in trueAnswer:
            if not (i in Ans_provided):
                answeredCorrectly = False
                break

        if answeredCorrectly:
            print "Answer is correct"
            for s in Client:
                s.send("Correct")
            score_keep[buzzed]+=1
        else:
            print "Answer is incorrect"
            for s in Client:
                s.send("Incorrect")
            score_keep[buzzed]-=0.5
        

        score_keepStr = '' 
        time.sleep(0.01)

        for i in score_keep:
            score_keepStr += ' ' + str(i)

        for s in Client:
            s.send(correctSTR)
            time.sleep(0.01)
            s.send(score_keepStr)
            
        time.sleep(0.01)
        
        if(score_max in score_keep or (score_max+0.5) in score_keep):
            for s in Client:
                s.send("0")
            break
        else:
            for s in Client:
                s.send("1")

game_begin()
game_end()
