##############################################################################
#
#    MICHIGAN COVID-19 DATA PROCESSING - MARCUS WOLFF
#
#    Options to view:
#        1: Minimum and Maximum of all vaccinated
#        2: Minimum and Maximum of those 12 and older
#        3: Minimum and Maximum of those 18 and older
#        4: Minimum and Maximum of those 65 and older
#        5: Total vaccinated for Michigan
#
#    Algorithm
#    
#    Create file pointer by calling open_file() function
#    Call display_options() function to show menu
#    Enter main loop, continuing until user enters "q" to quit
#        Based on user choice, calcuate requested data by calling
#            find_min_max_column() function
#        Call fix_count_string() function to ensure last word of county name 
#            is "County"
#        Display requested data by calling display_min_max() function
#        Prepare for next repetition: obtain new input and display menu
#    Close the file
#    END
#
##############################################################################
def reset_file_pointer_to_beginning(fp):
    """
    DO NOT CHANGE
    Resets file pointer to the beginning and returns updated file pointer
    
    Parameters: file pointer object
    return: file pointer object
    """
    fp.seek(0)
    return fp

def open_file():
    ''' This function prompts for a file name until a file is opened for \
        reading, and returns the file object associated with it.'''
    
    # Try to take user input for a file name, and catch the error if the file
    # Name is invalid
    while True:
        try:
            file_name_str = input("Input a file for reading: ")
            file_pointer = open(file_name_str,"r")
            break
    
        except FileNotFoundError:
            print("Invalid filename, please try again.")
            
    return file_pointer

def fix_county_string(s):
    ''' This function takes one parameter, s, and modifies the county name \
        to end in "County" exactly, returning the modified form of s.'''
        
    s_word_list = s.strip().split()
    # If the county name already ends in "County", do not modify anything
    if s_word_list[-1] == "County":
        return s
    
    # Otherwise, modify the county name accordingly
    elif s_word_list[-1] == "C":
        s_new = s + "ounty"
        return s_new
    
    elif s_word_list[-1] == "Co":
        s_new = s + "unty"
        return s_new
    
    elif s_word_list[-1] == "Cou":
        s_new = s + "nty"
        return s_new
    
    elif s_word_list[-1] == "Coun":
        s_new = s + "ty"
        return s_new
    
    elif s_word_list[-1] == "Count":
        s_new = s + "y"
        return s_new
    
    else:
        pass
        return s

def find_min_max_column(fp,start,end):
    ''' This function takes three parameters, the function pointer and the \
        starting and ending points for the slicing of file lines. It returns \
        the minimum and maximum values of the user-desired column.'''
    
    # Initialize variables to be returned
    min_val = 1e9
    min_county = ""
    max_val = 0
    max_county = ""
    
    reset_file_pointer_to_beginning(fp)
    fp.readline()
    
    # Min-max algorithm
    for line_str in fp:
        current_percentage = float(line_str[start:end].strip())
        
        if current_percentage < min_val:
            min_val = current_percentage
            min_county = line_str[24:43]
            min_county = fix_county_string(min_county)
            
        if current_percentage > max_val:
            max_val = current_percentage
            max_county = line_str[24:43]
            max_county = fix_county_string(max_county)
    
    return min_val,min_county,max_val,max_county

def display_min_max(s,min_val, min_county, max_val, max_county):
    ''' This function is purely for displaying output and does not return \
        anything. It takes five string parameters and formats the output \
        properly.'''
    
    # Display output with proper formatting
    print("\nPercent vaccinated for {}".format(s))
    print("\n\t Minimum is in {} at {}%".format(min_county,min_val))
    print("\t Maximum is in {} at {}%".format(max_county,max_val))
 
def all_vaccinated(fp):
    ''' This function takes one parameter, the file pointer, and returns \
        the total number of Michigan residents that are vaccinated.'''
    
    total_int = 0
    
    reset_file_pointer_to_beginning(fp)
    fp.readline()
    
    # Compute a running total for the total number of vaccinated residents
    for line_str in fp:
        
        current_line_int = int(line_str[86:100].strip())
        total_int = total_int + current_line_int
    
    return total_int
        
def display_options():
    """
    DO NOT CHANGE
    Display menu of options for program
    """
    OPTIONS = """\nMenu
    1: Minimum and Maximum of all vaccinated
    2: Minimum and Maximum of those 12 and older
    3: Minimum and Maximum of those 18 and older
    4: Minimum and Maximum of those 65 and older
    5: Total vaccinated for Michigan
    q: quit\n"""
    print(OPTIONS)
 

def main():
    ''' The main function is the location from where we call our other \
        functions.'''
        
    # Create the file pointer and display the menu to the user
    fp = open_file()
    display_options()
    
    option = input("Select and option, q to quit: ")
    
    # Continue to provide data, provided user input is not "q"
    while option != "q":
        
        # Account for invalid inputs
        while not(option in "12345q"):
            print("Invalid option; please try again.")
            option = input("Select and option, q to quit: ")
        
        if option == "1":
            
            s = "all"
            
            # Find the min and max value and county for all residents of 
            # The county
            min_value,min_county,max_value,max_county = \
            find_min_max_column(fp,71,85)
            
            # Reformat variables with proper types for display_min_max()
            # Function
            min_value = str(min_value)
            max_value = str(max_value)
            
            # Display the output properly
            display_min_max(s,min_value,min_county,max_value,max_county)
        
        elif option  == "2":
            
            s = "age 12 and older"
            
            # Find the min and max value and county for 12 and older
            min_value,min_county,max_value,max_county = \
            find_min_max_column(fp,136,154)
            
            # Reformat variables with proper types for display_min_max()
            # Function
            min_value = str(min_value)
            max_value = str(max_value)
            
            # Display the output properly
            display_min_max(s,min_value,min_county,max_value,max_county)
        
        elif option == "3":
            
            s = "age 18 and older"
            
            # Find the min and max value and county for 18 and older
            min_value,min_county,max_value,max_county = \
            find_min_max_column(fp,183,201)
            
            # Reformat variables with proper types for display_min_max()
            # Function
            min_value = str(min_value)
            max_value = str(max_value)
            
            # Display the output properly
            display_min_max(s,min_value,min_county,max_value,max_county)
        
        elif option == "4":
            
            s = "age 65 and older"
            
            # Find the min and max value and county for 65 and older
            min_value,min_county,max_value,max_county = \
            find_min_max_column(fp,230,234)
            
            # Reformat variables with proper types for display_min_max()
            # Function
            min_value = str(min_value)
            max_value = str(max_value)
            
            # Display the output properly
            display_min_max(s,min_value,min_county,max_value,max_county)
            
        elif option == "5":
            
            # Find the total number of Michigan residents vaccinated
            total_int = all_vaccinated(fp)
            
            # Print output for this case without using display_min_max()
            # Function
            print("\nTotal vaccinated in Michigan: {:,d}".format(total_int))
            
        # Preparation for the next repetition
        display_options()
        option = input("Select and option, q to quit: ")
        
    fp.close()
    
# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.         
if __name__ == "__main__":
    main()
