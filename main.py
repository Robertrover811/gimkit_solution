from random import randint as rand
from random import choice
import matplotlib.pyplot as plt


perQuestion = 1
total = 0
# Dictionary of the available upgrades
upgrades = {
	# Money Per Question upgrade levels
  "moneyPerQuestion":{
		0:{
			"cost":0,
			"gain":1
		},
    1:{
      "cost":10,
      "gain":5
    },
    2:{
      "cost":100,
      "gain":50
    },
    3:{
      "cost":1000,
      "gain":100
    },
    4:{
      "cost":10000,
      "gain":500
    },
    5:{
      "cost":75000,
      "gain":2000
    },
    6:{
      "cost":300000,
      "gain":5000
    },
    7:{
      "cost":1000000,
      "gain":10000
    },
    8:{
      "cost":10000000,
      "gain":250000
    },
    9:{
      "cost":100000000,
      "gain":1000000
    }
  },
  "multiplier":{
		0:{
			"cost":0,
			"gain":1
		},
		1:{
			"cost":50,
			"gain":1.5
		},
		2:{
			"cost":300,
			"gain":2
		},
		3:{
			"cost":2000,
			"gain":3
		},
		4:{
			"cost":12000,
			"gain":5
		},
		5:{
			"cost":85000,
			"gain":8
		},
		6:{
			"cost":700000,
			"gain":12
		},
		7:{
			"cost":6500000,
			"gain":18
		},
		8:{
			"cost":65000000,
			"gain":30
		},
		9:{
			"cost":1000000000,
			"gain":100
		},
  },
  "streakBonus":{
		0:{
			"cost":0,
			"gain":1
		},
		1:{
			"cost":20,
			"gain":3
		},
		2:{
			"cost":200,
			"gain":10
		},
		3:{
			"cost":2000,
			"gain":50
		},
		4:{
			"cost":20000,
			"gain":250
		},
		5:{
			"cost":200000,
			"gain":1200
		},
		6:{
			"cost":2000000,
			"gain":6500
		},
		7:{
			"cost":20000000,
			"gain":35000
		},
		8:{
			"cost":200000000,
			"gain":175000
		},
		9:{
			"cost":2000000000,
			"gain":1000000
		},
  }
}

POINT_COUNT = 150

answers = []
for i in range(POINT_COUNT):
  if rand(1,100) > 80:
    answers.append(True)
  else:
    answers.append(False)


S = upgrades["streakBonus"][0]["gain"]
M = upgrades["multiplier"][0]["gain"]
Q = upgrades["moneyPerQuestion"][0]["gain"]
P = 0
n = POINT_COUNT

outputs_streak = []
lvl = 1
streak = 0
for i in range(n):
  P = P+M*(Q+(S*streak))
  outputs_streak.append(P)
  if P >= upgrades["streakBonus"][lvl]["cost"]:
    P -= upgrades["streakBonus"][lvl]["cost"]
    S = upgrades["streakBonus"][lvl]["gain"]
    lvl += 1
    streak = 0


S = upgrades["streakBonus"][0]["gain"]
M = upgrades["multiplier"][0]["gain"]
Q = upgrades["moneyPerQuestion"][0]["gain"]
P = 0
n = POINT_COUNT

outputs_multiplier = []
lvl = 1
for i in range(n):
  P = P+M*(Q+(S*i))
  outputs_multiplier.append(P)
  if P >= upgrades["multiplier"][lvl]["cost"]:
    P -= upgrades["multiplier"][lvl]["cost"]
    lvl += 1
    M = upgrades["multiplier"][lvl]["gain"]

S = upgrades["streakBonus"][0]["gain"]
M = upgrades["multiplier"][0]["gain"]
Q = upgrades["moneyPerQuestion"][0]["gain"]
P = 0
n = POINT_COUNT

outputs_question = []
lvl = 1
for i in range(n):
  P = P+M*(Q+(S*i))
  outputs_question.append(P)
  if P >= upgrades["moneyPerQuestion"][lvl]["cost"]:
    P -= upgrades["moneyPerQuestion"][lvl]["cost"]
    lvl += 1
    Q = upgrades["moneyPerQuestion"][lvl]["gain"]

