import re
from assets import art
from data import data


printer_logo = art.logo
printer_formats = data.FORMAT
printer_resources = data.resources


print(printer_logo) 



class Printer:

   
    def __init__(self):
        self.printer_formats = printer_formats
        self.printer_resources = printer_resources
  
   
    def start(self):

      
        
        printer_operation = input("""
        Welcome what would you like to do today?
        Enter 1 to Print
        Enter 2 to Get printer's report
        Enter 3 to Switch off the printer
        """)
       
        while printer_operation != "1"  and printer_operation != "2" and  printer_operation != "3":
            printer_operation = input("""
            Wrong input selected,please enter 1, 2 or 3
            Enter 1 to Print
            Enter 2 to Get printer's report
            Enter 3 to Switch off the printer
            """)
            printer_operation = printer_operation

        
        if printer_operation == "1":
           
            print_format, print_quantity = self.print()
           
            self.Print_user_project(print_format, print_quantity)
            
            self.printer_decision()
        elif printer_operation == "2":
            
            self.print_report()
            
            self.printer_decision()
        else:
            
            return self.off()
  
    
    def printer_decision(self):

        
        printer_decision = input("""
        Would you like to perform another operation?
        Enter 1 to Perform  another operation
        Enter 2 to Switch off the printer
        """)

        
        while printer_decision != "1"  and printer_decision != "2":
            printer_decision = input("""
        Wrong input selected,please enter 1 or 2
        Enter 1 to Perform  another operation
        Enter 2 to Switch off the printer
        """)
        printer_decision = printer_decision


        if printer_decision == "1":
            
            self.start()
        else:
           
            self.off()

    
    def print(self):
        
        print_operation = input("""
        What format would you like to print? colored or greyscale
        Enter 1 for coloured
        Enter 2 for greyscale
        """)
        
        while print_operation != "1"  and print_operation != "2":
            print_operation = input("""
            Wrong input selected,please enter 1 or 2
            Enter 1 for coloured
            Enter 2 for greyscale
            """)
            print_operation = print_operation

       
        if print_operation == "1":
            print_format = "coloured"
        else:
            print_format = "greyscale"
        

        
        print_quantity = input("""How many quantity would you like to print?: """)

        
        print_quantity_regex = '[0-9]$'
        print_quantity_validation = re.match(print_quantity_regex, print_quantity)
        while print_quantity_validation == None:
            print_quantity= input("Wrong input, enter only numbers (0-9) ")
            print_quantity_regex = '[0-9]$'
            print_quantity_validation = re.match(print_quantity_regex, print_quantity)
            print_quantity_validation = print_quantity_validation

        print_quantity = int(print_quantity)

        return print_format, print_quantity
    
    
    def off(self):
        secret_word = input("Please enter the secret word: ").lower()
        while secret_word != "off":
            secret_word = input("Incorrect word entered: DO YOU MEAN TO ENTER OFF: ")
            secret_word = secret_word
        print ("Ending execution and turning off printer...")

    
    def print_report(self):

        action = input("Please enter the key word: ").lower()
        while action != "report":
            action = input("Incorrect word entered: DO YOU MEAN TO ENTER 'report': ")
            action = action
        print(f"""
        Current printer resources:         
        ink:    {self.printer_resources["ink"]}ml
        paper:  {self.printer_resources["paper"]}pc
        profit: #{self.printer_resources["profit"]}
        """)
    
    def local_currency_converter(self,total_print_price):
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

       
        currency_quantity_regex = '[0-9]$'
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
            currency_quantity_regex = '[0-9]$'
            currency_quantity = currency_quantity
            currency_quantity_validation = re.match(currency_quantity_regex, currency_quantity)
            currency_quantity_validation = currency_quantity_validation


        

        amount_paid = currency_note * int(currency_quantity) 

        return amount_paid

    
    def update_profit(self, amount_paid):
        updated_price = self.printer_resources["profit"] + amount_paid
        self.printer_resources["profit"] = updated_price

    
    def check_resources(self,print_format, number_of_pages):
        
        ink_available = self.printer_resources["ink"]
        paper_available = self.printer_resources["paper"]
       
      
        if print_format == "coloured":
            
            ink_required_per_one = self.printer_formats[print_format]["materials"]["ink"]
            total_ink_volume_required = ink_required_per_one * number_of_pages
           
            if total_ink_volume_required > ink_available:
                print("Sorry there is  not enough ink")
                self.start()
            elif number_of_pages > paper_available:
                print("Sorry there is  not enough paper")
                self.start()
            else:
                return  total_ink_volume_required, number_of_pages, print_format
        else:
            
            ink_required_per_one = self.printer_formats[print_format]["materials"]["ink"]
            total_ink_volume_required = ink_required_per_one * number_of_pages
          
            if total_ink_volume_required > ink_available:
                print("Sorry there is  not enough ink")
                self.start()
            elif number_of_pages > paper_available:
                print("Sorry there is  not enough paper")
                self.start()
            else:
                return total_ink_volume_required, number_of_pages, print_format


    def process_price(self,print_format, number_of_pages ): 
       
        total_ink_required, page_quantity, print_format = self.check_resources(print_format, number_of_pages)
        
        amount_per_print = self.printer_formats[print_format]['price']
        total_print_price = amount_per_print * page_quantity
        amount = self.local_currency_converter(total_print_price)
        return amount, total_print_price

    def check_transaction(self,print_format, number_of_pages):
        amount_paid, cost_price = self.process_price(print_format, number_of_pages)
        
       
        if amount_paid < cost_price:
            print("Sorry that's not enough money, Money refunded")
            return "Unsuccesful"
        
        elif amount_paid == cost_price:
            self.update_profit(amount_paid)
            return "Succesful"
       
        elif amount_paid  >  cost_price:
            
            change = amount_paid - cost_price
            
            print(" ")
            print(f"Here is #{change} in change")
            
            self.update_profit(amount_paid)
            return "Succesful"
    
    
    def Print_user_project(self,print_format, number_of_pages):
        transaction_status = self.check_transaction(print_format, number_of_pages)
        total_ink_needed, total_paper_needed, _ = self.check_resources(print_format, number_of_pages)
      
        if transaction_status == "Succesful":
            
            self.printer_resources["ink"] -= total_ink_needed
            self.printer_resources["paper"] -= total_paper_needed

            
            print ("""
            ---------------------------------
            Here is your project
            Thank you for using our services
            ---------------------------------
            """)



   
print_job = Printer()
print_job.start()





