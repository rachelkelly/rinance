# 2014 rachel kelly, creative commons license
# a program for budgeting

#some pseudocode:
#open moneyfile read/write
#envelopes = {}
#for line in moneyfile:
#   make dict, keys are things-to-pay & values are $$ designated
#   each thing-to-pay
#   print things-to-pay
#
#then "what is incoming amount"

#below line for testing purposes
#static_rent = static_sprint = static_oil = 0

amount = 1550
if amount > 1500:
    in_rent = amount-(amount-525)
    static_rent = static_rent + in_rent
    amount = amount - in_rent

    in_sprint = amount-(amount-200)
    static_sprint = static_sprint - in_sprint
    amount = amount - in_sprint

    in_oil = amount - (amount-50)
    static_oil = static_oil - in_oil
    amount = amount - in_oil
    
    

    print amount
#	
#       
#	
# please enter $ currently in BOFA:
