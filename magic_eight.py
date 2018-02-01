# add a function
def ask_answer():
    return input("What is your question?")
a1=ask_answer()#python file for HW4

# check if user input is a question
while a1 != "":
    if "?" in a1:
        print (choice(ans_list))
        a1=ask_answer()
    else:
        print ("I’m sorry, I can only answer questions.")
        st = input("If you want to stop, please input 'quit'; else, input your question:")
        if st !="quit":
            a1=ask_answer()
        else:
            break
