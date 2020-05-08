import json
from difflib import get_close_matches

with open('data.json') as json_file:
    data = json.load(json_file)
    p = input("enter: ")
    p = p.lower()
    if p in data:
        for i in data[p]:
            print(i)
    elif len(get_close_matches(p , data.keys())) > 0:
        yn = input("Did you mean % s instead? Enter Y if yes, or N if no: " % get_close_matches(p, data.keys())[0])
        yn = yn.lower()
        if yn == 'yes' or yn == 'y':
            p = get_close_matches(p, data.keys())[0]
            for i in data[p]:
                print(i)
        else:
            print("We are unable to understand your word")
    else:
        print("We are unable to understand your word")
