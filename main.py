def main():
    #Welcomes the user to my quiz
    print("Welcome to my general knowledge quiz")
    name = input("""What is your name?
""")
    print("""Hello %s, in this game you will be made to answer questions testing your general knowledge.
You can answer these questions by typing in the correct answer (make sure that all spelling is correct, capital
letters are not needed""" % name)
    count = 0
    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    correct = 0
    progress = 1
    import random
    replay = True
    while x == True:
        repeat = True
        while repeat == True:
            ran_q = random.randrange(1, 20)
            count += 1
            if count == 1:
                a = ran_q
            if count == 2:
                b = ran_q
            if count == 3:
                c = ran_q
            if count == 4:
                d = ran_q
            if count == 5:
                e = ran_q
            if count == 6:
                f = ran_q
            if count == 7:
                g = ran_q
            if count == 8:
                h = ran_q
            if count == 9:
                i = ran_q
            if count == 10:
                j = ran_q
            if count == 11:
                k = ran_q
            if count == 12:
                l = ran_q
            if count == 13:
                m = ran_q
            if count == 14:
                n = ran_q
            if count == 15:
                o = ran_q
            if (ran_q != a and ran_q != b and ran_q != c and ran_q != d and ran_q != e and ran_q != f 
                   and ran_q != g and ran_q != h and ran_q != i and ran_q != j and ran_q != k and ran_q != l 
                   and ran_q != m and ran_q != n and ran_q != o):
                question_num = ran_q
                repeat = False
        print(question_num)
        if question_num == 1:
            answer = "beards"
            guess = input("""If you had pogonophobia what would you be afraid of?
""")
            guess = guess.lower()
            progress += 1
            if guess ==  answer:
                correct += 1
                print("Well done %s, you are correct" % name)
            else:
                print("Wrong answer, %s" % name)
                print("The correct answer was '%s'" % answer)
        elif question_num == 2:
            answer = "five"
            answer_alternative = "5"
            guess = input("""How many rings on the Olympic flag?
""")
            guess = guess.lower()
            progress += 1
            if guess ==  answer or answer_alternative:
                correct += 1
                print("Well done %s, you are correct" % name)
            else:
                print("Wrong answer, %s" % name)
                print("The correct answer was '%s'" % answer)
        elif question_num == 3:
            answer = "eat porridge"
            guess = input("""What would a Scotsman do with a spurtle?
""")
            guess = guess.lower()
            progress += 1
            if guess ==  answer or answer_alternative:
                correct += 1
                print("Well done %s, you are correct" % name)
            else:
                print("Wrong answer, %s" % name)
                print("The correct answer was '%s'" % answer)
        elif question_num == 4:
            answer = "6"
            answer_alternative = "six"
            guess = input("""How many feet in a fathom?
""")
            guess = guess.lower()
            progress += 1
            if guess ==  answer or answer_alternative:
                correct += 1
                print("Well done %s, you are correct" % name)
            else:
                print("Wrong answer, %s" % name)
                print("The correct answer was '%s'" % answer)
        elif question_num == 5:
                answer = "pinocchio"
                answer_alternative = "pinocchio's"
                guess = input("""Whose nose grew when he told a lie?
""")
                guess = guess.lower()
                progress += 1
                if guess ==  answer or answer_alternative:
                    correct += 1
                    print("Well done %s, you are correct" % name)
                else:
                    print("Wrong answer, %s" % name)
                    print("The correct answer was '%s'" % answer)
        elif question_num == 6:
                answer = "hippo"
                answer_alternative = "hippopotamus"
                guess = input("""What animals name translates as water horse?
""")
                guess = guess.lower()
                progress += 1
                if guess ==  answer or answer_alternative:
                    correct += 1
                    print("Well done %s, you are correct" % name)
                else:
                    print("Wrong answer, %s" % name)
                    print("The correct answer was '%s'" % answer)
        elif question_num == 7:
                answer = "arthur ransom"
                answer_alternative = "arthurransom"
                guess = input("""Who wrote the children's novel Swallows and Amazons?
""")
                guess = guess.lower()
                progress += 1
                if guess ==  answer or answer_alternative:
                    correct += 1
                    print("Well done %s, you are correct" % name)
                else:
                    print("Wrong answer, %s" % name)
                    print("The correct answer was '%s'" % answer)
        elif question_num == 8:
                answer = "eiffel tower"
                answer_alternative = "the eiffel tower"
                guess = input("""What is 6 inches bigger in Summer?
""")
                guess = guess.lower()
                progress += 1
                if guess ==  answer or guess == answer_alternative:
                    correct += 1
                    print("Well done %s, you are correct" % name)
                else:
                    print("Wrong answer, %s" % name)
                    print("The correct answer was '%s'" % answer)
        elif question_num == 9:
                answer = "eiffel tower"
                answer_alternative = "the eiffel tower"
                guess = input("""What is 6 inches bigger in Summer?
""")
                guess = guess.lower()
                progress += 1
                if guess ==  answer or guess == answer_alternative:
                    correct += 1
                    print("Well done %s, you are correct" % name)
                else:
                    print("Wrong answer, %s" % name)
                    print("The correct answer was '%s'" % answer)
        elif question_num == 10:
                answer = "the rain"
                answer_alternative = "rain"
                guess = input("""What do ombrophobes fear?
""")
                guess = guess.lower()
                progress += 1
                if guess ==  answer or guess == answer_alternative:
                    correct += 1
                    print("Well done %s, you are correct" % name)
                else:
                    print("Wrong answer, %s" % name)
                    print("The correct answer was '%s'" % answer)
        elif question_num == 11:
                answer = "freckles"
                guess = input("""What are lentigines?
""")
                guess = guess.lower()
                progress += 1
                if guess ==  answer:
                    correct += 1
                    print("Well done %s, you are correct" % name)
                else:
                    print("Wrong answer, %s" % name)
                    print("The correct answer was '%s'" % answer)
        elif question_num == 12:
                answer = "nightsticks"
                answer_alternative = "night sticks"
                guess = input("""British policemen have truncheons what is USA equivalent?
""")
                guess = guess.lower()
                progress += 1
                if guess ==  answer or guess == answer_alternative or guess == "night stick" or guess == "nightstick":
                    correct += 1
                    print("Well done %s, you are correct" % name)
                else:
                    print("Wrong answer, %s" % name)
                    print("The correct answer was '%s'" % answer)
        elif question_num == 13:
                answer = "zone improvement plan"
                guess = input("""What does Zip stand for in Zip Code?
""")
                guess = guess.lower()
                progress += 1
                if guess ==  answer:
                    correct += 1
                    print("Well done %s, you are correct" % name)
                else:
                    print("Wrong answer, %s" % name)
                    print("The correct answer was '%s'" % answer)
        elif question_num == 14:
                answer = "birch"
                answer_alternative = "birch tree"
                guess = input("""What wood is plywood mostly made from?
""")
                guess = guess.lower()
                progress += 1
                if guess ==  answer or guess == answer_alternative:
                    correct += 1
                    print("Well done %s, you are correct" % name)
                else:
                    print("Wrong answer, %s" % name)
                    print("The correct answer was '%s'" % answer)
        elif question_num == 15:
                answer = ""
                answer_alternative = ""
                guess = input("""?
""")
                guess = guess.lower()
                progress += 1
                if guess ==  answer or guess == answer_alternative:
                    correct += 1
                    print("Well done %s, you are correct" % name)
                else:
                    print("Wrong answer, %s" % name)
                    print("The correct answer was '%s'" % answer)
        elif question_num == 16:
                answer = ""
                answer_alternative = ""
                guess = input("""?
""")
                guess = guess.lower()
                progress += 1
                if guess ==  answer or guess == answer_alternative:
                    correct += 1
                    print("Well done %s, you are correct" % name)
                else:
                    print("Wrong answer, %s" % name)
                    print("The correct answer was '%s'" % answer)
        elif question_num == 17:
                answer = ""
                answer_alternative = ""
                guess = input("""?
""")
                guess = guess.lower()
                progress += 1
                if guess ==  answer or guess == answer_alternative:
                    correct += 1
                    print("Well done %s, you are correct" % name)
                else:
                    print("Wrong answer, %s" % name)
                    print("The correct answer was '%s'" % answer)
        elif question_num == 18:
                answer = ""
                answer_alternative = ""
                guess = input("""?
""")
                guess = guess.lower()
                progress += 1
                if guess ==  answer or guess == answer_alternative:
                    correct += 1
                    print("Well done %s, you are correct" % name)
                else:
                    print("Wrong answer, %s" % name)
                    print("The correct answer was '%s'" % answer)
        elif question_num == 19:
                answer = ""
                answer_alternative = ""
                guess = input("""?
""")
                guess = guess.lower()
                progress += 1
                if guess ==  answer or guess == answer_alternative:
                    correct += 1
                    print("Well done %s, you are correct" % name)
                else:
                    print("Wrong answer, %s" % name)
                    print("The correct answer was '%s'" % answer)
        elif question_num == 20:
                answer = ""
                answer_alternative = ""
                guess = input("""?
""")
                guess = guess.lower()
                progress += 1
                if guess ==  answer or guess == answer_alternative:
                    correct += 1
                    print("Well done %s, you are correct" % name)
                else:
                    print("Wrong answer, %s" % name)
                    print("The correct answer was '%s'" % answer)
main()       
        
