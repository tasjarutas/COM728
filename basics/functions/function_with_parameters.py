def climb_ladder (step_remaining, step_to_crossed ):
    if step_remaining > step_to_crossed:
        print("Still some way to go!")
    else:
        print("We are almost there!")


climb_ladder(5, 2)
climb_ladder(2, 5)
