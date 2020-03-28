#                   DESAFIO 105
#   Create a program that has a function caled_ grades() , receiving than multiple grades of students and will return a
# DICTIONARY, with the folling informations:
#   - Quantity of grades| - Higher Grade | - Lower Grade | - Average |- SITUATION optional


def grades(*g, sit=False):
    """
                    Function to Calculate Student Grades/ GPA
    :param g:        grades
    :param sit:      situation of student
    :return:         all the info collected
    """
    info = dict()
    info['Total'] = len(g)
    info['Higher'] = max(g)
    info['Lower'] = min(g)
    info['avg'] = sum(g) /len(g)
    if sit:
        if info['avg'] >= 9:
            info['Situation'] = 'AWESOME'
        elif info['avg'] >= 7:
            info['Situation'] = "GOOD"
        elif info['avg'] > 5:
            info['Situation'] = "MODEST"
        elif info['avg'] < 5 :
            info['Situation'] = "POOR"
    return info



#---------PROGRAMA PRINCIPAL
ans = grades(6, 7.9, 5.0, 9.0, sit=True)
print(ans)
help(grades)
