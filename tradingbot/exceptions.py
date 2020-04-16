class TradingBotException(Exception):
    """
    TradingBot base exception. Handled at the outermost level.
    All other exception types are subclasses of this exception type.
    """


class OperationalException(TradingBotException):
    """
    Requires manual intervention and will stop the bot.
    Most of the time, this is caused by an invalid Configuration.
    """


class DependencyException(TradingBotException):
    """
    Indicates that an assumed dependency is not met.
    This could happen when there is currently not enough money on the account.
    """


class InvalidOrderException(TradingBotException):
    """
    This is returned when the order is not valid. Example:
    If stoploss on exchange order is hit, then trying to cancel the order
    should return this exception.
    """


class TemporaryError(TradingBotException):
    """
    Temporary network or exchange related error.
    This could happen when an exchange is congested, unavailable, or the user
    has networking problems. Usually resolves itself after a time.
    """
