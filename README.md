Multiplayer Quiz game using Socket Programming in Python.

a. How to get started :

   1. Download the files 'server.py' and 'client.py' in your system.
   2. Now run the following commands in the terminal 'python server.py' in one terminal and 'python client.py' in other three terminals.
   3. Here we have 4 terminals opened in total, one for the server and rest three for the clients(user).

b. Overview :

   1. There are three players (clients) in the game.
   2. The host (server) has a list of 50 questions and correct answers with him.
   3. A question is randomly chosen among the given set of questions and then server sends to all the three players.
   4. The players press the buzzer by pressing 'Enter'  key on the keyboard. The first one to press the buzzer is given chance to answer the question.
   5. If the answer is correct then he is awarded a point ( +1.0 ), else a negative point awarded ( -0.5 ).
   6. It the player who pressed the buzzer fails to answer the question then no more chance is given to any other player.
   7. The host then proceeds with the next question.
   8. The game stops when a player gets 5 points or more and then he is declared the winner.

c. Description : 
    
   1. I have divided the project into two parts, the client phase and the server part. 
   2. First the server waits for a connection from the three clients and then proceeds with the questions if and only if all the three participants have joined.
   3. Each of them have been assigned as Player0, Player1 and Player2 with respect to the time of their participation. Then the server broadcasts the questions from the stored set of questions in the list randomly.
   4. It then waits for buzzer to be pressed from any one of the user and then waits for the user to give some input. If the user gives a correct answer his score is incremented accordingly and reduced if it is a wrong answer.
   5. Current score is displayed at the end of each question.
   6. It keeps on doing the process until a player scores 5 points or more. And the function game_end() is intiated.
   7. The teminal in which the host is running displays who pressed the buzzer and the answer given by them, if the answer given is correct then it dislays both options as the correct answer, and if the given answer is incorrect then it dislpays the correct answer and incorrect answer both.
