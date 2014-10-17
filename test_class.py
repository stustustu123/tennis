#!/usr/bin/env python

class tennis_score(object):
    game = ("0", "15", "30", "40", "Ad")
    def __init__(self, match_type):
	self.p1_game_points = 0
	self.p2_game_points = 0
	self.p1_set_points = [0, 0, 0, 0, 0]
	self.p2_set_points = [0, 0, 0, 0, 0]
	self.current_set = 0
	self.tie_breaker = 0
	self.p1_name = "Albert"
	self.p2_name = "Bob"
	self.sets = self.sets_to_play(match_type)
	self.match_type = match_type
	self.deuce = False
        
    def sets_to_play(self, match_type):
        if match_type==("Male"):
            return 5
        else:
            return 3

    def check_end_of_game(self):
	if self.deuce == False:
	    if ((self.p1_game_points <= 2) and (self.p2_game_points >= 4)) or ((self.p2_game_points <= 2) and (self.p1_game_points >= 4)):
		return True
	    else:
		return False
	else:
	    if ((self.p1_game_points > 4) or (self.p2_game_points > 4)):
		print "End of game"
		return True
	    else:
		return False
	    
    def check_is_deuce(self):
	#if player == 0:
	if (((self.p1_game_points) >= 3) and (self.p2_game_points >= 3)):
	    print "Deuce"
	    self.deuce = True
	    return True
	#else:
	    #if (((self.p2_game_points) >= 3) and (self.p1_game_points >= 3)):
		#print "Deuce"
		#self.deuce = True
		#return True
	    
    def get_game_scores(self, player):
	if player == 0:
	    score = {self.p1_name:self.game[self.p1_game_points], self.p2_name:self.game[self.p2_game_points]}
	else:
	    score = {self.p1_name:self.game[self.p1_game_points], self.p2_name:self.game[self.p2_game_points]}
	return score

    def get_set_scores(self):
	a = self.sets
	score = {self.p1_name:self.p1_set_points[0:a], self.p2_name:self.p2_set_points[0:a]}
	return score
 
    def point_scored(self, player):
	
	if self.check_end_of_game():
	    if player==0:
		self.p1_set_points[self.current_set]+=1
	    else:
		self.p2_set_points[self.current_set]+=1
	    print self.get_set_scores()
	    self.p1_game_points = 0
	    self.p2_game_points = 0
	    self.deuce = False
	    self.current_set+=1
	else:
	    if player==0:
		if self.check_is_deuce() and (self.p1_game_points > 4):
		    self.p2_game_points-=1
		self.p1_game_points+=1
	    elif player==1:
		if self.check_is_deuce() and (self.p2_game_points > 4):
		    self.p1_game_points-=1
		self.p2_game_points+=1
	    a=self.get_game_scores(player)
	    print a
        #return a
    
    
a=tennis_score("Male")
print a.sets_to_play(a.match_type)
a.point_scored(1) #bob 15
a.point_scored(1) #bob 30
a.point_scored(0) #Albert 15
a.point_scored(0) #Albert 30
a.point_scored(1) #Bob 40
a.point_scored(0) #Albert 40
a.point_scored(1) #Bob Adv
a.point_scored(0) #Deuce
a.point_scored(1) #Bob Adv
a.point_scored(1) #Bob Win
#print a.get_set_scores()
