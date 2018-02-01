from random import choice
# add a function
def ask_answer():
    return input("What is your question?")
a1=ask_answer()#python file for HW4
ans_list=['It is certain','It is decidedly so','Without a doubt','Yes definitely','You may rely on it','As I see it, yes','Most likely','Outlook good','Yes', 'Signs point to yes', 'Reply hazy try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',"Don't count on it", 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']

print(choice(ans_list))

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