S = upgrades["streakBonus"][0]["gain"]
M = upgrades["multiplier"][0]["gain"]
Q = upgrades["moneyPerQuestion"][0]["gain"]
P = 0
n = POINT_COUNT
streak = 0

outputs_cyclical = []
choices_cyclical = []
lvlQ = 1
lvlM = 1
lvlS = 1
for i in range(n):
  P = P+M*(Q+(S*streak))
  outputs_cyclical.append(P)
  if lvlQ < 10 and P >= upgrades["moneyPerQuestion"][lvlQ]["cost"]:
    P -= upgrades["moneyPerQuestion"][lvlQ]["cost"]
    Q = upgrades["moneyPerQuestion"][lvlQ]["gain"]
    if lvlQ < 10:
      lvlQ += 1

  if lvlM < 10 and P >= upgrades["multiplier"][lvlM]["cost"]:
    P -= upgrades["multiplier"][lvlM]["cost"]
    M = upgrades["multiplier"][lvlM]["gain"]
    if lvlM < 10:
      lvlM += 1

  if lvlS < 10 and P >= upgrades["streakBonus"][lvlS]["cost"]:
    P -= upgrades["streakBonus"][lvlS]["cost"]
    S = upgrades["streakBonus"][lvlS]["gain"]
    streak = 0
    if lvlS < 10:
      lvlS += 1


S = upgrades["streakBonus"][0]["gain"]
M = upgrades["multiplier"][0]["gain"]
Q = upgrades["moneyPerQuestion"][0]["gain"]
P = 0
n = POINT_COUNT
streak = 0

outputs_random = []
choice_random = []
lvlQ = 1
lvlM = 1
lvlS = 1
choice_count = 0

def buyMPQ():
  global lvlQ
  global P
  global Q
  global choice_count
  if lvlQ < 10 and P >= upgrades["moneyPerQuestion"][lvlQ]["cost"]:
    choice_count += 1
    P -= upgrades["moneyPerQuestion"][lvlQ]["cost"]
    Q = upgrades["moneyPerQuestion"][lvlQ]["gain"]
    if lvlQ < 10:
      lvlQ += 1
  return "Q"

def buyMul():
  global lvlM
  global P
  global M
  global choice_count
  if lvlM < 10 and P >= upgrades["multiplier"][lvlM]["cost"]:
    choice_count += 1
    P -= upgrades["multiplier"][lvlM]["cost"]
    M = upgrades["multiplier"][lvlM]["gain"]
    if lvlQ < 10:
      lvlM += 1
  return "M"

def buyStk():
  global lvlS
  global P
  global S
  global choice_count
  if lvlS < 10 and P >= upgrades["streakBonus"][lvlS]["cost"]:
    choice_random.append("S")
    choice_count += 1
    P -= upgrades["streakBonus"][lvlS]["cost"]
    S = upgrades["streakBonus"][lvlS]["gain"]
    streak = 0
    if lvlQ < 10:
      lvlS += 1
  return "S"

choices = [buyMPQ,buyMul,buyStk]

for i in range(n):
  P = P+M*(Q+(S*streak))
  outputs_random.append(P)
  func = choice(choices)
  choice_random.append(func())
  if len(choice_random) == choice_count:
    choice_random = "_"
    choice_count += 1


inputs = [x+1 for x in range(POINT_COUNT)]

plt.plot(inputs, outputs_streak, 'r--', label = "streak")
plt.plot(inputs, outputs_multiplier, 'bs', label = "multiplier")
plt.plot(inputs, outputs_question, 'g^', label = "perQuestion")
plt.plot(inputs, outputs_cyclical, 'rs', label = "cyclical")
plt.plot(inputs, outputs_random, 'gs', label = "random")
plt.legend(loc="upper left")
plt.ylabel('Simple Test of GimKit')
plt.ylim(0,700)
#plt.xlim(0,0)

print(choice_random)

plt.show()
