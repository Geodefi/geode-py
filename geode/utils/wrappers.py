import logging
from time import sleep
import requests
from requests.exceptions import JSONDecodeError


from geode.exceptions import (
    HTTPRequestException,
    UnexpectedResponseException,
    MaxAttemptException,
)
from geode.globals import MAX_ATTEMPT, ATTEMPT_RATE


def multiple_attempt(call_attempt=None):
    def wrap(*args, **kwargs):
        count = 0
        while True:
            try:
                return call_attempt(*args, **kwargs)
            except Exception as exc:
                if count < MAX_ATTEMPT:
                    logging.info(f"Call failed {count} times, will retry...")
                    sleep(ATTEMPT_RATE)
                    count += 1
                else:
                    raise MaxAttemptException(
                        f"{call_attempt} Call Error"
                    ) from exc

    return wrap


@multiple_attempt
def http_request(func):
    def wrap(*args, **kwargs):
        try:
            url, full = func(*args, **kwargs)
            res = requests.get(url, timeout=10)
            if res.status_code == 200:
                try:
                    if full:
                        return res.json()
                    else:
                        return res.json()["data"]
                except JSONDecodeError:
                    return res.content
            else:
                raise HTTPRequestException(
                    res.status_code, res.reason, res.text
                )
        except Exception as exc:
            raise UnexpectedResponseException from exc

    return wrap
