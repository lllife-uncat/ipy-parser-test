from functools import wraps
from time import time


def timed(f) :
    """
    Timeed decoration.
    Calculate running time for each funtion. """

    @wraps(f)
    def wrapper(*args, **kwds) :
        start = time()
        result = f(*args, **kwds)
        elapsed = time() - start
        print "%s" % (f.__name__)
        print ("-" * 60)
        print "Took %f time to finish" % (elapsed)
        print "\n"
        return result
    return wrapper
