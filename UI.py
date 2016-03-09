import os

while True:
	usecase = input("Plese enter the number of your desired use-case or q to exit: ")
	if usecase == 'q':
		break
	command = "python usecase" + usecase + ".py"
	os.system(command)
