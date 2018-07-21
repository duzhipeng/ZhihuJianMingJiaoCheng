# -*- coding: utf-8 -*-
from .default import Config


class UATConfig(Config):
    # Flask
    DEBUG = False
    SECRET_KEY = ''
