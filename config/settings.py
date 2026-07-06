"""
Application Settings

Loads all secrets from the .env file.

Never hardcode credentials anywhere else.
"""

from dotenv import load_dotenv
import os

load_dotenv()

DHAN_CLIENT_ID = os.getenv("DHAN_CLIENT_ID")

DHAN_ACCESS_TOKEN = os.getenv("DHAN_ACCESS_TOKEN")

APP_NAME = "AutoTrader"

APP_VERSION = "2.0.0"

DEBUG = True

INITIAL_WINDOW = 5

WINDOW_INCREMENT = 5

MAX_WINDOW = 15

MIN_VALID_PAIRS = 40