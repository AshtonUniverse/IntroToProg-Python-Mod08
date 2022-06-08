# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# ALarkin,6.7.2022,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'Products.txt'
lstOfProductObjects = []  # A list that acts as a 'table' of rows

class Product:
    """Stores data about a product:

    properties:
       product_name: (string) with the product's name

       product_price: (float) with the product's standard price
    methods:
        to_string(): (str) all properties

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class

        ALarkin,6.7.2022,Modified code to complete assignment 8
    """
    # TODO: Add Code to the Product class

    # -- Constructor --
    def __init__(self, product_name: str, product_price: float):
        # -- Attributes --
        self.__product_name = str(product_name)
        self.__product_price = float(product_price)

    # -- Properties --
    # product_name
    @property
    def product_name(self):
        return str(self.__product_name)

    @product_name.setter
    def product_name(self, value: str):
        if str(value).isnumeric() == True:
            self.__product_name = value
        else:
            raise Exception("Product names cannot be number!")

    # product_price
    @property
    def product_price(self):
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, value: float):
        if str(value).isnumeric() == False:
            self.__product_price = float(value)
        else:
            raise Exception("Price must be numbers!")

    # -- Methods --
    def to_string(self):
        """ alias of __str__()"""
        return self.__str__()

    def __str__(self):
        """ Convert product data to string"""
        return self.product_name + ',' + str(self.product_price)

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects)

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class

        ALarkin,6.7.2022,Modified code to complete assignment 8
    """

    # TODO: Add Code to process data from a file
    @staticmethod
    def read_data_from_file(file_name: str):
        """Reads data from a file into a list of dictionary rows:

         :param file_name: (string) with name of file:
         :return: (list) of rows
        """
        list_of_rows = []
        try:
            import os.path
            isfile_bln = (os.path.isfile(file_name))
            if (isfile_bln == True):
                file = open(file_name, "r")
                for line in file:
                    data = line.split(",")
                    row = Product(data[0], float(data[1]))
                    list_of_rows.append(row)
                file.close()
        except FileNotFoundError as e:
            print("Error file not found:", e, sep='\n')
        except Exception as e:
            print()
            print("Error reading data from file:", e, sep='\n')
        return list_of_rows

    # TODO: Add Code to process data to a file
    @staticmethod
    def save_data_to_file(file_name: str, list_of_rows: list):
        """Writes data from a list of dictionary rows to a file:

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: status_bln (boolean) return status
        """
        save_bln = False
        try:
            strOverwrite = str(input("Overwrite: " + file_name + "?" + " [y/n] ").strip().lower())
            if (strOverwrite == 'y'):
                objFile = open(file_name, "w")
                for row in list_of_rows:
                    objFile.write(row.to_string() + "\n")
                objFile.close()
                save_bln = True
                print()  # Add an extra line for looks
                print("*************")
                print("Data Saved")
                print("*************")
            else:
                print("Overwrite = No | File not overwritten")
        except Exception as e:
            print()  # adding a new line for looks
            print("Error saving data:", e, sep='\n')
        return save_bln


# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    """Performs Input and Output tasks:

    methods:
    menu()
    choice()
    product_list()
    input_data()

    changelog: (When,Who,What)
        ALarkin,6.7.2022,
    """

    # TODO: Add code to show menu to user
    @staticmethod
    def menu():
        """
        Display a menu of options to the user

        :return: nothing
        """
        print('''
        ****************************
        Product List - Option Menu
        ****************************
        1) Show current data
        2) Add a product
        3) Save data to file        
        4) Exit program
        ****************************
        ''')
        print()  # Add an extra line for looks

    # TODO: Add code to get user's choice
    @staticmethod
    def choice():
        """
        Get users menu choice

        :return: (str) choice
        """
        choice = str(input("Choose an option? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def product_list(list_of_rows: list):
        """
        Print current products in the list of rows:

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******** Current Product List *************")
        for row in list_of_rows:
            print(row.product_name + " (" + str(row.product_price) + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    # TODO: Add code to get product data from user
    @staticmethod
    def input_data():
        """
        Get user input data

        :return: Product object with input data
        """
        try:
           product = str(input("Enter product name? - ").strip())
           price = float(input("Enter product price? - ").strip())
           print()  # Add an extra line for looks
           p = Product(product_name=product, product_price=price)
        except Exception as e:
           print(e)
        return p

        # Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body

# TODO: Load data from file into a list of product objects when script starts
lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)

while (True):
    # TODO: Show user a menu of options
    IO.menu()  # Shows menu
    # TODO: Get user's menu option choice
    strChoice = IO.choice()
    # TODO: Show user current data in the list of product objects
    if strChoice.strip() == '1':
        IO.product_list(lstOfProductObjects)  # Show current data in the list/table
        continue
    # TODO: Let user add data to the list of product objects
    if strChoice.strip() == '2':
        lstOfProductObjects.append(IO.input_data())
        continue
    # TODO: Let user save current data to file
    elif strChoice == '3':
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
        continue
    # TODO: Exit program
    elif strChoice == '4':
        break

# Exit the program
input("\nPress the enter key to exit.")