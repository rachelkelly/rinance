#some silly attempt at brian's perl brinance

def loadMoney(fileName):
	moneyFile = open(fileName, "r")

print "how much dollaz you got"
oldMoney = float(raw_input())
print "how much dollaz you get"
newMoney = float(raw_input())
currentMoney = oldMoney + newMoney
print "so you're adding %s to your old monay, %s, which is %s." % (newMoney, oldMoney, currentMoney)

def paycheck(newMoney):
	if newMoney >= 2000:
		print "is this a paycheck?"
		payYN = raw_input()
			if payYN == "y":
				print "whose?  jon or rachel?"
				payWho = raw_input()
				if payWho == "jon":
					print "ok!  jon's paycheck = $%s" %newMoney
				elif payWho == "rachel":
					print "ok!  rachel's paycheck = $%s" %newMoney
				elif payWho == "quit":
					print "ok fine"
					#do something here, maybe go strt to subdivision()?
				else:
					print "type 'jon', 'rachel', or 'quit'."
			elif payYN == "n":
				print "don't get all pissed off about it I was just curious"
				#subdivision()?
			else:
				print "type 'y' or 'n'"


def subdivision(newMoney):
	print "since I'm fabulous and brilliant, I'll go ahead and subdivide your new dollaz."

	subdividable = newMoney
	#all these categories will have to have another file to refer to
	bills = bills + 1650
	subdividable =- bills

	print "after bills (rent, electricity, water, comcast), you have %s left." % subdividable
	print "you have %s in the billz envelope" % bills

	shoes = shoes + 10
	subdividable =- shoes

	print "after adding to shoe fund you have %s left" %subdividable
	print "you got hella hella %s for shoez" % shoes

	vacay =+ 100
	subdividable =- vacay

	print "after adding to vacation fund you have %s left" % subdividable
	print "you have $%s left for hella boozin' in the cocomos" % vacay

	clothes =+ 50
	subdividable =- clothes

	print "left: %s" % subdividable
	print "clothesfund: %s" % clothes

	oil =+ 50
	subdividable =- oil

	print "left: %s" % subdividable
	print "oil: %s" % oil

def summary(currentMoney):
	
