from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import time
import random

author = 'Priyoma Mustafi'

doc = """
Non Promotable Tasks treatment
"""

class Constants(BaseConstants):
    name_in_url = 'NPT'
    players_per_group = 3
    num_rounds = 10

    minTime = 3

    matrix = {
        12: {
            1: [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]],
            2: [[2, 8, 9], [10, 1, 5], [7, 11, 4], [6, 12, 3]],
            3: [[6, 10, 4], [3, 11, 2], [1, 9, 7], [5, 8, 12]],
            4: [[6, 5, 11], [2, 10, 7], [12, 9, 4], [8, 1, 3]],
            5: [[2, 3, 9], [10, 12, 6], [8, 7, 11], [5, 1, 4]],
            6: [[11, 4, 6], [3, 12, 7], [10, 2, 5], [8, 9, 1]],
            7: [[10, 3, 1], [11, 12, 5], [7, 9, 4], [6, 8, 2]],
            8: [[10, 8, 9], [2, 1, 5], [7, 11, 6], [4, 12, 3]],
            9: [[6, 10, 4], [3, 11, 2], [1, 9, 7], [5, 8, 12]],
            10: [[6, 5, 11], [2, 10, 7], [12, 9, 4], [8, 1, 3]]
        },
        15: {
            1: [[15, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14]],
            2: [[7, 12, 3], [6, 5, 10], [1, 4, 14], [15, 13, 9], [8, 11, 2]],
            3: [[9, 12, 4], [7, 15, 10], [8, 14, 3], [6, 13, 2], [1, 11, 5]],
            4: [[12, 15, 11], [8, 5, 13], [6, 9, 14], [4, 2, 7], [3, 1, 10]],
            5: [[12, 8, 10], [11, 6, 4], [15, 14, 5], [2, 9, 3], [13, 1, 7]],
            6: [[4, 10, 13], [5, 2, 12], [3, 15, 6], [9, 8, 1], [14, 11, 7]],
            7: [[15, 8, 4], [7, 5, 9], [12, 1, 6], [13, 11, 3], [14, 10, 2]],
            8: [[15, 14, 5], [9, 12, 8], [3, 1, 7], [6, 11, 10], [2, 13, 4]],
            9: [[1, 9, 4], [8, 10, 5], [11, 3, 12], [6, 13, 15], [2, 14, 7]],
            10: [[12, 10, 1], [15, 8, 4], [11, 5, 2], [9, 13, 7], [3, 14, 6]],
        },
        18: {
            1: [[18, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14], [15, 16, 17]],
            2: [[10, 14, 5], [17, 13, 1], [18, 12, 4], [6, 9, 3], [11, 7, 15], [2, 16, 8]],
            3: [[15, 9, 1], [3, 2, 11], [13, 10, 4], [5, 17, 7], [16, 6, 12], [18, 14, 8]],
            4: [[15, 18, 5], [8, 3, 17], [4, 14, 2], [9, 13, 16], [6, 11, 1], [12, 7, 10]],
            5: [[5, 6, 13], [18, 3, 7], [9, 12, 8], [15, 10, 2], [16, 4, 1], [17, 14, 11]],
            6: [[14, 15, 6], [12, 5, 1], [4, 8, 11], [17, 18, 9], [16, 3, 10], [2, 7, 13]],
            7: [[10, 18, 6], [12, 17, 2], [16, 11, 5], [8, 13, 15], [1, 14, 3], [9, 7, 4]],
            8: [[18, 11, 13], [16, 14, 7], [8, 10, 1], [15, 12, 3], [6, 17, 4], [2, 9, 5]],
            9: [[13, 17, 10], [3, 9, 16], [18, 8, 15], [1, 14, 5], [4, 2, 11], [6, 7, 12]],
            10: [[7, 17, 11], [18, 13, 4], [16, 10, 5], [2, 15, 3], [12, 1, 8], [6, 9, 14]]
        },
        21: {
            1: [[21, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14], [15, 16, 17], [18, 19, 20]],
            2: [[5, 19, 15], [10, 7, 18], [11, 1, 14], [13, 17, 4], [21, 9, 16], [12, 2, 6], [8, 20, 3]],
            3: [[5, 21, 8], [12, 11, 7], [13, 9, 2], [14, 16, 3], [6, 4, 20], [15, 1, 18], [17, 10, 19]],
            4: [[14, 6, 5], [12, 21, 20], [15, 8, 4], [17, 1, 9], [7, 19, 3], [2, 16, 10], [11, 18, 13]],
            5: [[10, 4, 21], [7, 16, 5], [11, 3, 2], [13, 19, 6], [20, 9, 15], [1, 8, 12], [17, 14, 18]],
            6: [[20, 16, 13], [3, 15, 21], [5, 2, 18], [10, 6, 1], [8, 17, 11], [19, 4, 12], [14, 9, 7]],
            7: [[6, 17, 3], [9, 18, 4], [7, 21, 13], [12, 10, 15], [2, 8, 14], [19, 1, 16], [5, 20, 11]],
            8: [[9, 8, 19], [15, 7, 2], [4, 16, 11], [18, 6, 21], [14, 20, 10], [12, 5, 17], [1, 13, 3]],
            9: [[2, 20, 17], [18, 16, 8], [19, 21, 14], [4, 7, 1], [10, 5, 13], [6, 11, 15], [9, 3, 12]],
            10: [[9, 14, 5], [7, 3, 20], [13, 18, 10], [19, 1, 17], [6, 2, 8], [15, 4, 12], [21, 16, 11]],
        },
        24: {
            1: [[24, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14], [15, 16, 17], [18, 19, 20], [21, 22, 23]],
            2: [[14, 7, 24], [22, 1, 10], [8, 23, 19], [5, 2, 12], [9, 3, 18], [16, 13, 11], [15, 4, 6], [21, 20, 17]],
            3: [[9, 17, 22], [5, 7, 15], [8, 12, 18], [2, 10, 4], [23, 11, 6], [3, 14, 19], [16, 21, 1], [20, 13, 24]],
            4: [[3, 10, 12], [6, 5, 13], [20, 9, 4], [7, 19, 16], [21, 14, 15], [22, 24, 11], [8, 1, 17], [2, 23, 18]],
            5: [[18, 5, 24], [9, 19, 6], [14, 17, 11], [3, 2, 21], [4, 1, 12], [23, 16, 10], [22, 7, 20], [13, 15, 8]],
            6: [[4, 19, 17], [13, 2, 9], [5, 8, 16], [21, 12, 7], [15, 24, 10], [1, 14, 23], [11, 20, 3], [22, 6, 18]],
            7: [[21, 18, 13], [12, 20, 16], [19, 15, 2], [3, 7, 23], [1, 11, 5], [9, 24, 8], [10, 17, 6], [4, 14, 22]],
            8: [[4, 23, 13], [16, 14, 9], [7, 1, 18], [22, 19, 5], [12, 11, 15], [21, 8, 10], [24, 17, 3], [2, 20, 6]],
            9: [[24, 6, 21], [17, 23, 12], [18, 4, 16], [3, 8, 22], [1, 9, 15], [10, 13, 19], [5, 14, 20], [7, 2, 11]],
            10: [[7, 17, 13], [10, 14, 18], [15, 23, 20], [6, 1, 3], [5, 9, 21], [16, 2, 22], [12, 24, 19], [11, 4, 8]],
        },
        27: {
            1: [[27, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14], [15, 16, 17], [18, 19, 20], [21, 22, 23],
             [24, 25, 26]],
            2: [[7, 1, 3], [15, 9, 14], [12, 4, 19], [11, 18, 5], [16, 20, 26], [21, 24, 10], [2, 22, 8], [13, 25, 23], [
                17, 6, 27]],
            3: [[23, 3, 27], [15, 13, 10], [22, 4, 16], [19, 11, 17], [6, 21, 26], [8, 14, 20], [7, 5, 24], [9, 25, 1], [18,
                                                                                                                     12,
                                                                                                                     2]],
            4: [[23, 17, 26], [5, 1, 8], [3, 16, 2], [27, 7, 14], [20, 9, 6], [12, 22, 25], [15, 19, 21], [24, 11, 13], [4,
                                                                                                                     18,
                                                                                                                     10]],
            5: [[20, 4, 21], [1, 12, 26], [15, 6, 18], [10, 25, 17], [19, 23, 2], [13, 8, 3], [14, 22, 5], [9, 24, 27], [7,
                                                                                                                     11,
                                                                                                                     16]],
            6: [[21, 18, 27], [25, 6, 3], [22, 9, 7], [11, 14, 26], [5, 12, 10], [1, 20, 23], [19, 13, 16], [17, 2, 24], [8,
                                                                                                                      15,
                                                                                                                      4]],
            7: [[13, 18, 9], [16, 10, 6], [4, 26, 7], [21, 1, 11], [12, 17, 8], [5, 19, 27], [25, 2, 14], [15, 23, 24], [22,
                                                                                                                     3,
                                                                                                                     20]],
            8: [[25, 27, 16], [26, 3, 15], [11, 6, 2], [8, 18, 23], [17, 1, 22], [5, 13, 20], [9, 21, 12], [19, 10, 7], [4,
                                                                                                                     24,
                                                                                                                     14]],
            9: [[4, 27, 13], [12, 20, 11], [16, 18, 14], [26, 10, 22], [17, 9, 3], [24, 19, 1], [7, 15, 2], [21, 8, 25], [5,
                                                                                                                      23,
                                                                                                                      6]],
            10: [[7, 23, 12], [2, 13, 26], [14, 10, 1], [16, 8, 9], [22, 19, 6], [17, 21, 5], [25, 4, 11], [24, 3, 18], [20,
                                                                                                                     27,
                                                                                                                     15]],
        },
    }

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.session.num_participants > 9:
            self.set_group_matrix(Constants.matrix[self.session.num_participants][self.round_number])
        else:
            self.group_randomly()
        print(self.get_group_matrix())
        for player in self.get_players():
            if self.round_number == 1:
                player.participant.vars['NPTPay'] = 0
            else:
                pass
    def startTime(self):
        for player in self.get_players():
            player.startTime = time.time_ns() ##getting the time in nano-seconds
        for group in self.get_groups():
            group.set_time()

