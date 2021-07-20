# get all imports from the asset and data  folder
import re
from assets import art
from data import data

# extract printer information and resources from the modules imported
printer_logo = art.logo
printer_formats = data.FORMAT
printer_resources = data.resources

# printer's display message
print(printer_logo) 



class Printer:
    # initialise printer resources
    def __init__(self):
        # initialised the printer resources and printer formats
        self.printer_formats = printer_formats
        self.printer_resources = printer_resources
  
    # welcome page
    def start(self):

      
        # prompt_user by asking what type of operation they would like to do?
        printer_operation = input("""
        Welcome what would you like to do today?
        Enter 1 to Print
        Enter 2 to Get printer's report
        Enter 3 to Switch off the printer
        """)
        # validate printer_opertion
        while printer_operation != "1"  and printer_operation != "2" and  printer_operation != "3":
            printer_operation = input("""
            Wrong input selected,please enter 1, 2 or 3
            Enter 1 to Print
            Enter 2 to Get printer's report
            Enter 3 to Switch off the printer
            """)
            printer_operation = printer_operation

        # process the user input
        if printer_operation == "1":
            # put print abstraction here
            print_format, print_quantity = self.print()
            # use output to process user's project
            self.Print_user_project(print_format, print_quantity)
            # make another decision
            self.printer_decision()
        elif printer_operation == "2":
            # get printers report
            self.print_report()
            # make another decision
            self.printer_decision()
        else:
            # switch off printer
            return self.off()
  
    # decision feature
    def printer_decision(self):

        # prompt_user by asking what type of operation they would like to do?
        printer_decision = input("""
        Would you like to perform another operation?
        Enter 1 to Perform  another operation
        Enter 2 to Switch off the printer
        """)

        # validate printer_opertion
        while printer_decision != "1"  and printer_decision != "2":
            printer_decision = input("""
        Wrong input selected,please enter 1 or 2
        Enter 1 to Perform  another operation
        Enter 2 to Switch off the printer
        """)
        printer_decision = printer_decision


        if printer_decision == "1":
            # restart the printer
            self.start()
        else:
            # switch off
            self.off()

    # print feature
    def print(self):
        # prompt_user by asking what they like to print
        print_operation = input("""
        What format would you like to print? colored or greyscale
        Enter 1 for coloured
        Enter 2 for greyscale
        """)
        # validate the input
        while print_operation != "1"  and print_operation != "2":
            print_operation = input("""
            Wrong input selected,please enter 1 or 2
            Enter 1 for coloured
            Enter 2 for greyscale
            """)
            print_operation = print_operation

        # process the user input
        if print_operation == "1":
            print_format = "coloured"
        else:
            print_format = "greyscale"
        

        # take the quantity  required
        print_quantity = input("""How many quantity would you like to print?: """)

        # validate currency quantity
        print_quantity_regex = '[0-9]'
        print_quantity_validation = re.match(print_quantity_regex, print_quantity)
        while print_quantity_validation == None:
            print_quantity= input("Wrong input, enter only numbers (0-9) ")
            print_quantity_regex = '[0-9]'
            print_quantity_validation = re.match(print_quantity_regex, print_quantity)
            print_quantity_validation = print_quantity_validation

        print_quantity = int(print_quantity)

        return print_format, print_quantity
    
    # off feature
    def off(self):
        # prompt the user to enter the secret_word
        secret_word = input("Please enter the secret word: ").lower()
        # validate the secret_word
        while secret_word != "off":
            secret_word = input("Incorrect word entered: DO YOU MEAN TO ENTER OFF: ")
            secret_word = secret_word
 
        print ("Ending execution and turning off printer...")

    # print_report feature
    def print_report(self):
         # prompt the user to enter the report word
        action = input("Please enter the key word: ").lower()
        # validate the report_word
        while action != "report":
            action = input("Incorrect word entered: DO YOU MEAN TO ENTER 'report': ")
            action = action
        # displays the printer's resources
        print(f"""
        Current printer resources:         
        ink:    {self.printer_resources["ink"]}ml
        paper:  {self.printer_resources["paper"]}pc
        profit: #{self.printer_resources["profit"]}
        """)
    
    # check resource feature
    def check_resources(self,print_format, number_of_pages):
        # get all the available resources now
        ink_available = self.printer_resources["ink"]
        paper_available = self.printer_resources["paper"]
       
        # # calculate the resources needed based on the print_format selected
        if print_format == "coloured":
            # get the ink required for one coloured paper print
            ink_required_per_one = self.printer_formats[print_format]["materials"]["ink"]
            # get the total volume required to print the number_of_pages
            total_ink_volume_required = ink_required_per_one * number_of_pages
            # make decision based on the total ink volume required and number of pages
            # make ink decisions first
            if total_ink_volume_required > ink_available:
                return "Sorry there is  not enough ink"
            elif number_of_pages > paper_available:
                return "Sorry there is  not enough paper"
            else:
                return  total_ink_volume_required, number_of_pages, print_format
        else:
            # get the ink required for one coloured paper print
            ink_required_per_one = self.printer_formats[print_format]["materials"]["ink"]
            # get the total volume required to print the number_of_pages
            total_ink_volume_required = ink_required_per_one * number_of_pages
            # make decision based on the total ink volume required and number of pages
            # make ink decisions first
            if total_ink_volume_required > ink_available:
                return "Sorry there is  not enough ink"
            elif number_of_pages > paper_available:
                return "Sorry there is  not enough paper"
            else:
                return total_ink_volume_required, number_of_pages, print_format

    # local_currency coverter
    def local_currency_converter(self,total_print_price):
        # tell the user the price and prompt the user the currency to put
        currency_input = input(f"""
        --------------------------------------------------
        Your price is: #{total_print_price}
        Please insert the order of the accepted currency:
        Enter 1 for Wazobia
        Enter 2 for Muri
        Enter 3 for Fiba
        Enter 4 for Biyar
        --------------------------------------------------
        """)
        # validate currency chosen 
        while currency_input != "5" and currency_input != "4" and currency_input != "3" and currency_input != "2" and currency_input != "1":
            currency_input = input(f"""
            --------------------------------------------------
            Wrong input
            Your price is: #{total_print_price}
            Please insert the order of the accepted currency:
            Enter 1 for Wazobia
            Enter 2 for Muri
            Enter 3 for Fiba
            Enter 4 for Biyar
            --------------------------------------------------
            """)

        # get the equivalent currency note
        if currency_input == "1":
            currency_note = 50
        elif currency_input == "2":
            currency_note = 20
        elif currency_input == "3":
            currency_note = 10
        else:
            currency_note = 5

        currency_quantity = input(f"""
        --------------------------------------------------
        Your price is: #{total_print_price}
        Your currency note is: #{currency_note}
        Please enter currency quantity:
        --------------------------------------------------
        """)

        # validate currency quantity
        currency_quantity_regex = '[0-9]'
        currency_quantity_validation = re.match(currency_quantity_regex, currency_quantity)
        while currency_quantity_validation == None:
            currency_quantity= input(f"""
            --------------------------------------------------
            Wrong input, quantity can only be numbers (0-9)
            Your price is: #{total_print_price}
            Your currency note is: #{currency_note}
            Please enter currency quantity:
            --------------------------------------------------
            """)
            currency_quantity_regex = '[0-9]'
            currency_quantity_validation = re.match(currency_quantity_regex, currency_quantity)
            currency_quantity_validation = currency_quantity_validation


        

        amount_paid = currency_note * int(currency_quantity) 

        return amount_paid

    # process price
    def process_price(self,print_format, number_of_pages ): 
        # get total_ink_volume and page_quantity from the check_resources method
        _ , page_quantity, print_format = self.check_resources(print_format, number_of_pages)
        # get the amount per print as per the print formant
        amount_per_print = self.printer_formats[print_format]['price']
        # calculate total price
        total_print_price = amount_per_print * page_quantity
        # destructure the local_currency_converter
        amount = self.local_currency_converter(total_print_price)
        return amount, total_print_price

    # update feature
    def update_profit(self, amount_paid):
        updated_price = self.printer_resources["profit"] + amount_paid
        self.printer_resources["profit"] = updated_price

    # check transaction
    def check_transaction(self,print_format, number_of_pages):
        amount_paid, cost_price = self.process_price(print_format, number_of_pages)
        
        # amount less than cost
        if amount_paid < cost_price:
            print("Sorry that's not enough money, Money refunded")
            return "Unsuccesful"
        # amount = cost , update the price in resource
        elif amount_paid == cost_price:
            self.update_profit(amount_paid)
            return "Succesful"
        # amount > cost, give change first then update the price in resources
        elif amount_paid  >  cost_price:
            # get change
            change = amount_paid - cost_price
            # print change to the screen
            print(" ")
            print(f"Here is #{change} in change")
            # update the profit
            self.update_profit(amount_paid)
            return "Succesful"
    
    # check printer_user_project
    def Print_user_project(self,print_format, number_of_pages):
        transaction_status = self.check_transaction(print_format, number_of_pages)
        total_ink_needed, total_paper_needed, _ = self.check_resources(print_format, number_of_pages)
        # make decision based on transaction_status, update the resource parameters
        if transaction_status == "Succesful":
            # update resource material
            self.printer_resources["ink"] -= total_ink_needed
            self.printer_resources["paper"] -= total_paper_needed

            # print the user resources
            print ("""
            ---------------------------------
            Here is your project
            Thank you for using our services
            ---------------------------------
            """)



# instantiate a new user of the printer class       
new_user = Printer()
# starts the printer
new_user.start()





