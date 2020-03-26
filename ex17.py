#           DESAFIO 101
# Make a programa that has a FUNCTION CALLED vote() , it will receive as a PARAMETER the year of birthday of a person
# Returning than a LITERAL VALUE ,indicating if this person right of vote is [NOT POSSIBLE / OPTIONAL / MANDATORY]


def vote(year):
    from datetime import date
    act = date.today().year
    age = act - ybday
    if age < 16:
        return f"You're {age} Years old and You can't Vote yet..."
    elif 16 >= age < 18 or age >= 65:
        return f"You're {age} Years old and Vote is Optional..."
    else:
        return f"You're {age} Years old and Vote is MANDATORY!"


ybday = int(input('What is your Year of Birthday? '))
print(vote(ybday))
