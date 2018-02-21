import HW4Game as pro

TAIL_PROBS = 1-0.4 # These are constant, using capital to represent
FILP_TIMES = 20
REPEAT_SIZE = 1000
WIN_MON = 100
START_MON = 250

#mygame = pro.Game(id=1, tail_prob=TAIL_PROBS)
#print (mygame.simulate(n_flip_times=FILP_TIMES, win_mon= WIN_MON, start_mon= START_MON))
#print(mygame.get_reward())

# create a cohort
myRepeatgame= pro.repeatation(repeat_size=REPEAT_SIZE, tail_prob= TAIL_PROBS)
# simulate the patient
myRepeatgame.simulate(n_flip_times=FILP_TIMES, win_mon= WIN_MON, start_mon= START_MON)

# print the patient survival time
print(myRepeatgame.get_ave_reward())
