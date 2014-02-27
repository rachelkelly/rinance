rent = 1050
comcast = 75
sprint = 130
electric = 100
loans = 550
savings = 200
groceries = 400
foodOut = 300
clothes = 30
vacation = 30

expenses = [rent, comcast, sprint, electric, loans, savings, groceries, foodOut, clothes, vacation]


print "how much did you get paid"
newMoney = float(raw_input('> ')

if newMoney > 2500:
	subdivision()
else:
	pass
if newMoney > 1000:
	print "let's divide this evenly between vacation, savings & clothes."
	vacationEnvelope += (newMoney/3)
	savingsEnvelope += (newMoney/3)
	clothesEnvelope += (newMoney/3)
	summary()
else:
	print "extra?  we'll put it in savings."
	savings += newMoney
	print "okay, now you have %s in savings." % savings

def subdivision(newMoney):
	subdividable = newMoney
	print "you have %s to break up here." % subdividable

	for i in expenses:
		print "putting \$ %s toward %s envelope." % (float(i), i)
		#I don't think this will work to declare the number
		#relevant to each member of the list of expenses
		#ideally above print stmt says, at least for the rent portion:
		#"putting 1050 toward rent envelope."
		
		subdividable -= i
		#and now how to put actual amount toward each i?
		#rentenvelope += float(i)
		
		print "there is %s in the envelope belonging to %s now" % (float(i), i)
	
	print "now you've got %s left.  that's all gonna go into THE FUTURE." % subdividable
	theFutureEnvelope += subdividable
	
	assert subdividable == 0

# basically I want to do the subdivision portion in one big for loop for the list of expenses,
# iterating through correctly & then stopping after one round.


def summary():
	#want to print all envelope amounts here
	#want to print remaining (estimated?) balance on loans.
		# would probably have to import math to get e in order to do the P*e etc equation
	#also probably a good idea to list when all bills get paid.
	command = 
