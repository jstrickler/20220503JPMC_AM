from datetime import datetime
import logging
from functools import wraps

logging.basicConfig(
    filename='timestamps.log',
    level=logging.DEBUG,
)

def log_timestamp(old_func):
    old_func_name = old_func.__name__

    @wraps(old_func)
    def replacement(*args, **kwargs):
        logging.debug(
            f"Calling {old_func_name} at {datetime.now().ctime()}"
        )
        return old_func(*args, **kwargs)

    return replacement

@log_timestamp
def spam():
    print("Hello from spam()")
# spam = timestamp(spam)


@log_timestamp
def ham():
    print("Hello from ham()")

def toast():
    print("Hello from toast()")

toast = log_timestamp(toast)

spam()
ham()
spam()
spam()
spam()
toast()
toast()
ham()
toast()

print(spam.__name__)
print(toast.__name__)


