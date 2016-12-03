from Controllers import XboxController
import time

XboxController.Filter(3)

while True:
	inp = XboxController.Input()

	XboxController.Vibrate(inp['RT'], inp['RT'])

	if (inp['Buttons'] & XboxController.A):
		print(inp['LX'], inp['LY'], inp['LT'])

	if (inp['Buttons'] & XboxController.UP):
		XboxController.Filter(0)
	if (inp['Buttons'] & XboxController.LEFT):
		XboxController.Filter(1)
	if (inp['Buttons'] & XboxController.DOWN):
		XboxController.Filter(2)
	if (inp['Buttons'] & XboxController.RIGHT):
		XboxController.Filter(3)

	if (inp['Buttons'] & XboxController.START):
		XboxController.Calibrate()

	if (inp['Buttons'] & XboxController.BACK):
		break

	time.sleep(0.01)
