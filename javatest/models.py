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
import math

author = 'Marissa Lepper'

doc = """
Test of javascript
"""


class Constants(BaseConstants):
    name_in_url = 'javatest'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.randCode =math.floor(10000*random.random())
            p.javaAnswer = 10000*math.floor(10*random.random()) + 1000*math.floor(10*random.random()) + 100*math.floor(10*random.random()) + 10*math.floor(10*random.random()) + math.floor(10*random.random())


class Group(BaseGroup):
    def live_answer(self,  id_in_group, answer):
        if answer.get('pageLoad'):
            secret = self.get_player_by_id(id_in_group).javaAnswer

            broadcast = {'secret': secret}
            return {id_in_group: broadcast}
        elif not answer.get('pageLoad'):
            secret = self.get_player_by_id(id_in_group).javaAnswer
            broadcast = {'secret': secret}
            return {id_in_group: broadcast}


class Player(BasePlayer):
    randCode = models.IntegerField()
    javaTest = models.IntegerField()
    javaAnswer = models.IntegerField()

    ping = models.IntegerField(label="Ping:")
    download = models.FloatField(label="Download Speed:")
    upload = models.FloatField(label="Upload Speed")


    pledge1 = models.BooleanField(initial=None, widget=widgets.CheckboxInput,
                                  label="Be available for the full time of the experiment"
                                  )
    pledge2 = models.BooleanField(initial=None, widget=widgets.CheckboxInput,
                                  label="Devote my full attention to the experiment and not engage in other activities, such as browsing the internet"
                                  )
    pledge3 = models.BooleanField(initial=None, widget=widgets.CheckboxInput,
                                  label="Put my mobile devices in silent mode and not use them during the experiment"
                                  )
    pledge4 = models.BooleanField(initial=None, widget=widgets.CheckboxInput,
                                  label="Not communicate with any other participants during the session")
    pledge5 = models.BooleanField(initial=None, widget=widgets.CheckboxInput, label="I checked my internet speed and" " have a ping speed under 100")


    def javaTest_error_message(self, value):
        print('value is', value)
        if value != self.javaAnswer:
            return 'Please send the researcher a message if you cannot see the code.'
