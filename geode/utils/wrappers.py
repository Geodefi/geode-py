import logging
import requests
from requests.exceptions import JSONDecodeError

from time import sleep

from geode.exceptions import BadRequestException, UnexpectedResponseException, MaxAttemptException
from geode.globals import MAX_ATTEMPT, ATTEMPT_RATE


def multipleAttempt(callAttempt=None):
    def wrap(*args, **kwargs):
        count = 0
        while True:
            try:
                return callAttempt(
                    *args, **kwargs)
            except:
                if count < MAX_ATTEMPT:
                    logging.info(
                        f"Call failed {count} times, will retry...")
                    sleep(ATTEMPT_RATE)
                    count += 1
                else:
                    raise MaxAttemptException(
                        f"{callAttempt} Call Error")
    return wrap


@multipleAttempt
def httpRequest(func):
    def wrap(*args, **kwargs):
        try:
            url = func(*args, **kwargs)
            res = requests.get(url)
            if res.status_code == 200:

                try:
                    return res.json()["data"]
                except JSONDecodeError:
                    return res.content
            else:
                raise BadRequestException(
                    res.status_code, res.reason, res.text)
        except:
            raise UnexpectedResponseException
    return wrap
