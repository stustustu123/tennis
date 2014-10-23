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
    	
    def reset_match(self):
        self.reset_game_scores()
        self.p1_set_tally = 0
        self.p2_set_tally = 0
        self.current_set = 0
        self.p1_set_points = [0, 0, 0, 0, 0]
        self.p2_set_points = [0, 0, 0, 0, 0]
        self.tie_breaker = False

    def reset_game_scores(self):
        print "resetting game scores"
        self.p1_game_points = 0
        self.p2_game_points = 0
#        self.tie_breaker = False
        self.deuce = False

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
                self.toggle_serve()
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
                self.toggle_serve()
                return True
            else:
                return False

    def check_end_of_set(self):
        p1_set = self.p1_set_points[self.current_set]
        p2_set = self.p2_set_points[self.current_set]
        if (((p1_set > 5) and (p2_set < 5)) or ((p2_set > 5) and (p1_set < 5))):
            return True
        elif (((p1_set > 6) and (p2_set == 5)) or ((p2_set > 6) and (p1_set == 5))):
            return True
        elif (p1_set == 6) and (p2_set == 6):
            print "p1_set and p2_set == 6"
            self.tie_breaker = True
            self.p1_game_points = 0
            self.p2_game_points = 0
            return False
        else:
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
            if (self.p1_set_tally == 3) or (self.p1_set_tally == 3):
                self.match_complete = True
                return True
            else:
                return False
        else:
            if (self.p1_set_tally == 2) or (self.p1_set_tally == 2):
                self.match_complete = True
                return True
            else:
                return False
            
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
                if self.check_end_of_game(player):
                    if self.check_end_of_set():
                        self.update_set_tally(player)
                        if self.check_is_finished():
                            self.match_complete = True
                        else:
                            self.current_set +=1
                    self.reset_game_scores()
            else:
                if player==0:
                    self.p1_game_points+=1
                elif player==1:
                    self.p2_game_points+=1
                if self.check_end_of_tie_breaker(player):
                    print "End of tie"
                    self.update_set_tally(player)
                    if self.check_is_finished():
                        self.match_complete = True
                    else:
                        self.current_set +=1

                    self.reset_game_scores()
                    self.tie_breaker = False
                
    