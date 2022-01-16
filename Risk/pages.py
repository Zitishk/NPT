from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Risk(Page):
    def is_displayed(self):
        return self.round_number==1
class Risk2(Page):
    form_model = 'player'
    form_fields = ['Risk1','Risk2','Risk3','Risk4','Risk5','Risk6','Risk7','Risk8','Risk9','Risk10']
    def before_next_page(self):
        self.player.set_riskres()
        return

class Riskres(Page):
    def vars_for_template(self):
        Payoff = self.player.participant.vars['pay']
        Round = self.player.participant.vars['round11']
        Decision = self.player.participant.vars['decision11']
        chance = self.participant.vars['chance']
        chance2 = self.participant.vars['chance2']
        small = self.participant.vars['small']
        big = self.participant.vars['big']
        return {'Payoff' : Payoff, 'Round':Round, 'Decision':Decision,'small':small,'big':big,'chance':chance,'chance2':chance2 }

class Survey(Page):
    form_model = 'player'
    def get_form_fields(self):
        q = 'q'
        fields = []
        field = ['gender','caste','relegion','year','income','freeform']
        for i in range(1,21):
            fields.append(q+str(i))
            pass
        return fields + field



class Endresult(Page):
    def vars_for_template(self):
        round = self.player.participant.vars['round']
        earnings = self.player.participant.vars['earnin']
        Payoff = self.player.participant.vars['pay']
        self.player.payoff = Payoff + earnings
        final =  Payoff + earnings
        if(earnings==100):
            decision=False
            name = 'No one'
        elif(earnings==300):
            decision = True
            name = 'No one else'
        else:
            decision= False
            name = 'Someone'
        return {'round' : round,'decision' : decision, 'earnings' : earnings,'name':name,'Payoff':Payoff,'final':final}

class Thank(Page):
    def vars_for_template(self):
        final = int(self.player.payoff[2:])
        money = final*0.2
        return {'fianl':final,'money':money}


page_sequence = [Risk, Risk2, Riskres,Survey, Endresult, Thank]
