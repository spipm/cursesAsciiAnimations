
from os import listdir
from os.path import isfile, join

from time import sleep
from random import choice

minAnimationTime = 35


def drawAnimation(stdscr, width, height):
	'''
		Show animation
	'''
	stdscr.clear()

	# choose animation
	availableAnimations = [f for f in listdir('animations/') if not isfile(join('animations/', f))]
	animationChosen = choice(availableAnimations)

	# get animation data
	with open('animations/'+animationChosen+'/'+animationChosen+'.txt','r') as fin:
		animationData = fin.read().split('[FILEBREAK]')

	animationTime = 0
	while animationTime < minAnimationTime:

		for frame in animationData:
			frameLines = frame.split("\n")

			# show animation 'frame'
			y=0
			animationX = int((width/2) - (len(frameLines[0])/2))

			for line in frameLines:
				stdscr.addstr(y,animationX,line)
				y+=1
				if y >= height:
					break

			animationTime += 1

			stdscr.refresh()
			sleep(0.1)
