"""Application configuration."""
import os
from datetime import timedelta


class Config(object):
    """Base configuration."""

    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    CORS_ORIGIN_WHITELIST = [
        'http://0.0.0.0:3000',
        'http://ltesocalhost:3000',
        'http://0.0.0.0:3002',
        'http://localhost:3002'
    ]


class ProdConfig(Config):
    """Production configuration."""

    ENV = 'prod'
    DEBUG = False


class DevConfig(Config):
    """Development configuration."""

    ENV = 'dev'
    DEBUG = True


class TestConfig(Config):
    """Test configuration."""

    TESTING = True
    DEBUG = True