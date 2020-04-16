"""
Commands module.
Contains all start-commands, subcommands and CLI Interface creation.

Note: Be careful with file-scoped imports in these subfiles.
    as they are parsed on startup, nothing containing optional modules should be loaded.
"""
from tradingbot.commands.arguments import Arguments
from tradingbot.commands.trade_commands import start_trading
from tradingbot.commands.build_config_commnads import start_new_config
