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

mturk_hit_settings = dict(
    keywords='bonus, study, training',
    title='Experimental study on decision-making (approx. 45 minutes; $8 compensation on average)',
    description='This HIT is a three-part study in which you play a lottery, receive a training as well as work on tasks concerning decision-making and then answer some personal questions. Requirements: Web browser must support the playback of videos and the concept of Net Present Value must be known (eligibility checks to both at the beginning); Mobile devices not allowed',
    frame_height=500,
    template='global/mturk_template.html',
    minutes_allotted_per_assignment=120,
    expiration_hours=7 * 24,
    qualification_requirements=[
   {
        'QualificationTypeId': "00000000000000000071",
        'Comparator': "EqualTo",
        'LocaleValues': [{'Country': "US"}]
    },
    {
        'QualificationTypeId': "3GNL8ZDCGCK9VB6Q1AXGLO7B64OOI5",
        'Comparator': "DoesNotExist",
    },
            { # Worker_​NumberHITsApproved
            'QualificationTypeId': "00000000000000000040",
            'Comparator': "GreaterThan",
            'IntegerValues': [100]
            },
   	{ # Worker_​NumberHITsApproved
            'QualificationTypeId': "000000000000000000L0",
            'Comparator': "GreaterThan",
            'IntegerValues': [95]
        },
   
    ],
    grant_qualification_id='3GNL8ZDCGCK9VB6Q1AXGLO7B64OOI5', # to prevent retakes
)

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=1.23, doc="", mturk_hit_settings=mturk_hit_settings
)

# setting for integration with AWS Mturk
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')

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
