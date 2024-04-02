temp = {}


def player(prev_play, opponent_history=[]):

    global temp

    #Default guess
    guess = "R"

    #Number of elements in the sequence
    num = 6

    # Add the opponents last play to the list
    if prev_play in ["R", "P", "S"]:
        opponent_history.append(prev_play)

    # If the length of the opponents history is greater than the number of elements in the sequence
    if len(opponent_history) > num:
        # Get the last num elements of the opponents history
        inp = "".join(opponent_history[-num:])

        # If the sequence is in the dictionary, add 1 to the value
        if "".join(opponent_history[-(num + 1):]) in temp.keys():
            temp["".join(opponent_history[-(num + 1):])] += 1
        else:
            temp["".join(opponent_history[-(num + 1):])] = 1

        # Possible next moves
        possible = [inp + "R", inp + "P", inp + "S"]


        for i in possible:
            if not i in temp.keys():
                temp[i] = 0


        predict = max(possible, key=lambda key: temp[key])

        ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

        guess = ideal_response[predict[-1]]

    return guess