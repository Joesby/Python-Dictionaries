#Task 1: Customer Service Ticket Tracker
#create a dictionary to store nested dictionaries for each ticket and their information
service_tickets = {
    "Ticket_1": {"Customer": "Alice", "Issue": "Login problem", "Status": "Open"},
    "Ticket_2": {"Customer": "Bob", "Issue": "Payment issue", "Status": "Closed"}
}

#function that opens a new service ticket
def New_Ticket(name, issue):
    #make a variable that is one more than the total tickets and change to a string
    ticket_number = str(len(service_tickets) + 1)
    #update the service_tickets dictionary with the ticket number created 
    #using the name and issue provided, and a default open status for nested dictionaries
    service_tickets.update({"Ticket_" + ticket_number: {"Customer": name.capitalize(), "Issue": issue.capitalize(), "Status": "Open"}})

#function updates the status of an existing ticket
def Update_Ticket(name, status):
    #reach into the service_tickets dictionary and iterate through nested dictionaries to find the correct Customer value
    for i in service_tickets:
        ticket_info = service_tickets.get(i)
        if ticket_info.get("Customer") == name:
            #when the correct name is found, change the status to the argument the user provided
            ticket_info = service_tickets.get(i)
            ticket_info.update({"Status": status})

#function for displaying all tickets or displaying by a sepecific status
def Display_Tickets(status):
    #reach into the initial service_tickets dictionary
    for i in service_tickets:
        ticket_info = service_tickets.get(i)
        #if the status is the same as the user provided argument, display the ticket using the iterable variable
        if ticket_info.get("Status") == status:
            print(i + ": " + str(ticket_info))
        #if the status input is 'All', print the iteratable variable
        #without a designated status, this same print statement will display all tickets
        elif status == "All":
            print(i + ": " + str(ticket_info))

#Welcome the user to the Customer Service Ticket Tracker
print("Welcome to the Customer Service Ticket Tracker!")
print("Here are a list of options:")
print("1. Create a new service ticket.")
print("2. Update the status of a pre-existing ticket.")
print("3. Display tickets by status.")
print("4. Exit.")
print()

#use a try block to take user input specifically for int input
try:
    user_choice = int(input("Please choose one of the numbered options: "))
#add a response for if user inputs anything other than an integer, set user_choice to zero to enter the while loop
except ValueError:
    print("Please choose the number of the selection you want to make.")
    user_choice = 0

#put user in a while loop, exiting if the value is equal to 4
while user_choice != 4:
    #when input is 1, prompt the user for arguments to use New_Ticket function
    if user_choice == 1:
        ticket_name = input("Please provide a name for the new ticket: ")
        ticket_issue = input("What is the issue for this ticket? ")
        New_Ticket(ticket_name, ticket_issue)

    #when input is 2, format user input, then search through the service_tickets dictionary for the right ticket
    elif user_choice == 2:
        ticket_name = input("Please provide the name on the ticket you would like to change the status of: ")
        ticket_name = ticket_name.capitalize()
        for i in service_tickets:
            ticket_info = service_tickets.get(i)
            #when the ticket with the right name is found, prompt the user with a new ticket status and format it correctly
            if ticket_name in ticket_info.get("Customer"):
                new_status = input("Would you like to open or close " + ticket_name + "'s ticket? ")
                new_status = new_status.capitalize()
                #depending on which option the user chooses, use the Update_Ticket function to open or close tickets and provide feedback
                if new_status == "Open":
                    Update_Ticket(ticket_name, "Open")
                    print(ticket_name + "'s ticket has been opened.")
                elif new_status == "Close":
                    Update_Ticket(ticket_name, "Closed")
                    print(ticket_name + "'s ticket has been closed.")
                #if they input anything other than open or close, as directed, provide feedback
                else:
                    print("I'm sorry, that isn't a valid ticket status.")
                    break

    #when input is 3, prompt the user a status to display select tickets, then format correctly
    elif user_choice == 3:
        ticket_status = input("Would you like to display open, closed, or all service tickets? ")
        ticket_status = ticket_status.capitalize()
        #if the input status is open or closed, use the Display_Tickets with the user provided status
        if "Open" in ticket_status or "Closed" in ticket_status:
            Display_Tickets(ticket_status)
        #if the user provides any other input, change the ticket status to all and display all tickets
        else:
            ticket_status = "All"
            Display_Tickets(ticket_status)

    #use zero to designate a way to iterate through the loop again without errors or output
    elif user_choice == 0:
        pass

    #if the user provides any integers outside of the available selections
    #prompt the user to make a valid selection and change the input to zero to iterate back through the loop
    else:
        print("Please make a valid selection.")
        user_choice = 0

    #use a blank space for readability
    #then give the user another prompt to continue using the Ticket Tracker
    #using a try and except block to avoid potential errors
    print()
    try:
        user_choice = int(input("Please choose one of the numbered options: "))
    except ValueError:
        print("Please choose the number of the selection you want to make.")
        user_choice = 0

#thank the user for using the ticket tracker once they have quit
print("Thank you for using our Ticket Tracker! Good-bye!")