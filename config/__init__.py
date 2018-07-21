# -*- coding: utf-8 -*-
import os


def load_config():
    """加载配置类"""
    mode = os.environ.get('MODE')
    try:
        if mode == 'PRODUCTION':
            from .production import ProductionConfig
            return ProductionConfig
        elif mode == 'UAT':
            from .uat import UATConfig
            return UATConfig
        else:
            from .development import DevelopmentConfig
            return DevelopmentConfig
    except:
        from .default import Config
        return Config
