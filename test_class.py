#!/usr/bin/env python

class tennis_score(object):
    game = ("0", "15", "30", "40", "Ad")
    def __init__(self, match_type):
        self.p1_game_points = 0
        self.p2_game_points = 0
    	self.p1_set_points = [0, 0, 0, 0, 0]
    	self.p2_set_points = [0, 0, 0, 0, 0]
    	self.p1_set_tally = 0
    	self.p2_set_tally = 0
    	self.current_set = 0
    	self.tie_breaker = False
    	self.p1_name = ""
    	self.p2_name = ""
    	self.serve = 0
    	self.sets = self.sets_to_play(match_type)
    	self.match_type = match_type
    	self.deuce = False
    	self.match_complete = False
    	
    def sets_to_play(self, match_type):
        if match_type==("Male"):
            return 5
        else:
            return 3
        
    def toggle_serve(self):
        self.serve=abs(self.serve - 1)
        
    def update_set_tally(self, player):
        if player == 0:
            self.p1_set_tally +=1
        else:
            self.p2_set_tally +=1

    def check_end_of_game(self, player):
    	if self.deuce == False:
            # Non-deuce game
            if ((self.p1_game_points <= 2) and (self.p2_game_points >= 4)) or ((self.p2_game_points <= 2) and (self.p1_game_points >= 4)):
                if player == 0:
                    self.p1_game_points -=1
                else:
                    self.p2_game_points -=1
                if player==0:
                    self.p1_set_points[self.current_set]+=1
                else:
                    self.p2_set_points[self.current_set]+=1
                #print self.get_set_scores()
                self.toggle_serve()
                self.reset_game_scores()
                return True
    	    else:
    	    	return False
    	else:
            # Deuce game...
            if ((self.p1_game_points > 4) or (self.p2_game_points > 4)):
                if player == 0:
                    self.p1_game_points -=1
                else:
                    self.p2_game_points -=1
                if player==0:
                    self.p1_set_points[self.current_set]+=1
                else:
                    self.p2_set_points[self.current_set]+=1
                #print self.get_set_scores()
                self.toggle_serve()
                self.reset_game_scores()
                return True
            else:
                return False

    def check_end_of_set(self):
	p1_set = self.p1_set_points[self.current_set]
        p2_set = self.p2_set_points[self.current_set]
	#print str(p1_set) + " " + str(p2_set)
        if (((p1_set > 5) and (p2_set < 5)) or ((p2_set > 5) and (p1_set < 5))):
            return True
        elif (((p1_set > 6) and (p2_set == 5)) or ((p2_set > 6) and (p1_set == 5))):
            return True
        elif (p1_set == 6) and (p2_set == 6):
            self.tie_breaker = True
	    self.p1_game_points = 0
	    self.p2_game_points = 0
            return False
        else:
            #print "Not end of set"
            return False
        
    def check_end_of_tie_breaker(self, player):
	p1_game = self.p1_game_points
        p2_game = self.p2_game_points
        if (p1_game > 6) or (p2_game > 6):
            if ((p1_game - p2_game) > 1) or ((p2_game - p1_game) > 1):
		if player==0:
		    self.p1_set_points[self.current_set] +=1
		else:
		    self.p2_set_points[self.current_set] +=1
                return True
            else:
                return False

    def check_is_finished(self):
        if self.sets == 5:
            if (self.p1_set_tally == 3) or (self.p1_set_tally == 3):# or (self.current_set == self.sets):
                #print "Finished"
                self.match_complete = True
                return True
            else:
                return False
        else:
            if (self.p1_set_tally == 2) or (self.p1_set_tally == 2):# or (self.current_set == self.sets):
                #print "Finished"
                self.match_complete = True
                return True
            else:
                return False
        

    def reset_game_scores(self):
        self.p1_game_points = 0
        self.p2_game_points = 0
        self.tie_breaker = False
        self.deuce = False

    def check_is_deuce(self):
        if (((self.p1_game_points-1) >= 3) and (self.p2_game_points >= 3)) or ((self.p1_game_points >= 3) and ((self.p2_game_points-1) >= 3)):
            self.deuce = True
            return True
            
    def get_game_scores(self, player):
        score = {self.p1_name:self.game[self.p1_game_points], self.p2_name:self.game[self.p2_game_points]}
	return score

    def get_set_scores(self):
    	a = self.sets
    	score = {self.p1_name:self.p1_set_points[0:a], self.p2_name:self.p2_set_points[0:a]}
    	return score
     
    def point_scored(self, player):
        #print "Player %s scored a point" % player
        if self.match_complete == False:
            if self.tie_breaker == False:
                if player==0:
                    self.p1_game_points+=1
                    if self.check_is_deuce():
                        if (self.p2_game_points > 3):
                            self.p2_game_points-=1
                            self.p1_game_points-=1
                elif player==1:
                    self.p2_game_points+=1
                    if self.check_is_deuce():
                        if (self.p1_game_points > 3):
                            self.p1_game_points-=1
                            self.p2_game_points-=1

                if not self.check_end_of_game(player):
                    a=self.get_game_scores(player)
                    
                #else:
                if self.check_end_of_set():
                    if not self.check_is_finished():
                        self.current_set +=1
                    else:
                        self.match_complete = True
		    self.update_set_tally(player)
		    self.reset_game_scores()
                #if self.tie_breaker:
                    #if
            else:
                if player==0:
                    self.p1_game_points+=1
                elif player==1:
                    self.p2_game_points+=1
                
                if self.check_end_of_tie_breaker(player):
                    if not self.check_is_finished():
                        self.current_set +=1
                    else:
                        self.match_complete = True
		    self.update_set_tally(player)
		    self.reset_game_scores()
            
                    #print "Score is: %s" % a
                    #return a
    
    
#a=tennis_score("Male")
#a.p1_name="Bob"
#a.p2_name="Albert"
#print "Sets to play: %s" % a.sets_to_play(a.match_type)

#a.point_scored(1) #bob 15
#a.point_scored(1) #bob 30
#a.point_scored(0) #Albert 15
#a.point_scored(0) #Albert 30
#a.point_scored(1) #Bob 40
#a.point_scored(0)
#a.point_scored(0) #Albert 40
#a.point_scored(1) #Bob Adv
#a.point_scored(0) #Deuce
#a.point_scored(1) #Bob Adv
#a.point_scored(1) #Bob Win
#a.point_scored(1)
#a.point_scored(1)
#a.point_scored(1)
