#           Desafio 044
#   Elabore um programa que calcule o valor a ser oago por um produto , considerando seu preco normal e condicao de
# pagamento : - A vista/ dinheiro ou cheque : 10% desconto | 2x no cartao preco normal
# A vista no cartao 5% desconto | 3x ou mais no cartao : 20% juros |

print("        Welcome to Will's Store !       "
      " Lets calculate your item's final price.")
price = float(input('What is the price of the items you are purchasing : $'))
payOP = int(input('''What is the type of payment 
[Cash/Check]         =  1
 [Debit]             =  2
 [Credit 2x]         =  3
 [Credit 3x or more] =  4 \n'''))

if   payOP == 1:
    total = price - (price * 0.10)
elif payOP == 2:
    total = price - (price * 0.05)
elif payOP == 3:
    total = price
    parcel = total / 2
    print('You have have Two payments of ${:.2f}'.format(parcel))
elif payOP == 4:
    total = price + (price * 0.20)
    parcQ = int(input('How many payments?'))
    parcel = total /  parcQ
    print('You have Three payments of ${:.2f}'.format(parcel))
print('The product was ${:.2f} , product price now is ${:.2f} with interest.'.format(price, total))
