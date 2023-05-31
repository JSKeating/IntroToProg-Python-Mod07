# ---------------------------------------------------------------------------- #
# Title: Assignment 07 - Home Calculator (Pickling & Error Handling)
# Description: Program takes data from user regarding the home they intend to sell,
#              calculates their estimated sale proceeds, then pickles and saves
#              the data into a binary file. Custom error functions are
#              demonstrated and used to help maintain program integrity.
# ChangeLog (Who,When,What):
# Jordan Keating,5.30.2023, Created program and ran testing
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
file_name = "HomeData.dat"  # The name of the binary file
file = None  # An object that represents a file
table_lst = []  # A list that acts as a 'table' of rows
choice = "" # A string variable to capture a user option
cont = True # Boolean variable for our while loop

import pickle # Allows us to access and use pickling functions

# Processing  --------------------------------------------------------------- #
class Processor:
    """ Performs all processing tasks"""

    @staticmethod
    def choice_check(user_choice):
        """ Catches incorrect user inputs

                :param user_choice (str) captured user input
                :return: False if no error, True if error found
                """
        try:
            if user_choice == "s":
                return False
            elif user_choice == "b":
                raise buy_not_ready()
            else:
                raise only_s_or_b()
        except Exception as e:
            print(e)
            return True

    @staticmethod
    def seller_net_proceeds(list_of_data):
        """ Calculates estimated proceeds from home sale based on user inputs

                :param list_of_data: (list) home sale price, mortgage balance, commission rate
                :return: (float) seller estimated proceeds
                """
        escrow_tax_rate = 0.0178
        escrow_fees = 3500.0
        seller_proceeds = list_of_data[0] - list_of_data[1] - (list_of_data[0]*(list_of_data[2]/100)) - list_of_data[0]*escrow_tax_rate - escrow_fees
        return seller_proceeds

    def save_data_to_file(file_name, list_of_data):
        """ Saves data to binary file

                :param file_name: (string) with name of file:
                :param list_of_data: (list) to write to binary file:
                :return: Nothing
                """
        file = open(file_name, "wb")
        pickle.dump(list_of_data, file)
        file.close()
        print("\nData saved successfully!")

    def read_data_from_file(file_name):
        """ Reads data from binary file

                :param file_name: (string) with name of file:
                :return: (list) data from file
                """
        file = open(file_name, "rb")
        unpickled_data = pickle.load(file)
        file.close()
        return unpickled_data

    def read_data_as_text(file_name):
        """ Reads data from binary file

                :param file_name: (string) with name of file:
                :return: (str) binary data from file
                """
        file = open(file_name, "r")
        data = file.read()
        file.close()
        return data

# Presentation (Input/Output) ----------------------------------------------- #
class IO:
    """  Performs input and output tasks """

    @staticmethod
    def welcome():
        """ Welcomes user to the program

        :return: nothing
        """
        print("Welcome to Jordan's Real Estate Program!")
        
    @staticmethod
    def buy_or_sell():
        """  Collect user option of "Buy" or "Sell"

        :return: string
        """
        print("\nAre you interested in buying or selling your home? ")
        option = input("Please enter 'B' for Buy or 'S' for Sell: ").strip().lower()
        return option

    @staticmethod
    def seller_inputs():
        """ Collect home sale data from user

        :return: list
        """
        salePrice = float(input("How much do you expect your home is worth? "))
        mortgage = float(input("What is your remaining mortgage balance? "))
        commission = float(input("What percentage will your agent collect for the sale? "))
        homeAddress = str(input("What is the address for this home? "))
        homeSize = int(input("What is the approx square footage for this home? "))
        return salePrice, mortgage, commission, homeAddress, homeSize

# Error Handling ------------------------------------------------------------ #
class buy_not_ready(Exception):
    def __str__(self):
        return 'Sorry, our buy options are not ready at this time!'
    
class only_s_or_b(Exception):
    def __str__(self):
        return 'Please enter only "S" for Sell or "B" for Buy'

# Main Body of Script ------------------------------------------------------- #

    # Find out what user would like to do (buy or sell)
    # If sell - Present user with estimated home sale proceeds
    #   From user - get existing mortgage, expected sale price, commission rates
    #   Detail out different expenses
    # If buy - display error code (option not yet available)

IO.welcome()
while cont == True:
    choice = IO.buy_or_sell()
    cont = Processor.choice_check(choice)
    if cont == False:
        print("\nLet's see how much you'll receive from your home sale...\n ")
        table_lst = IO.seller_inputs()
        proceeds = Processor.seller_net_proceeds(table_lst)
        print("\nYour expected net proceeds from your home sale are " , proceeds)
        save_option = input("Would you like to save this data? Y or N: ").strip().lower()
        if save_option == "y":
            Processor.save_data_to_file("HomeData.dat", table_lst)
            data = Processor.read_data_from_file("HomeData.dat")
            print("\nYour info was saved as follows: \n", data)
            pickled = Processor.read_data_as_text("HomeData.dat")
            print("Here is your info pickled: \n", pickled)
        else:
            break
    else:
        continue
print("\nThank you for using my program! See you next time!")
input("Press any key to exit")