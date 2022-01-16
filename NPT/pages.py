from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time


class Round(Page):
    live_method = 'live_leave'

    def get_timeout_seconds(self):
        return self.group.round_time_limit + Constants.minTime + 5

    timer_text = 'Remaining Time:'

    form_model = 'player'
    form_fields = ['invest','javaTime', 'pressTime']

    def vars_for_template(self):
        time = self.group.round_time_limit + Constants.minTime
        novolunteer = self.session.config['payoff_novolunteer']
        volunteer = self.session.config['payoff_volunteer']
        other_volunteer = self.session.config['payoff_other_volunteer']
        minTime = 1000 * Constants.minTime

        return {'time': time,
                'volunteer': volunteer, 'other_volunteer': other_volunteer, 'novolunteer': novolunteer,
                'minTime': minTime}

    def before_next_page(self):
        self.player.leaveTime = time.time_ns()
        if(self.round_number==10):
            self.group.set_money()


class MyWaitPage(WaitPage):
    wait_for_all_groups = True
    body_text = "Please wait for the experiment to continue."
    after_all_players_arrive = 'startTime'

class ShortWaitPage(WaitPage):
    body_text = "Please wait while your earnings are calculated"
    after_all_players_arrive = 'investPay'


class Results(Page):
    def vars_for_template(self):
        invest = self.player.investsPay == 1
        group = self.group.noInvest < 1
        earnings = self.player.earnings
        name = 'No one'
        for p in self.group.get_players():
            if(p.earnings==int(self.session.config['payoff_volunteer'])):
                name = p.participant.vars['name']
        mode = self.session.config['mode']
        names = []
        for p in self.group.get_players():
            if(p.earnings!=int(self.session.config['payoff_volunteer'])):
                names.append(p.participant.vars['name'])
        return {'invest':invest, 'group':group,'earning':earnings,'name':name,'mode':mode,'name1':names[0],'name2':names[1]}

    def before_next_page(self):
        self.group.checkTime()
        return

class Task1End(WaitPage):
    body_text = 'This completes Task A. Please wait for instructions for Task B.'
    wait_for_all_groups = True

    def is_displayed(self):
        return self.round_number == Constants.num_rounds



class Begin(Page):
    def vars_for_template(self):
        yes = 0
        if(self.round_number==5):
            yes=1
        return { 'yes': yes }
    def is_displayed(self):
        return (self.round_number == 1 or self.round_number == 5)

page_sequence = [Begin, MyWaitPage, Round, ShortWaitPage, Results]
