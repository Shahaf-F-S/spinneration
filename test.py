# test.py

import time

from spinneroo import Spinner

def main() -> None:
    """A function to run the main test."""

    spinner1 = Spinner(
        title='Process 1',
        message='processing',
        complete="complete",
        counter=True,
        clean=True,
        silence=False
    )
    spinner1.spin()

    time.sleep(5)

    spinner2 = Spinner(
        title='Process 2',
        message='processing',
        complete="complete",
        counter=True,
        clean=True,
        silence=False
    )
    spinner2.spin()

    time.sleep(5)

    spinner2.stop()

    time.sleep(5)

    spinner1.stop()
# end main

if __name__ == "__main__":
    main()
# end if