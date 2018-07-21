# -*- coding: utf-8 -*-
from .default import Config


class ProductionConfig(Config):
    # Flask
    DEBUG = False
    SECRET_KEY = ''
