import os

class Config:
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://username:password@localhost/blogs'


class ProdConfig(Config):
  pass

class TestConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:nyururu@localhost/blogs_test'


class DevConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:nyururu@localhost/blogs'
  DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}