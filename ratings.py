# create a function that takes in a file as an argument
# create a blank dictionary
# split the lines into indices
# store the indices into a dictionary
# return sorted dictionary


"""Restaurant rating lister."""


# put your code here
def restaurant_ratings(filename):
    """Takes in a file and allows the user to manipulate the data,
    either displaying an ordered list of restaurants or adding a new one to
    the list"""
    the_file = open(filename)
    ratings = {}

    for line in the_file:
        line = line.rstrip()
        split_line = line.split(":")
        restaurant_name, rating = split_line
        ratings[restaurant_name] = rating

    while True:
        ratings = {}

        for line in the_file:
            line = line.rstrip()
            split_line = line.split(":")
            restaurant_name, rating = split_line
            ratings[restaurant_name] = rating
        
        initial_input = input("""Would you like to:

        [S]ee all ratings
        [A]dd a rating
        [Q]uit

        > """)
        if initial_input == "S":
            sorted_ratings = sorted(ratings)
            for restaurant in sorted_ratings:
                print(f"{restaurant} is rated at {ratings[restaurant]}")
        elif initial_input == "A":
            user_restaurant = input("Input restaurant to rate: ")
            user_rating = input("Input rating: ")
            if user_rating in range(1,6):
                ratings[user_restaurant] = user_rating
            else:
                print("Rating must be a number from 1 to 5.")
        elif initial_input == "Q":
            break
   
    the_file.close()

restaurant_ratings("scores.txt")
