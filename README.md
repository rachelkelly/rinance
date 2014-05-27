<<<<<<< HEAD
rinance
=======

fitting brinance to python

brian is my brother.

http://www.locoburger.org/prog/brinance/
=======
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
# fn get_bill() will ask which bill is to be paid.  bill must have a match
# in {moneyitems}.
# then in pay_bill(), if the input
# has a match in {moneyitems}, it will ask "is it a normal payout," and if it
# is, it will take that amount out of its corresponding envelope.
# e.g. "is 'static_sprint' a normal payout this month," "yes," "ok, taking
# $160 out of 'static_sprint' envelope."
# if the typical_choice == 'n', then pay_bill asks how much should come out
# of $BILL.
# after a bill is paid, it will ask the user if she wants to pay another.
# if so, then the process repeats identically.
# if not, the program writes all envelope subtractions to envelopes.txt, 
# prints all bills paid (so a new dict is made of paid
# bills to report at end of program), all envelope quantities, & exits.
# decompose bill_pay into get_bill_to_pay and pay_bill for INPUT and OUTPUT,
# respectively, VALIDATION and COMPUTATION.
>>>>>>> objectish
