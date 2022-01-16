from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = 'player'
    form_fields = ['javaTest']

    live_method = 'live_answer'

    def vars_for_template(self):
        randomID = self.player.randCode
        return {'randomID':randomID,}


class Pledge(Page):
    form_model = 'player'
    form_fields = ['pledge1', 'pledge2', 'pledge3', 'pledge4', 'pledge5']


class Speed(Page):
    form_model = 'player'
    form_fields = ['ping', 'download', 'upload']


page_sequence = [MyPage, Speed]
