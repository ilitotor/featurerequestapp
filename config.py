import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Development(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(os.path.join(basedir, "features.db"))


class Testing(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(os.path.join(basedir, "features_test.db"))


config = dict(
    development=Development(),
    testing=Testing()
)
