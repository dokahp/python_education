import argparse
import math

# Initiate the parser
parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=str)
parser.add_argument("--payment", type=int)
# Read arguments from the command line
args = parser.parse_args()

def count_of_month(wanted_monthly_payment, interest_rate, sum_of_credit):
    monthly_rate = float(interest_rate) / 12 / 100
    count = math.log((wanted_monthly_payment / (wanted_monthly_payment -
                                                (monthly_rate * sum_of_credit))), monthly_rate + 1)
    year = math.ceil(count) // 12
    month = math.ceil(count) % 12
    if year < 1:
        print("You need {month} months to repay credit!".format(month=month))
    elif month < 1:
        print("You need {year} years to repay credit!".format(year=year))
    elif year > 1 and month > 1:
        print("You need {year} years and {month} months to repay credit!".format(year=year, month=month))
    elif year == 1 and month == 0:
        print("You need {year} year to repay credit!".format(year=year))
    overpayment = (wanted_monthly_payment * ((year * 12) + month)) - sum_of_credit
    print("Overpayment = ", overpayment)
    return math.ceil(count)  # возвращаем количество месяцев, чтобы использовать в других функциях

def credit_principal(annuity, periods, tax):
    i = float(tax) / 12 / 100
    niz_verx = i * math.pow((1 + i), periods)
    niz_niz = math.pow((1 + i), periods) -1
    all_niz = niz_verx / niz_niz
    cr_principal = math.floor(annuity / all_niz)
    print("Your credit principal = {cr_pr:.0f}!".format(cr_pr=cr_principal))
    print("Overpayment = ", annuity * periods - cr_principal)
def annuity_payment(credit_sum, periods, tax):
    i = float(tax) / 12 / 100
    annuity_p = math.ceil(credit_sum * (i * math.pow(1+i, periods) / (math.pow((1 + i), periods) - 1)))
    print("Your annuity payment = {annu_p}!".format(annu_p=annuity_p))
    print("Overpayment = ", annuity_p * periods - credit_sum)
    return annuity_p

def diff_payment(credit_sum, periods, tax):
    overpayment = 0
    tax = float(tax) / 12 / 100
    for i in range(1,periods + 1):
        diff = math.ceil((credit_sum / periods) + tax * (credit_sum - (credit_sum * (i - 1)) / periods))
        overpayment += diff
        print("Month {i}: paid out {diff:.0f}".format(i=i, diff=diff))
    print("Overpayment = ", overpayment-credit_sum)

if args.type == 'diff':
    try:
        diff_payment(args.principal, args.periods, float(args.interest))
    except:
        print('Incorrect parameters')

elif args.principal is None and args.payment > 0 and args.periods > 0 and float(args.interest) > 0:
    try:
        credit_principal(args.payment, args.periods, args.interest)
    except:
        print('Incorrect parameters')

elif args.payment is None and args.type == 'annuity' and args.principal > 0 and args.periods > 0:
    try:
        annuity_payment(args.principal, args.periods, args.interest)
    except:
        print('Incorrect parameters')
elif args.type == 'annuity' and args.principal > 0 and args.payment > 0:
    try:
        count_of_month(args.payment, args.interest, args.principal)
    except:
        print('Incorrect parameters')
else:
    print('Incorrect parameters')