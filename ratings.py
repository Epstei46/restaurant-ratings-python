"""Restaurant rating lister."""
# Exercise located at https://ed.devmountain.com/materials/data-bp-1/exercises/core-python/


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
    dictionary[user_key] = int(user_value)
    

def print_sorted_dictionary(dictionary):
    """Print restaurants and ratings, sorted."""
    
    # sorted_dict = dict(sorted(dictionary.items()))
    # print(sorted_dict)
    for key,value in sorted(dictionary.items()):
        print(f"{key} is rated at {value}.")

# read existing scores in from file
scores = process_scores()

# allow user to add a restaurant/rating pair
add_restaurant(scores)

# print an alphabetical list of all rated restaurants and their ratings
print_sorted_dictionary(scores)