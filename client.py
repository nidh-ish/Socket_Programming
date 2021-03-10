SERVER_IP = ''  

SERVER_PORT = 1644

import select
import threading
import sys
import random
import time
import socket
import termios

try: 
    def Message_recv(s,killRequest):
        while not killRequest.isSet(): 
            r, w, x = select.select([s], [], []) 
            data = r[0].recv(1024)
            print data
            if data:
                killRequest.set()

    def Message_send(s, userid, killRequest, youBuzzed):
        while not killRequest.isSet(): 
            r, w, x = select.select([sys.stdin], [], [], 0.02)

            if r:
                s.send(str(userid))
                youBuzzed.set()
                time.sleep(0.01)
                break

    serverip = SERVER_IP
    serverport = SERVER_PORT
    clientport = random.randint(2000, 3000)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', clientport))
    s.connect((serverip, serverport))
    userid = s.recv(1024)
    print "Hello. Your player number is : ", userid
    win_score = s.recv(1024)
    print  "Press buzzer first to answer first. Score required to win is : ", win_score

    
    continue_next_round = 1 
    while continue_next_round:
        
        question = s.recv(1024)
        killRequest = threading.Event()
        youBuzzed = threading.Event()

        sendThread = threading.Thread(target = Message_send, args = [s, userid, killRequest, youBuzzed]) 
        receiveThread = threading.Thread(target = Message_recv, args = [s, killRequest])

        time.sleep(0.1)
        print "Question:", question
        print "Buzzer Round"
        
        s.setblocking(0)
        sendThread.start()
        receiveThread.start()
        receiveThread.join()
        sendThread.join()

        s.setblocking(1)
        termios.tcflush(sys.stdin, termios.TCIOFLUSH) 
        time.sleep(0.01)
        if youBuzzed.isSet():
            print "Answer the question : "
            givenAnswer = raw_input()
            s.send(givenAnswer)
        else:
            givenAnswer = s.recv(1024)
            print "Answer selected is :", givenAnswer
            
        is_correct_str = s.recv(1024)
        time.sleep(0.001)
        print is_correct_str
        trueAnswer = s.recv(1024)
        print "Correct answer is:",trueAnswer

        tally = s.recv(1024) 
        tally = tally.split()

        print "Score of player"
        for i in range(len(tally)):
            print i, tally[i]
        continue_next_round = s.recv(1024)
        continue_next_round = int(continue_next_round)

    final_message = s.recv(1024) 
    print final_message
except Exception as e:
    print e 
finally: 
    s.close()
