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

import random
author = 'Your name here'

doc = """
Your app description
"""

def make_field():
    return models.IntegerField(
        choices=[[1,'Option A'],[0,'Option B']],
        widget=widgets.RadioSelect,
    )
def make_field2(label):
    return models.IntegerField(
        label = label,
        choices=[1,2,3,4,5],
        widget=widgets.RadioSelectHorizontal,
    )
class Constants(BaseConstants):
    name_in_url = 'Risk'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Risk1 = make_field()
    Risk2 = make_field()
    Risk3 = make_field()
    Risk4 = make_field()
    Risk5 = make_field()
    Risk6 = make_field()
    Risk7 = make_field()
    Risk8 = make_field()
    Risk9 = make_field()
    Risk10 = make_field()

    q1 = make_field2('If you win a prize for the best all round performance in your university, how likely are you to inform your friends about it? ')
    q2 = make_field2('If you win a prize for the best all round performance in your university, how likely are you to inform your family about it? ')
    q3 = make_field2('If you win a prize for the best all round performance in your university, how likely are you to post on Facebook or other social media about it ')
    q4 = make_field2('How stressed did the time make you feel during the decision task? ')
    q5 = make_field2('How do you see yourself: are you generally a person who is fully prepared to take risks or do you try to avoid taking risks? ')
    q6 = make_field2('How likely are you to admit that your tastes are different from those of your friends? ')
    q7 = make_field2('How likely are you to argue with a friend about an issue on which he or she has a very different opinion? ')
    q8 = make_field2('How likely are you to defend an unpopular issue that you believe in at a social occasion? ')
    q9 = make_field2('People should be willing to help others who are less fortunate ')
    q10 = make_field2('These days people need to look after themselves and not overly worry about others. ')
    q11 = make_field2('It is important to help one another so that the community in general is a better place. ')
    q12 = make_field2('I see myself as someone who tends to find fault with others ')
    q13 = make_field2('I see myself as someone who can be cold and aloof ')
    q14 = make_field2('I see myself as someone who is considerate and kind to almost everyone ')
    q15 = make_field2('I see myself as someone who likes to cooperate with others ')
    q16 = make_field2('I see myself as someone who is sometimes rude to others ')
    q17 = make_field2('I see myself as someone who is helpful and unselfish with others ')
    q18 = make_field2('I see myself as someone who starts quarrels with others ')
    q19 = make_field2('I see myself as someone who has a forgiving nature ')
    q20 = make_field2('I see myself as someone who is generally trusting ')

    gender = models.StringField(label="Gender",choices = ['Male','Female'],widget=widgets.RadioSelect)
    caste = models.StringField(label = "Caste", choices = ['General','Scheduled Caste','Scheduled Tribe','OBC','Prefer not to say'],widget=widgets.RadioSelect)
    relegion = models.StringField(label = "Relegion", choices = ['Hindu','Muslim','Christian','Prefer not to say'],widget=widgets.RadioSelect)
    year = models.StringField(label = "Which year in college are you ?", choices = ['UG First Year','UG Second Year','UG Third Year','UG Fourth Year','Masters First Year','Masters Second Year'],widget=widgets.RadioSelect)
    income = models.IntegerField(label = "What is your approximate monthly family income in Rupees? ")
    freeform = models.StringField(label ="We are interested in the reasons why you did or did not choose to invest in this study. Please explain what affected your decisions." )

    def set_riskres(self):
        i = random.randint(1,10)
        k = [self.Risk1,self.Risk2,self.Risk3,self.Risk4,self.Risk5,self.Risk6,self.Risk7,self.Risk8,self.Risk9,self.Risk10]
        if(k[i]==1):
            pay = random.choices([200,160],weights=[i/10,(10-i)/10],k=1)
            self.participant.vars['small'] = 160
            self.participant.vars['big'] = 200
        else:
            pay = random.choices([385,10],weights=[i/10,(10-i)/10],k=1)
            self.participant.vars['small'] = 10
            self.participant.vars['big'] = 385
        self.participant.vars['pay'] = pay[0]
        self.participant.vars['round11'] = i
        self.participant.vars['chance'] = (10-i)*10
        self.participant.vars['chance2'] = i*10
        self.participant.vars['decision11'] = k[i]
        return
