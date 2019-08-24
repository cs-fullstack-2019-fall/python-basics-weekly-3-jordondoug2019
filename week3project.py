#Week 3 Project

x=-1 #Variable created for the purpose of the while loop. Used so the while loop will continue to be in a false
        #conditon.
acct=20 #Variable is established outside of loops/conditions so it can be read globally throughout each piece of code
        #I believe its called scope.
nameInput=input("Enter Your name:   ")# Challenege: create a variable to hold input for name
pin=input("Enter 4 digit pin:  ") #Challenge: create a variable that will accept four digit pin
print(f"Hello {nameInput} Welcome to Codecrew Banking!") #Confirming User input of name with a small message
# pin2=pin
# if(pin==pin2):
#     pin=input("ENter pin again")
while(x!=4):#Create a while loop that includes menu options in f string template
    print( #f string template used to display each option the way i type it. \n is used to create multi lines.
        f"Hello, Please choose one of the following:\n"
        f"1.Check Balance\n"
        f"2. Add Money to Account\n"
        f"3. Withdraw money from account\n"
        f"4. Quit"
         )
    userInput=int(input("What would you like to do?  ")) #Input variable for menu
    if(userInput==1): #Condition for option 1
        print(f"\nYour current balance is: ${acct}\n") #Use to display current balance
    if(userInput==2): #Condition for option 2
        acctDeposit= int(input("How much would you like to deposit?  ")) #Variable created to hold user input for amount to deposit
        acct=acct+acctDeposit #Acct variable redeclared to output new balance. (20+ whatever the user would like to deposit)
        print(f"\nYour new balance is: ${acct}\n") #display updated balance
    elif(userInput==3): #Condition for option 3
        acctWithdraw= int(input("How much would you like to withdraw?  ")) #variable created to hold user input for amount to withdraw
        newacct=acct-acctWithdraw #acct variable redeclared to output new balance. !! : you should redefine acct NOT create a new varibale so that the running total is updated 
        if(acctWithdraw>acct): # if input is greater than acct variable,
            print(f"\nInsufficient funds\n") # displays message if condition is true
        elif(acctWithdraw<acct): #if 1st condition is not true, this condition checks if input is less than acct variable
            print(f" \nYour new balance is:${newacct}\n")# if the condition is true, displays message with new account balance
    elif(userInput==4):
        print(f"\nThank You for banking with CodeCrew\n")# condition for option 4
        break;

