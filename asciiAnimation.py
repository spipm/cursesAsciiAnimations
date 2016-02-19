# amazing animations from http://www.qqpr.com
# cursus tutorial from http://ironalbatross.net/wiki/index.php?title=Python_Curses
# and https://docs.python.org/2/howto/curses.html
# and https://docs.python.org/2/library/curses.html?highlight=curses#module-curses

from time import sleep
import curses
from methods.funOnTheBun import drawAnimation


stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

height,width = stdscr.getmaxyx()


try:
	while 1:
		stdscr.clear()

		drawAnimation(stdscr, width, height)

		stdscr.refresh()
		sleep(0.4)

finally:
	curses.nocbreak()
	stdscr.keypad(0)
	curses.echo()
	curses.endwin()





