# 2014 rachel kelly, creative commons license
# remixing, redistribution ok with credit please

# turns out there are lots of ways to approach this problem.

normal_bills = {'normal_sprint_out': 160, 'normal_oil_out': 50, 
                'normal_rent_out': 1050, 'normal_comcast_out': 75,
                'normal_loans_out': 450, 'vacation': 50}

inexact_bills = ["electric", "savings", "groceries", "food out", 
                 "clothes", "vacation"]

# the following lines until in_or_out() were formerly a defined fn,
# but the dict needs to be global so everybody can utilize it equally

moneyfile = open("envelopes.txt", "r")
moneyitems = {}

for line in moneyfile:
    entry = line.strip().split(",")
    lineitem = entry[0]
    amount = entry[1]
    moneyitems[lineitem] = amount
    print "current %s amount: $%r" % (lineitem, amount)
    # lineitem, amount = line.strip().split(",")
    
print moneyitems
moneyfile.close()

# beginning of progrm

def in_or_out():
    print "hi!  money in or out?"
    in_out_choice = raw_input("> ")    

    if in_out_choice == "in":
        envelope_distribution()    
    elif in_out_choice == "out":
        get_bill()
    elif in_out_choice == "quit":
        exit(0)
    else:
        print "no doof, type 'in' or 'out', or type 'quit' to, yknow."
        in_or_out()

def envelope_distribution():
    pass 

def get_bill():
    print "which bill are you paying (which envelope are you taking from)?"
    whichbill = raw_input("> ")
    if whichbill in moneyitems:
        pay_bill(whichbill)
    else:
        raise ValueError("no bill with name "+whichbill)
    
# this has a long way to go
def pay_bill(bill_to_pay):
    if bill_to_pay in normal_bills:            
        print "the typical amount out for %s is usually $%d." % (moneyitems[bill_to_pay], normal_bills[bill_to_pay])
        #thisbillmoney = moneyitems[whichbill:value]
        print "is that how much it is this time?  y/n"
        #above line: e.g. 'the sprint bill is usually $175.  is that...'
        print "you can also quit at this point."
        typical_choice = raw_input("> ")            
        if typical_choice == "y":
            # if bill_to_pay in normal_bills, then take closest match ... ?
            print "ok, taking $x from thatbill" # % (x, y)
            #moneyitems[bill_to_pay] = moneyitems[whichbill] - normal_bills[bill_to_pay]
        elif typical_choice == "n":
            print "n"
        elif typical_choice == "quit":
            exit(0)
        else:
            pay_bill()
    elif bill_to_pay in inexact_bills:
        print "ok!  how much are you going to pay on %s?" #% inexact_bills[bill_to_pay]???
    else:
        pay_bill()

#test harness attempt
#it works but is repetitive for me - but that's ok maybe!
#"testing turns fear into boredom"
#for i in range (10):
    #in_or_out()

in_or_out()
