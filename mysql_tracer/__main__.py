"""
CLI script to run MySQL SELECT statements

It produces a copy of provided file with additional metadata and an export of results in CSV format
"""
import logging

from mysql_tracer import _configuration
from mysql_tracer._cursor_provider import CursorProvider
from mysql_tracer._query import Query
from mysql_tracer.args_parser import get_main_args_parser, get_log_args_parser

log = logging.getLogger('mysql_tracer')


def configure_logger(log_level):
    """
    Set level of the main logger and add a console handler with the same level

    :param log_level: verbosity level of the logger
    :type log_level: 'DEBUG' | 'INFO' | 'WARNING' | 'ERROR' | 'CRITICAL'
    :return: None
    """
    log.setLevel(log_level)
    console = logging.StreamHandler()
    console.setLevel(log_level)
    console.setFormatter(logging.Formatter(fmt='%(asctime)s %(levelname)s - %(name)s: %(message)s'))
    log.addHandler(console)


def main():
    log_args_parsers = get_log_args_parser()
    log_args, remaining_args = log_args_parsers.parse_known_args()

    if log_args.log_level:
        configure_logger(log_args.log_level)

    config = _configuration.get()

    main_args_parser = get_main_args_parser([log_args_parsers], config)
    main_args = main_args_parser.parse_args()

    if not log_args.log_level and main_args.log_level:
        configure_logger(main_args.log_level)

    CursorProvider.init(main_args.host, main_args.user, main_args.port, main_args.database, main_args.ask_password,
                        main_args.store_password)

    template_vars = main_args.template_vars if main_args.template_vars else []
    queries = [Query(path, dict(template_vars)) for path in main_args.query]

    for query in queries:
        if main_args.display:
            query.display()
        else:
            query.export(destination=main_args.destination)


if __name__ == '__main__':
    main()
