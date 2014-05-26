# 2014 rachel kelly, creative commons license
# remixing, redistribution ok with credit please

# this is a third attempt at this program!
# turns out there are lots of ways to approach this problem.

# first, in_or_out() determines whether payday(in) or bills(out)
# 
# in:
# fn envelope_distribution() determines payday distribution.  if amt > 1000,
# then 550 to rent, 75 to sprint, 50 to electric, 40 to comcast, 50 to geico,
# 50 to water, 200 to food, rest to savings
# if amt < 1000, 300 to loans, rest to savings
# all contributions go toward the item in moneyitems.  not sure how this
# will work just yet.  it will add to static_$ENVELOPE and write it to
# envelopes.txt file.
#
# out:
# fn billpay() will print all items in moneyfile into a dict called
# moneyitems.  moneyitems is global so any function can use it.
# then the user will indicate which bill she is to pay.  then if the input
# has a match in {moneyitems}, it will ask "is it a normal payout," and if it
# is, it will take that amount out.
# e.g. "is 'static_sprint' a normal payout this month," "yes," "ok, taking
# $160 out of 'static_sprint' envelope."
# after a bill is paid, it will ask the user if she wants to pay another.
# if so, then the process repeats identically.
# if not, the program prints all bills paid (so a new dict is made of paid
# bills to report at end of program), all envelope quantities.

normal_bills = {'normal_sprint_out': 160, 'normal_oil_out': 50, 
                'normal_rent_out': 1050, 'normal_comcast_out': 75,
                'normal_loans_out': 450, 'vacation': 50}

print normal_bills

inexact_bills = ["electric", "savings", "groceries", "food out", 
                 "clothes", "vacation"]

print "inexact bills: %s" % inexact_bills

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
    
print moneyitems
moneyfile.close()

# beginning of progrm

def in_or_out():
    print "hi!  money in or out?"
    in_out_choice = raw_input("> ")    

    if in_out_choice == "in":
        envelope_distribution(in_out_choice)    
    elif in_out_choice == "out":
        bill_pay(in_out_choice)
    elif in_out_choice == "quit":
        exit(0)
    else:
        print "no doof, type 'in' or 'out', or type 'quit' to, yknow."
        in_or_out()

def envelope_distribution(in_out_choice):
    pass 

# this has a long way to go
def bill_pay(in_out_choice):
    print "which bill are you paying?"
    whichbill = raw_input("> ")
    for lineitem in moneyitems:
        if whichbill == moneyitems[lineitem]: #not sure if this will work
            billtopaynow = whichbill
            print billtopaynow
        else:
            print "not printing billtopaynow"
            
    if whichbill == moneyitems[lineitem]:
        print item
    else:
        print "didn't work"
    if whichbill in moneyitems:
        
        print "the %s is usually %s $%d." #% (moneyitems[whichbill], [*])
        # how to say "ok whichbill == its dict assignment & its value"?
        print "is that how much it is this time?  y/n"
        #above line: e.g. 'the sprint bill is usually $175.  is that...'
        print "you can also quit at this point."
        
        
        typical_choice = raw_input("> ")
        
        if typical_choice == "y":
            # if whichbill in normal_bills, then take closest match ... ?
            print "ok, taking $x from thatbill" # % (x, y) 
        elif typical_choice == "n":
            print "n"
        elif typical_choice == "quit":
            exit(0)
        else:
            bill_pay()

#test harness attempt
#it works but is repetitive for me - but that's ok maybe!
#"testing turns fear into boredom"
#for i in range (10):
    #in_or_out()

in_or_out()