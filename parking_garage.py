class ParkingGarage():
    """
    The parking garage class includes tickets, parking spaces, and a current ticket.

    Attributes:
    -tickets: expects a list
    -parking_spaces: expects a list
    -current_ticket: expects a dictionary with a 'paid' key set to False
    """
    
    
    
    def __init__(self, tickets, parking_spaces, current_ticket):
        self.tickets = tickets
        self.parking_spaces = parking_spaces
        self.current_ticket = current_ticket

    # take_ticket() gives the user a ticket if there is one available, and a parking space available.

    def take_ticket(self):
        if len(self.tickets) > 0:
            del self.tickets[-1]
            print("Here is your ticket!")
        else:
            print("There are no spots available.")
        
        if len(self.parking_spaces) > 0:
            del self.parking_spaces[-1]

    # pay_for_parking() prompts the user to input the amount to be paid
        
    def pay_for_parking(self):
        paid_amount = int(input("Please input the amount you wish to pay. Spaces are $1 per hour. "))
        if paid_amount > 0:
            print("Your payment has been accepted, you have 15 minutes to exit the garage.")
            self.current_ticket['paid'] = True

    # leave_garage() allows the user to leave if they have paid for their ticket
    # and refills the garage's spaces and tickets

    def leave_garage(self):
        if self.current_ticket['paid'] == True:
            print('Thank you, have a nice day!')
        else:
            paid_amount =int(input("Please input the amount you wish to pay. Spaces are $1 per hour. "))
        self.tickets.append('ticket')
        self.parking_spaces.append('space')


new_parking_garage = ParkingGarage(['ticket', 'ticket', 'ticket', 'ticket', 'ticket'], 
                                                                    ['space', 'space', 'space', 'space', 'space'],
                                                                    {'paid' : False})

new_parking_garage.take_ticket()
new_parking_garage.pay_for_parking()
new_parking_garage.leave_garage()
