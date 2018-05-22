class Parent(object):
	def implicit(self):
		print("Parent implicit()")

class Children(Parent):
	pass

dad =Parent()
son = Children()

dad.implicit()
son.implicit()
