"""Restaurant rating lister."""
# Exercise located at https://ed.devmountain.com/materials/data-bp-1/exercises/core-python/
# If I come back to this, didn't finish all the further study stuff.


def process_scores():
    """Read scores file and return dictionary of {restaurant-name: score}."""
    scores = open("scores.txt")

    dictionary = {}

    for line in scores:
        # print(line)
        line = line.rstrip()
        restaurant, rating = line.split(':')
        # print(restaurant, rating)
        dictionary[restaurant] = int(rating)
    
    scores.close()
    
    # print(dictionary)
    return dictionary

def add_restaurant(dictionary):
    """Add a restaurant and rating."""

    user_key = input("Add a restuarant name: ")
    user_value = input("Add a rating: ")
    while True: # loop to validate restaurant rating user just inputted.
        try:
            user_value = int(user_value)
            if 0 < user_value < 6:
                dictionary[user_key] = int(user_value)
                return False
            else:
                user_value = input("Rating must be a number between 1 and 5. Try again: ")
                continue
        except:
            user_value = input("Rating must be a number between 1 and 5. Try again: ")
            continue
    

def print_sorted_dictionary(dictionary):
    """Print restaurants and ratings, sorted."""
    
    # sorted_dict = dict(sorted(dictionary.items()))
    # print(sorted_dict)
    for key,value in sorted(dictionary.items()):
        print(f"{key} is rated at {value}.")
        
def what_do():
    """"Asks the user what they would like to do. View restaurants + ratings, add to the list, or quit."""
    # read existing scores in from file
    scores = process_scores()
    while True:
        user_input = input("What would you like to do? Enter '1' to see all ratings, enter '2' to add and rate a new restaurant, and enter '3' to Quit.\n")
        if user_input == '1':
            # print an alphabetical list of all rated restaurants and their ratings
            print_sorted_dictionary(scores)
        elif user_input == '2':
            # allow user to add a restaurant/rating pair
            add_restaurant(scores)
        elif user_input == '3':
            return False
        else:
            user_input = input(f"Mate. '{user_input}' is invalid. Enter '1' to see all ratings, enter '2' to add and rate a new restaurant, and enter '3' to Quit.\n")

# Initiates the app.
what_do()