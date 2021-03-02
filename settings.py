from os import environ

SESSION_CONFIGS = [
    dict(
       name='A1',
       display_name="A1",
       num_demo_participants=3,
       app_sequence=['Preexperiment'],
    ),
    dict(
       name='A2',
       display_name="A2",
       num_demo_participants=3,
       app_sequence=['Preexperiment'],
    ),
    dict(
       name='A3',
       display_name="A3",
       num_demo_participants=3,
       app_sequence=['Preexperiment'],
    ),
    dict(
       name='C0',
       display_name="C0",
       num_demo_participants=3,
       app_sequence=['Preexperiment'],
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=1.23, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '5pug1m_y2pz7#&0dr(s@k*#whs8=3@#cfyzj%in%n6k1woe_m-'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
