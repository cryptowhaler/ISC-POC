#!/usr/bin/env python3
"""
Main  bot script.
"""

#from tradingbot.exceptions import FreqtradeException, OperationalException
import sys

# check min. python version
if sys.version_info < (3, 6):
    sys.exit("Trading Bot requires Python version >= 3.6")

# flake8: noqa E402
import logging
from typing import Any, List

from tradingbot.commands import Arguments


logger = logging.getLogger('tradingbot')


def main(sysargv: List[str] = None) -> None:
    """
    This function will initiate the bot and start the trading loop.
    :return: None
    """

    return_code: Any = 1
    try:
        arguments = Arguments(sysargv)  #initializes Arguments (which is a class) instance
        args = arguments.get_parsed_arg()

        # Call subcommand.
        if 'func' in args:
            return_code = args['func'](args)

    except SystemExit as e:
        return_code = e


    #     else:
    #         # No subcommand was issued.
    #         raise OperationalException(
    #             "Usage of Freqtrade requires a subcommand to be specified.\n"
    #             "To have the bot executing trades in live/dry-run modes, "
    #             "depending on the value of the `dry_run` setting in the config, run Freqtrade "
    #             "as `tradingbot trade [options...]`.\n"
    #             "To see the full list of options available, please use "
    #             "`tradingbot --help` or `tradingbot <command> --help`."
    #             )
    #
    # except SystemExit as e:
    #     return_code = e
    # except KeyboardInterrupt:
    #     logger.info('SIGINT received, aborting ...')
    #     return_code = 0
    # except FreqtradeException as e:
    #     logger.error(str(e))
    #     return_code = 2
    # except Exception:
    #     logger.exception('Fatal exception!')
    # finally:
    #     sys.exit(return_code)


if __name__ == '__main__':
    main()
