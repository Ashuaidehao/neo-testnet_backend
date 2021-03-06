import os
from datetime import timedelta
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(os.path.realpath(__file__))
ENV = os.getenv("NEO_WISH_ENV")

# neo3 cli rpc address
FAUCET_CLI = 'http://127.0.0.1:30332'
CAPTCHA_SECRET = "6LfNuZkUAAAAAAg4Hy1EqXto5U7O1wBII8ZajAzd" 

class Config(object):

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    POSTGRES = {
        'user': 'neo_faucet',
        'pw': 'neo_faucet',
        'db': 'neo3_faucet',
        'host': 'localhost',
        'port': '5432',
    }

    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    RATELIMIT_ENABLED = True
    DROP_AMOUNT = 500

    # flask config
    SECRET_KEY = os.urandom(
        24)  # session secret key,init random string when app start
    PERMANENT_SESSION_LIFETIME = timedelta(seconds=1200)  # session expire time

    # Github config
    # local
    # GITHUB_CLIENT_ID = '205be6d17715fd71c4b2'
    # GITHUB_CLIENT_SECRET = '083391b15a1e7e36f12732c7f40b028f00b1e8aa'
    # test
    
    # prod
    GITHUB_CLIENT_ID = '332dbac3756470c983b6'
    GITHUB_CLIENT_SECRET = '08184bd1fdcccee3bccb59c34cb40099637c0c04'

    if ENV=="test":
        GITHUB_CLIENT_ID = 'cf5c80adab6f96806e05'
        GITHUB_CLIENT_SECRET = '4583c7c12ee734744566be5dee95d77b18a00258'

        
        


