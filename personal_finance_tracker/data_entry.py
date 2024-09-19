from datetime import datetime

date_format = "%m-%d-%Y"
CATEGORIES = {"I": "Income", "E": "Expense"} #Dictionary for categories
def get_date(prompt, allow_default=False):
    """
    Prompts the user for a date with the given prompt and returns it in MM-DD-YYYY
    format. If allow_default is True, the user can hit enter without entering a date
    and the function will return the current date. If the user enters an invalid date,
    the function will print an error message and recursively call itself until a valid
    date is entered. RECURSIVE FUNCTION
    """
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date. Proper format is MM-DD-YYYY. Please try again.")
        return get_date(prompt, allow_default)

def get_amount():
    
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            raise ValueError("Amount must be a non-negative non-zero value.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    """
    Prompts the user for a category and returns it as a string. If the user enters an 
    invalid category, the function will print an error message and recursively call 
    itself until a valid category is entered. The category is case-insensitive. 
    RECURSIVE FUNCTION
    """
    category = input("Enter the Category (I for INCOME, or E for EXPENSE): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category] #returns the key from dictionary above
    
    print("Invalid category. Please try again.")
    return get_category()

def get_description():
    return input("Enter description (Optional): ")