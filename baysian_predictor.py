#!/usr/bin/python3.5
#the selected coin. The function pheads may be called and any time and will 
#return your best estimate of the next flip landing on heads.

#based on baysian predictor, we have a list of coins, defining probability of head for each coin and we choose one coin out of it and flip multiple times,
#we need to predict next probability of head given sequence that already occurs, like "HHTTT", what we update self.prob is figure out the probability of
#P[coin x | "HHTT" or any sequence occurs] by using baysian formula(this is how we compute the posterior probability)
from __future__ import division
class FlipPredictor(object):
    def __init__(self,coins):
        self.coins=coins
        n=len(coins)
        self.probs=[1/n]*n
    def pheads(self):
        #Write a function that returns 
        #the probability of the next flip being heads 
        return sum([self.probs[i]*self.coins[i] for i in range(len(self.coins))])

    def update(self,result):
        #Write a function the updates
        #the probabilities of flipping each coin
        sum_prob, prob_coins = 0, self.coins
        if result == "T":
            prob_coins = [1-x for x in self.coins]
        for i in range(len(self.coins)):
            sum_prob += prob_coins[i] * self.probs[i]
        for i in range(len(self.coins)):
            self.probs[i] = (self.probs[i] * prob_coins[i]) / sum_prob

#The code below this line tests your implementation. 
#You need not change it
#You may add additional test cases or otherwise modify if desired
def test(coins,flips):        
    f=FlipPredictor(coins)
    guesses=[]
    for flip in flips:
        f.update(flip)
        guesses.append(f.pheads())
    return guesses   
        
def maxdiff(l1,l2):
    return max([abs(x-y) for x,y in zip(l1,l2)])

testcases=[
(([0.5,0.4,0.3],'HHTH'),[0.4166666666666667, 0.432, 0.42183098591549295, 0.43639398998330553]),
(([0.14,0.32,0.42,0.81,0.21],'HHHTTTHHH'),[0.5255789473684211, 0.6512136991788505, 0.7295055220497553, 0.6187139453483192, 0.4823974597714815, 0.3895729901052968, 0.46081730193074644, 0.5444108434105802, 0.6297110187222278]),
(([0.14,0.32,0.42,0.81,0.21],'TTTHHHHHH'),[0.2907741935483871, 0.25157009005730924, 0.23136284577678012, 0.2766575695593804, 0.3296000585271367, 0.38957299010529806, 0.4608173019307465, 0.5444108434105804, 0.6297110187222278]),
(([0.12,0.45,0.23,0.99,0.35,0.36],'THHTHTTH'),[0.28514285714285714, 0.3378256513026052, 0.380956725493104, 0.3518717367468537, 0.37500429586037076, 0.36528605387582497, 0.3555106542906013, 0.37479179323540324]),
(([0.03,0.32,0.59,0.53,0.55,0.42,0.65],'HHTHTTHTHHT'),[0.528705501618123, 0.5522060353798126, 0.5337142767315369, 0.5521920592821695, 0.5348391689038525, 0.5152373451083692, 0.535385450497415, 0.5168208803156963, 0.5357708613431963, 0.5510509656933194, 0.536055356823069])]

for inputs,output in testcases:
    if maxdiff(test(*inputs),output)<0.001:
        print 'Correct'
    else: print 'Incorrect'
