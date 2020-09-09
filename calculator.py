from tkinter import *

root = Tk()
root.title('calulator')
operation = ''

'''
This function takes in a number or operation and will add it to
the string that has been created previously. If nothing is 
passed when it is called, then it evaluates what is inside of it.
'''

def function(item):
	global operation
	if item == '':
		try:
			answer = eval(operation)
			e.delete(0, END)
			e.insert(0, answer)
		except ZeroDivisionError:
			e.delete(0, END)
			e.insert(0,'Can\'t divide by zero')
		except SyntaxError:
			e.delete(0, END)
			e.insert(0,'Syntax Error')


	elif item == 'clear':
		operation = ''
		e.delete(0, END)
	else:
		operation+= item
		e.delete(0, END)
		e.insert(0, operation)



#Creates display for calculator as well as creates the grid
#Weird white bar in display to be fixed soon!

Label(root).grid(row = 0)
Label(root).grid(row = 1)
Label(root).grid(row = 2)
Label(root).grid(row = 3)
Label(root).grid(row = 4)


e = Entry(root, width =35, borderwidth=5)
e.grid(row=0, column = 0, columnspan = 5)


display = Label(root, text = operation)
display.grid(row= 0)


#Buttons created and placed into the grid
one = Button(root, text = '1', command = lambda: function('1'))
one.grid(row = 1, column = 0, sticky = NSEW)

two = Button(root, text = '2', command = lambda: function('2'))
two.grid(row = 1, column = 1, sticky = NSEW)

three = Button(root, text = '3', command = lambda: function('3'))
three.grid(row = 1, column = 2, sticky = NSEW)

four = Button(root, text = '4', command = lambda: function('4'))
four.grid(row = 2, column = 0, sticky = NSEW)

five = Button(root, text = '5', command = lambda: function('5'))
five.grid(row = 2, column = 1, sticky = NSEW)

six = Button(root, text = '6', command = lambda: function('6'))
six.grid(row = 2, column = 2, sticky = NSEW)

seven = Button(root, text = '7', command = lambda: function('7'))
seven.grid(row = 3, column = 0, sticky = NSEW)

eight = Button(root, text = '8', command = lambda: function('8'))
eight.grid(row = 3, column = 1, sticky = NSEW)

nine = Button(root, text = '9', command = lambda: function('9'))
nine.grid(row = 3, column = 2, sticky = NSEW)

add = Button(root, text = '+', command = lambda: function('+'))
add.grid(row = 1, column = 3, sticky = NSEW)

sub= Button(root, text = '-', command = lambda: function('-'))
sub.grid(row = 2, column = 3, sticky = NSEW)

mult = Button(root, text = '*', command = lambda: function('*'))
mult.grid(row = 3, column = 3, sticky = NSEW)

divide = Button(root, text = '/', command = lambda: function('/'))
divide.grid(row = 4, column = 3, sticky = NSEW)

equals = Button(root, text = '=', command = lambda: function(''))
equals.grid(row = 1, column = 4, sticky = NSEW)

clear = Button(root, text = 'clr', command = lambda: function('clear'))
clear.grid(row = 4, column = 4, sticky = NSEW)

decimal = Button(root, text = '.', command = lambda: function('.'))
decimal.grid(row = 4, column = 2, sticky = NSEW)

negative= Button(root, text = '(-)', command = lambda: function('-'))
negative.grid(row = 4, column = 1, sticky = NSEW)

zero = Button(root, text = '0', command = lambda: function('0'))
zero.grid(row = 4, column = 0, sticky = NSEW)


def main():
	root.mainloop()

if __name__ == '__main__':
	main()







