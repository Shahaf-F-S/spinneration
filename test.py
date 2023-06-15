# test.py

import time

from spinneroo import Spinners, Spinner

def main() -> None:
    """A function to run the main test."""

    spinner = Spinner(
        title='Program', message='processing',
        elements=Spinners.line.value['frames'],
        complete=f"complete", counter=True, clean=True
    )
    spinner.spin()

    time.sleep(5)

    spinner.stop()
# end main

if __name__ == "__main__":
    main()
# end if