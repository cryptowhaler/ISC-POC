import logging

from tradingbot.exceptions import DependencyException, TemporaryError

logger = logging.getLogger(__name__)


API_RETRY_COUNT = 4

BAD_EXCHANGES = {   #Dict storing msgs to be displayed if exchange returns invalid
    "bitmex": "Various reasons.",
    "bitstamp": "Does not provide history. "
                "Details in https://github.com/freqtrade/freqtrade/issues/1983",
    **dict.fromkeys([
        'coinbase',
        'coinexchange',
        'coinmarketcap',
    ], "Does not provide timeframes. ccxt fetchOHLCV: False"),
    **dict.fromkeys([
        'bcex',
        'bit2c',
    ], "Does not provide timeframes. ccxt fetchOHLCV: emulated"),
}

MAP_EXCHANGE_CHILDCLASS = {
    'binanceus': 'binance',
    'binanceje': 'binance',
    'coindcx' : 'coindcx'
}


def retrier_async(f):
    async def wrapper(*args, **kwargs):
        count = kwargs.pop('count', API_RETRY_COUNT)
        try:
            return await f(*args, **kwargs)
        except (TemporaryError, DependencyException) as ex:
            logger.warning('%s() returned exception: "%s"', f.__name__, ex)
            if count > 0:
                count -= 1
                kwargs.update({'count': count})
                logger.warning('retrying %s() still for %s times', f.__name__, count)
                return await wrapper(*args, **kwargs)
            else:
                logger.warning('Giving up retrying: %s()', f.__name__)
                raise ex
    return wrapper


def retrier(f):
    def wrapper(*args, **kwargs):
        count = kwargs.pop('count', API_RETRY_COUNT)
        try:
            return f(*args, **kwargs)
        except (TemporaryError, DependencyException) as ex:
            logger.warning('%s() returned exception: "%s"', f.__name__, ex)
            if count > 0:
                count -= 1
                kwargs.update({'count': count})
                logger.warning('retrying %s() still for %s times', f.__name__, count)
                return wrapper(*args, **kwargs)
            else:
                logger.warning('Giving up retrying: %s()', f.__name__)
                raise ex
    return wrapper
