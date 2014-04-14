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

envelopes = {}
moneyfile = open("envelopes.txt", "rw")
for line in moneyfile:
    pass

#below line for testing purposes
static_rent = static_sprint = static_oil = 0

amount = 1550
if amount > 1500:
    in_rent = 525
    static_rent = static_rent + in_rent
    amount = amount - in_rent
    print "envelope rent: %r  amount left: %r" % (static_rent, amount)

    in_sprint = 200
    static_sprint = static_sprint + in_sprint
    amount = amount - in_sprint
    print "envelope sprint: %r  amount left: %r" % (static_sprint, amount)

    in_oil = 50
    static_oil = static_oil + in_oil
    amount = amount - in_oil
    print "envelope oil: %r  amount left: %r" % (static_oil, amount)

    otherthing = 700
    amount = amount - otherthing
    
    savings = 12
    print "now we'll put the left-over %r into savings" % amount
    savings = savings + amount
    print "savings has added amount & is now at: %r" % savings
    amount = 0
    print "amount: %r" % amount
#	
#       
#	
# please enter $ currently in BOFA:
