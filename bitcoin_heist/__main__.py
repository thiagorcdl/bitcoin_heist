"""Entry point for the whole package."""
import sys
from bitcoin_heist.src.analysis import binary, main
from bitcoin_heist.src.constants import BINARY_PARAM

if __name__ == "__main__":
    if BINARY_PARAM in sys.argv:
        binary()
    else:
        main()
