from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Test(Page):
    form_model = 'player'
    form_fields = ['audio']

class Welcome(Page):
    def is_displayed(self):
        return self.round_number==1
class Earnings(Page):
    def is_displayed(self):
        return self.round_number==1
class Overview(Page):
    def is_displayed(self):
        return self.round_number==1
class Instructions(Page):
    def vars_for_template(self):
        mode = self.session.config['mode']
        return { 'mode' : mode}
    def is_displayed(self):
        return self.round_number==1
class Quiz(Page):
    form_model = 'player'
    form_fields = ['Q1','Q2','Q3','Q4','Q5','Q6']
    def error_message(self, values):
        solutions = dict(
            Q1=2,
            Q2=3,
            Q3=3,
            Q4=2,
            Q5=1,
            Q6=2
        )
        error_messages = dict()
        for fieldn in solutions:
            if(values[fieldn]!=solutions[fieldn]):
                error_messages[fieldn] = 'Wrong answer, please select the correct answer to proceed'
        return error_messages
class Gender(Page):
    form_model='player'
    def get_form_fields(self):
        if(self.session.config['mode']==1):
            return ['age','gender']
        else:
            return ['age','gender','first_name','last_name']

    def before_next_page(self):
        if(self.session.config['mode']!=1):
            self.player.set_name_2()

class Name(Page):
    form_model = 'player'
    form_fields = ['name']

    def before_next_page(self):
        if(self.session.config['mode']==1):
            self.player.set_name_1()
    def is_displayed(self):
        return self.session.config['mode']==1

page_sequence = [Test,Gender,Name,Welcome,Earnings,Overview,Instructions,Quiz]
