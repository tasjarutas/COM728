print("What type of cover does the book have?")
book_cover = input()
if book_cover == "soft":
    condition = input("Is the book perfect-bound?\n")
    if condition == 'yes':
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")
elif book_cover == "hard":
    print("Books with hard covers can be more expensive!")
else:
    print("Unknown cover book type")
