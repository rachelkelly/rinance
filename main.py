# 2014 rachel kelly, creative commons license
# a program for budgeting
# envelopes.txt refers to file from which vars come to create dict
#   and to write values back as well.
# envelopes_dict = {} refers to the dict which will hold & manipulate
#   values for incoming/outgoing funds.

# TO-DO:
#   - read moneyfile values correctly & import to dict
#   - write moneyfile values back out correctly
#   - solve var amount complication for outgoing funds
#   - bill-pay portion
#   - refactor to class? or at least make some functions
#   - shit.  have to change all vars to dict[keys], or something
#   - make executable

# first: make an empty dict & read all lines in as dict key/vals
envelopes_dict = {}
moneyfile = open("envelopes.txt", "rw")
#for money_key, money_val in moneyfile:
    #envelopes_dict[money_key] = money_val
    #pass

# next: determine whether this is for taking from or adding to envelopes_dict.
print "money in or out?"
in_or_out = raw_input("> ")

if in_or_out == "in":
    print "how much money is coming in?  no decimals, just round down."
    amount = int(raw_input("> "))
    #entire amount conditional below sb here probably 

elif in_or_out == "out":
    bill_paying_list = []
    print "which bills?  options are rent, sprint, oil, electricity,"
    print "clothes, shoes, airfare, vacation, & more to come."
    bill_pay_choice = raw_input("> ")
    if bill_pay_choice in envelopes_dict:
        pass
        # ask how much to take & then do it.
        # this should probably be a function.

elif in_or_out == "exit":
    exit(0)

else:
    print "type 'in' or 'out'.  or type 'exit' to quit."


#below line for testing purposes - this & all other static_ vars
#sb read in from moneyfile var.
static_rent = static_sprint = static_oil = 0

# this is probably where a class would minimize this code
if amount > 1500:
    in_rent = 525
    static_rent = static_rent + in_rent
    amount = amount - in_rent
    print "envelope rent: $%r  amount left to distribute: $%r" % (static_rent, amount)
 
    in_sprint = 200
    static_sprint = static_sprint + in_sprint
    amount = amount - in_sprint
    print "envelope sprint: $%r  amount left to distribute: $%r" % (static_sprint, amount)

    in_oil = 50
    static_oil = static_oil + in_oil
    amount = amount - in_oil
    print "envelope oil: $%r  amount left to distribute: $%r" % (static_oil, amount)

    otherthing = 700
    amount = amount - otherthing
    
    savings = 12
    print "now we'll put the left-over $%r into savings" % amount
    savings = savings + amount
    print "savings has added all that was left & is now at: $%r" % savings
    amount = 0
    print "amount has been zeroed out."
    assert amount == 0

else:
    static_vacation = static_vacation + amount
    print "not a full salary check, so we'll put it all into fluff"
    print "vacation fund now at $%r" % static_vacation

# pseudocode: write all static_vars to envelopes_dict.txt