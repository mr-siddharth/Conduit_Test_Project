import os
import configurations.config as config


def get_base_url():
    return config.settings["base_url"]


def get_test_email():
    return os.environ.get('CONDUIT_TEST_EMAIL')


def get_test_password():
    return os.environ.get('CONDUIT_TEST_PASSWORD')


def get_test_username():
    return config.settings["username"]
