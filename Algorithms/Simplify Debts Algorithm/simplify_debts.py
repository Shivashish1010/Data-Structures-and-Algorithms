from collections import defaultdict
import heapq

def simplify_debts(transactions):

    total = defaultdict(int)

    for transaction in transactions:
        giver, receiver, amount = transaction
        total[giver] -= amount
        total[receiver] += amount

    credit = []
    debit = []

    for name, amount in total.items():
        if amount>0:
            credit.append((-amount, name))
        if amount<0:
            debit.append((amount, name))
        
    heapq.heapify(credit)
    heapq.heapify(debit)
    answer = []

    while credit and debit:
        credit_value, credit_name = heapq.heappop(credit)  
        debit_value, debit_name = heapq.heappop(debit)
        
        if credit_value < debit_value:
            amount_left = credit_value-debit_value
            answer.append((debit_name,credit_name,-1*debit_value))
            heapq.heappush(credit,(amount_left, credit_name))
        
        elif debit_value < credit_value:
            amount_left = debit_value-credit_value
            answer.append((debit_name,credit_name,-1*credit_value))
            heapq.heappush(debit,(amount_left, debit_name))
        
        else:
            answer.append((debit_name,credit_name,-1*credit_value))
    
    return answer

transactions = [
    ['Charlie','Bob',30],
    ['Gabe','David',10],
    ['Fred','Bob',10],
    ['Fred','Charlie',30],
    ['Fred','David',10],
    ['Fred','Ema',10],
    ['Bob','Charlie',40],
    ['Charlie','David',20],
    ['David','Ema',50],
]

print(simplify_debts(transactions))
