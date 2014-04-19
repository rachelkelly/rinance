# 2014 rachel kelly, creative commons license
# remixing, redistribution ok with credit please

# this is a third attempt at this program!
# turns out there are lots of ways to approach this problem.

# program map
# first, in_or_out determines whether check deposit(in) or billpay(out)
# in: 
# a function called money_distribution() determines, based on
# deposit, if it will be a total distribution or a partial one,
# "partial" being that the user will decide how much & where the
# amounts will be distributed.
# out:
# a function called billpay() will first ask if a) normal, so all EOM bills
# will automatically be deducted from their respective envelopes, or
# b) abnormal and the user will indicate which bill is being paid & how much.

def in_or_out():
    print "money in or out?"
    in_out_choice = raw_input("> ")
    if in_out_choice == "in":
        #have to make this var
        money_distribution()
    elif in_out_choice == "out":
        #have to still make this var
        billpay()
    elif in_out_choice == "quit":
        exit(0)
    else:
        print "no doof, type 'in' or 'out', or type 'quit' to, yknow."
        in_or_out()

in_or_out()