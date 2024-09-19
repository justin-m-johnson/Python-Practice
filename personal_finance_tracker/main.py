# Initialize the CSV file
import csv
import pandas as pd
from datetime import datetime
from data_entry import get_amount, get_category, get_description, get_date

class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["Date", "Description", "Category", "Amount"]

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)
        """
        Initialize the CSV file if it does not exist.

        This function will initialize the CSV file if it does not exist. If the file
        does exist, this function will not do anything.

        This function is a class method, which means that it can be called on the
        class itself, rather than on an instance of the class.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

    @classmethod
    def add_entry(cls, Date, Description, Category, Amount):
        new_entry = {
            "Date": Date,
            "Description": Description,
            "Category": Category,
            "Amount": Amount,
        }
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully!")
        """
        Add a new entry to the CSV file.

        This function will add a new entry to the CSV file. The entry will be added
        to the end of the file. The entry will be written in the format of a
        dictionary, where the keys are the column names and the values are the
        corresponding values for that entry.

        Parameters
        ----------
        Date : str
            The date of the entry in the format of "dd/mm/yyyy".
        Description : str
            A description of the entry.
        Category : str
            The category of the entry.
        Amount : float
            The amount of the entry.

        Returns
        -------
        None
        """

def add():
    CSV.initialize_csv()
    Date = get_date("Enter the date of the transaction (format: MM-DD-YYYY) or press enter for Today's Date: ", allow_default=True)
    Amount = get_amount()
    Category = get_category()
    Description = get_description()
    CSV.add_entry(Date, Description, Category, Amount)

add()