class Group(BaseGroup):
    investCheck = models.BooleanField(initial=False)

    def live_leave(self, id_in_group, data):
        print('invested', data, 'person who invest was', id_in_group)
        self.get_player_by_id(id_in_group).invest = True

        if data == 1:
            response = dict(type='round_finished')
            return {0: response}

    noInvest = models.BooleanField(initial=False)
    diffTime = models.FloatField()
    diffStartTime = models.FloatField()
    diff1 = models.FloatField()
    diff2 = models.FloatField()
    diff3 = models.FloatField()
    #Var to set timeing for indiv rounds
    round_time_limit = models.IntegerField()

    def checkTime(self):
        p1 = self.get_player_by_id(1)
        p1.amountTime = (p1.leaveTime - p1.startTime) / 1000000000 - 3
        p2 = self.get_player_by_id(2)
        p2.amountTime = (p2.leaveTime - p2.startTime) / 1000000000 - 3
        p3 = self.get_player_by_id(3)
        p3.amountTime = (p3.leaveTime - p3.startTime) / 1000000000 - 3

        print('time on page client/server:',"p1", p1.amountTime, p1.javaTime, 'p2', p2.amountTime, p2.javaTime, 'p3', p3.amountTime, p3.javaTime)

        difference = abs(p1.amountTime - p2.amountTime)
        diff2 = abs(p1.amountTime - p3.amountTime)
        diff3 = abs(p2.amountTime - p3.amountTime)
        self.diff1 = difference
        self.diff2 = diff2
        self.diff3 = diff3
        self.diffTime = (diff3 + diff2 + difference) / 3
        print('differences in server time', difference, diff2, diff3, self.diffTime)

        otherdiff = abs(p1.startTime - p2.startTime) / 1000000000
        otherdiff2 = abs(p1.startTime - p3.startTime) / 1000000000
        otherdiff3 = abs(p3.startTime - p2.startTime) / 1000000000
        self.diffStartTime = (otherdiff + otherdiff2 + otherdiff3) / 3

    def investPay(self):
        if not self.investCheck:
            invest = [p.invest for p in self.get_players()]
            print('invest',invest)
            if max(invest) == 1:
                print('someone invested')
                self.noInvest = False
            else:
                print('no one invested')
                self.noInvest = True

            if not self.noInvest:
                print('who gets paid for investing')
                players = sorted(self.get_players(), key=lambda p: [-p.invest, p.pressTime, random.random()])
                for (i, p) in enumerate(players, start=1):
                    p.investsPay = i
                for p in self.get_players():
                    if p.investsPay == 1:
                        p.earnings = int(self.session.config['payoff_volunteer'])
                    else:
                        p.earnings = int(self.session.config['payoff_other_volunteer'])
                    p.participant.vars['NPTPay'] = p.participant.vars['NPTPay'] + p.earnings
            else:
                print('no one invested')
                for p in self.get_players():
                    p.earnings = int(self.session.config['payoff_novolunteer'])
                    p.participant.vars['NPTPay'] = p.participant.vars['NPTPay'] + p.earnings
            self.investCheck = True
        else:
            pass
    def set_time(self):
        self.round_time_limit = int(random.uniform(45,90))
        return

    def set_money(self):
        for p in self.get_players():
            f_round = random.randint(1,10)
            p.participant.vars['round']  = f_round
            p.participant.vars['earnin'] = p.in_round(f_round).earnings

class Player(BasePlayer):
    startTime = models.FloatField()
    leaveTime = models.FloatField()
    amountTime = models.FloatField()

    invest = models.BooleanField(initial=False, blank=True)
    investsPay = models.IntegerField()

    earnings = models.IntegerField()

    javaTime = models.FloatField()
    pressTime = models.FloatField(initial=0, blank=True)
