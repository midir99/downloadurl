"""Main module."""

import argparse
import logging
import sys

from . import downloadurl


def parse_args() -> argparse.Namespace:
    """Parsers the arguments from the command line and returns them."""
    parser = argparse.ArgumentParser(
        prog="downloadurl",
        description="Download the content of some URL!",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "url",
        help="The URL you want to download.",
        type=str,
    )
    parser.add_argument(
        "dest",
        help=(
            "The name of the file where the content of the URL will be downloaded ("
            "including the extension is not necessary)."
        ),
        type=str,
    )
    return parser.parse_args()


def main():
    """Main function."""
    args = parse_args()
    try:
        filename = downloadurl.downloadurl(args.url, args.dest)
        print(f"{args.url} was downloaded into {filename}")
    except Exception:
        logging.exception("Unable to download the URL %s", args.url)
        sys.exit(1)
