# ['codewars', 'flick', 'code', 'wars'] ➞ [True, False, False, False]
def flick_switch(lst):
    state = True
    results = []
    
    for word in lst:
        if word == "flick":
          state = not state
        results.append(state)
    return results
