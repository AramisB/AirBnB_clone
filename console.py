import cmd

class HBNBCommand(cmd.Cmd):
	prompt = '(hbnb) '

	def do_quit(self, arg):
	"""Quit command to exit the program"""
	return True

	def do_EOF(self, arg):
	"""Handles EOF signal to exit the program"""
	print()
	return True

	def emptyline(self):
	"""Handles empty line"""
	pass

if __name__ == '__main__':
	HBNBCommand().cmdloop()
