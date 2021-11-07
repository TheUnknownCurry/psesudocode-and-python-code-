import random
attempts_list=[]
def start_game():
    random_number=int(random.randint(1,50))    
    print("Hello, Gamer ") 
    print("Welcome To The Number Guessing Game ")
    print("Let's Play An Interesting Game Were You Have To Guess A Number  ")
    print("A Number Which I Am Thinking Right Now ")
    print("Can You Guess The Number Right? ")
    player_name=input("But First May I Know Your Name- ") 
    play=input("Hi, {} and would you like to play this game? Enter(yes/no) ".format(player_name))  
    print("Let's start the game and have fun")
    print("Note: 1. You only have 5 attempts to guess the correct answer")
    print("      2. The total score of the game is 60")
    print("         10 points will decreased for your extra chance taken")
    attempts=0 
    score=60
    while play.lower()=="yes":
        if attempts<5:
            try:
                guess=input("Now Pick Any Number Between 1 to 50: ")
                if int(guess)< 1 or int(guess) > 50:
                    print("Guess Within The Range ")
                    print("Your number was not in the range of 1 to 50 ")
                if int(guess)==random_number:
                    print("Wow, Congrats!! You Got The Answer Right")
                    print("You are a real gamer")
                    attempts+=1
                    score-=10
                    attempts_list.append(attempts)
                    print("It Took {} Attempts To Get The Correct Answer".format(attempts))
                    print("Your total score is {}".format(score))
                    print("Let's again start the game and have fun")
                    play=input("Would You Like To Play Again Enter (yes/no): ")
                    attempts=0
                    score=60
                    random_number=int(random.randint(1,50))
                    if play.lower() == "no":
                        print("😞")
                        print("Ok no problem, I guess you will miss out on the fun...")
                        break
                elif int(guess) > random_number:
                    print("Oh no!! The Number Which I Guessed Is Too Low")  
                    print("Don't worry, give it one more try")
                    print("Hint- The number which i am thinking is in the range of {},{} :".format(random_number-5, random_number+5))  
                    attempts+=1
                    score-=10
                elif int(guess) < random_number:
                    print("The Number Which I Guessed Is Too High")
                    print("Don't worry, give it one more try")
                    print("Hint- The number is in the range of {},{} :".format(random_number-5, random_number+5))
                    attempts+=1 
                    score-=10
            except ValueError as err:
                print("Not A Valid Number, Try Again")
                print("Your number should be between 1 to 50 ")
                print("({})".format(err))
        else:
            print("Oh no!! Your attempts are over")
            play_again=input("Would You Like To Play Again Enter (yes/no): ")
            attempts=0
            random_number=int(random.randint(1,50))
            if play_again.lower() == "no":
                        print("😞")
                        print("Ok no problem, I guess you will miss out on the fun...")
                        break         
    else: 
        print("😞")
        print("Ok no problem, I guess you will miss out on the fun...")  
          
if __name__ == '__main__':
    start_game()      
