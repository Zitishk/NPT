from os import environ

SESSION_CONFIGS = [
     dict(
        name='button',
        display_name="Non-promotable Tasks",
        num_demo_participants=3,
        app_sequence=['javatest','general','NPT','Risk'],
        use_browser_bots=False,
        time=60,
        payoff_novolunteer=100,
        payoff_volunteer=300,
        payoff_other_volunteer=900,
        mode = 1,
     ),
     dict(
        name='Positive',
        display_name="Positive SR",
        num_demo_participants=3,
        app_sequence=['javatest','general','NPT','Risk'],
        use_browser_bots=False,
        time=60,
        payoff_novolunteer=100,
        payoff_volunteer=300,
        payoff_other_volunteer=900,
        mode = 2,
     ),
     dict(
        name='Negative',
        display_name="Negative SR",
        num_demo_participants=3,
        app_sequence=['javatest','general','NPT','Risk'],
        use_browser_bots=False,
        time=60,
        payoff_novolunteer=100,
        payoff_volunteer=300,
        payoff_other_volunteer=900,
        mode = 3,
     ),
     dict(
        name='PosNeg',
        display_name="PosNeg SR",
        num_demo_participants=3,
        app_sequence=['javatest','general','NPT','Risk'],
        use_browser_bots=False,
        time=60,
        payoff_novolunteer=100,
        payoff_volunteer=300,
        payoff_other_volunteer=900,
        mode = 4,
     ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=250, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'NOK'
USE_POINTS = False

ROOMS = [
    dict(
        name='experiment',
        display_name='NHH_Study',
        participant_label_file='participant_label.txt'
    ),
]


ADMIN_USERNAME = 'marissaOTree'
# for security, best to set admin password in an environment variable
DEBUG = (environ.get('OTREE_PRODUCTION') in {None, '', '0'})
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '947$_)06bnbxakn$e2!u!zq=o2=1!8y!da)wqy4yq9d9ca!sof'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
