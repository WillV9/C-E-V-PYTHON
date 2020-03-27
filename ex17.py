#               DESAFIO 102
#   MAKE A PROGRAM THAT HAS A FUNCTION CALLED fatorial() receiving TWO PARAMETERS:
# The first one  indicates de number to calculate and the Second one called as SHOW will be a value logic
# optional) indicating if will showing or not in the screen the process of calculing the fatorial


def fatorial(num, show=False):
    '''
    ~~> Function to calculate a number fatorial.
    :param num: For the number
    :param show: To show the complete fatorial progress
    :return: the fatorial result
    '''
    f = 1
    print(':-:' * 15)
    for each in range(num, 0 , -1):
        if show:
            print(each, end='')
            if each > 1:
                print(f'x ', end='')
            else:
                print(f' = ', end='')
        f *= each
    return f
print(':-:'* 15)



num = int(input('Insert A number to Get their Fatorial: '))
print(fatorial(num , show=True))
