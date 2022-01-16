from otree.api import Currency as c, currency_range, Submission
from . import pages
from ._builtin import Bot
from .models import Constants

def call_live_method(method, **kwargs):
    method(1, 0)
    method(2, 0)
    method(3, 0)
    method(1, 0)
    method(1, 0)
    method(2, 0)
    retval= method(3, 1)

class PlayerBot(Bot):
    def play_round(self):
        if self.player.id_in_group <3:
            yield Submission(pages.Round, dict(javaTime=1), timeout_happened=True)
        else:
            yield pages.Round
        yield pages.Results
        if self.round_number == 3:
            yield pages.Task1End
