from dataclasses import dataclass
from environs import Env

@dataclass
class TgBot:
    token: str
@dataclass
class Config:
    tg_bot: TgBot

def add_config_data():
    env = Env()
    env.read_env('.env')
    return Config(TgBot(token=env('BOT_token')))