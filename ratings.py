# create a function that takes in a file as an argument
# create a blank dictionary
# split the lines into indices
# store the indices into a dictionary
# return sorted dictionary


"""Restaurant rating lister."""


# put your code here
def restaurant_ratings(filename):
    the_file = open(filename)
    ratings = {}

    for line in the_file:
        line = line.rstrip()
        split_line = line.split(":")
        restaurant_name, rating = split_line
        ratings[restaurant_name] = rating

    user_restaurant = input("Input restaurant to rate: ")
    user_rating = input("Input rating: ")
    ratings[user_restaurant] = user_rating

    sorted_ratings = sorted(ratings)

    for restaurant in sorted_ratings:
        print(f"{restaurant} is rated at {ratings[restaurant]}")
    
    the_file.close()

restaurant_ratings("scores.txt")        