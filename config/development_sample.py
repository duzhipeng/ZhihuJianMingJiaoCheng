# -*- coding: utf-8 -*-
from .default import Config


class DevelopmentConfig(Config):
    # Flask
    DEBUG = True
    SECRET_KEY = ''
