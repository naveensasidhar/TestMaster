current_movies={"Super Man": "10:00am",
                "Bat Man": "1:00pm",
                "Iron Man": "3:00pm",
                "Spider Man": "5:00pm"}

# Print Out All Available Movie In List
print("We are Showing The Following Movies:")
for movie_key in current_movies:
    print(movie_key)

# Inut from User
movie = input("For What Movie Would You Like To Know Showtime For?\n")

#output the showtime.
movie_showtime = current_movies.get(movie)

if movie_showtime == None:
    print("Request movie Is Not Playing Now!!!")
else:
    print(movie, "is playing at", movie_showtime)    