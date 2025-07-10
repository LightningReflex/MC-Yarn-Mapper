from tkinter import *
from tkinter import ttk
# import sv_ttk
import tkinter.scrolledtext
from concurrent.futures import ThreadPoolExecutor
import time
import os
import re

# Global variables
version = '1.0.0'
tabCharacter = '	'



# Functions
def clear():
	inputCode.delete('1.0', END)
	outputCode.config(state=NORMAL)
	outputCode.delete('1.0', END)
	outputCode.config(state=DISABLED)

def remap():
	# Check if the user has selected a mapping
	if (defaultOption.get() == 'Choose a yarn mapping (mappings folder)'):
		outputCode.config(state=NORMAL)
		outputCode.insert(END, 'Please select a yarn mapping')
		outputCode.config(state=DISABLED)
		return
	# Clear the output field
	outputCode.config(state=NORMAL)
	outputCode.delete('1.0', END)
	outputCode.config(state=DISABLED)

	# Get the input code
	inputCodeText = inputCode.get('1.0', END)
	inputCodeText = inputCodeText.splitlines()

	# Get the mappings
	# 
	# v1	official	intermediary	named
	# CLASS	a	net/minecraft/class_5973	net/minecraft/util/math/MathConstants
	# METHOD	agh	(Lsc;ZLrm$a;)V	a	method_43505	sendChatMessage
	# FIELD	agi	Lagh;	d	field_14008	player
	# 
	with open('mappings/' + defaultOption.get(), 'r') as f:
		mappingFile = f.read()
	mappingFile = mappingFile.splitlines()

	# Create a dict with the mappings
	mappingDict = {}
	for line in mappingFile:
		line = line.split(tabCharacter)
		v1 = line[0]
		official = line[1]
		intermediary = ''
		named = ''
		if (line[0] == 'CLASS'):
			intermediary = line[2]
			named = line[3]
		elif (line[0] == 'METHOD'):
			intermediary = line[4]
			named = line[5]
		elif (line[0] == 'FIELD'):
			intermediary = line[4]
			named = line[5]
		# get just the class name from the intermediary
		intermediaryName = intermediary.split('/')[-1]
		if '$' in intermediaryName:
			intermediaryNameInnerClass = intermediaryName.split('$')[1]
		namedName = named.split('/')[-1]
		if '$' in namedName:
			namedNameInnerClass = namedName.split('$')[1]
			# Add the mappings to the dict
			mappingDict[intermediaryNameInnerClass] = namedNameInnerClass
		else:
			# Add the mappings to the dict
			mappingDict[intermediaryName] = namedName

	# Remap the code
	outputCodeText = ''
	for line in inputCodeText:

		# Compare line to regex for class, method, field
		# If it matches, remap it
		# If it doesn't match, just add it to the output
		regexClass = r'(class_[0-9]+)'
		regexMethod = r'(method_[0-9]+)'
		regexField = r'(field_[0-9]+)'
		regexComp = r'(comp_[0-9]+)' # No clue what comp is, but Minecraft uses it

		for regexFound in re.findall(regexClass, line):
			# Remap class
			intermediaryClassName = regexFound
			if intermediaryClassName in mappingDict:
				namedClassName = mappingDict[intermediaryClassName]
				line = line.replace(intermediaryClassName, namedClassName)

		for regexFound in re.findall(regexMethod, line):
			# Remap method
			intermediaryMethodName = regexFound
			if intermediaryMethodName in mappingDict:
				namedMethodName = mappingDict[intermediaryMethodName]
				line = line.replace(intermediaryMethodName, namedMethodName)

		for regexFound in re.findall(regexField, line):
			# Remap field
			intermediaryFieldName = regexFound
			if intermediaryFieldName in mappingDict:
				namedFieldName = mappingDict[intermediaryFieldName]
				line = line.replace(intermediaryFieldName, namedFieldName)

		for regexFound in re.findall(regexComp, line):
			# Remap comp
			intermediaryCompName = regexFound
			if intermediaryCompName in mappingDict:
				namedCompName = mappingDict[intermediaryCompName]
				line = line.replace(intermediaryCompName, namedCompName)

		outputCodeText += line + '\n'
	outputCodeText = outputCodeText[0:-1]

	# Display the output code
	outputCode.config(state=NORMAL)
	outputCode.insert(END, outputCodeText)
	outputCode.config(state=DISABLED)

def refreshMappingList():
	lastKnownMappingList = ['']
	defaultOption.set('Choose a yarn mapping (mappings folder)')
	while True:
		if (os.listdir('mappings') != lastKnownMappingList):
			# Reset var and delete all old options
			defaultOption.set('Choose a yarn mapping (mappings folder)')
			yarnMappingSelection.children['menu'].delete(0, 'end')

			# Set the new list
			for file in os.listdir('mappings'):
				if file != 'How-To-Map.md':
					yarnMappingSelection.children['menu'].add_command(label=file, command=tkinter._setit(defaultOption, file))
			lastKnownMappingList = os.listdir('mappings')
		time.sleep(1)



# Set up the main window
root = Tk()

root.title(f'MC Remapper - v{version}')
root.iconbitmap('resources/Logo.ico')
# root.minsize(900, 700)
# root.maxsize(900, 700)
# root.resizable(False, False)
root.geometry('900x700')

root.configure(bg='#2d2d2d')


# # Add the input and output fields
# inputCodeLabel = Label(root, text='Input Code', bg='#2d2d2d', fg='#ffffff')
# inputCodeLabel.place(x=10, y=10)

# inputCode = tkinter.scrolledtext.ScrolledText(width=108, height=19, bg='#3d3d3d', fg='#ffffff', font=('Courier', 10))
# inputCode.place(anchor='center', relx=0.5, rely=0.265)

# outputCodeLabel = Label(root, text='Output Code', bg='#2d2d2d', fg='#ffffff')
# outputCodeLabel.place(x=10, y=360)

# outputCode = tkinter.scrolledtext.ScrolledText(width=108, height=19, bg='#3d3d3d', fg='#ffffff', font=('Courier', 10))
# outputCode.config(state=DISABLED)
# outputCode.place(anchor='center', relx=0.5, rely=0.767)

# # Add the buttons
# clearButton = ttk.Button(root, text='Clear', command=lambda: clear())
# clearButton.place(anchor='center', relx=0.14, rely=0.516)

# defaultOption = StringVar(root)
# defaultOption.set('')
# yarnMappingSelection = OptionMenu(root, defaultOption, '')
# yarnMappingSelection.place(anchor='center', relx=0.75, rely=0.516)
# executor = ThreadPoolExecutor(max_workers=1)
# executor.submit(refreshMappingList)

# remapButton = ttk.Button(root, text='Remap', command=lambda: remap())
# remapButton.place(anchor='center', relx=0.954, rely=0.516)

# Setup grid
Grid.rowconfigure(root,1,weight=1)
Grid.rowconfigure(root,4,weight=1)
Grid.columnconfigure(root,0,weight=1)

# Add the input and output fields
inputCodeLabel = Label(root, text='Input Code', bg='#2d2d2d', fg='#ffffff')
# inputCodeLabel.place(x=10, y=10)
inputCodeLabel.grid(row=0, column=0, padx=0, pady=10, columnspan=3)

inputCode = tkinter.scrolledtext.ScrolledText(width=1, height=1, bg='#3d3d3d', fg='#ffffff', font=('Courier', 10))
# inputCode.place(anchor='center', relx=0.5, rely=0.265)
inputCode.grid(row=1, column=0, padx=10, pady=0, columnspan=3, sticky='nesw')

outputCodeLabel = Label(root, text='Output Code', bg='#2d2d2d', fg='#ffffff')
# outputCodeLabel.place(x=10, y=360)
outputCodeLabel.grid(row=3, column=0, padx=0, pady=0, columnspan=3)

outputCode = tkinter.scrolledtext.ScrolledText(width=1, height=1, bg='#3d3d3d', fg='#ffffff', font=('Courier', 10))
outputCode.config(state=DISABLED)
# outputCode.place(anchor='center', relx=0.5, rely=0.767)
outputCode.grid(row=4, column=0, padx=10, pady=10, columnspan=3, sticky='nesw')

# Add the buttons
clearButton = ttk.Button(root, text='Clear', command=lambda: clear())
# clearButton.place(anchor='center', relx=0.14, rely=0.516)
clearButton.grid(row=2, column=0, padx=10, pady=10, sticky='w')

defaultOption = StringVar(root)
defaultOption.set('')
yarnMappingSelection = OptionMenu(root, defaultOption, '')
# yarnMappingSelection.place(anchor='center', relx=0.75, rely=0.516)
yarnMappingSelection.grid(row=2, column=1, padx=10, pady=10)
executor = ThreadPoolExecutor(max_workers=1)
executor.submit(refreshMappingList)

remapButton = ttk.Button(root, text='Remap', command=lambda: remap())
# remapButton.place(anchor='center', relx=0.954, rely=0.516)
remapButton.grid(row=2, column=2, padx=10, pady=10)


# Run the main loop
if __name__ == '__main__':
	# sv_ttk.set_theme('dark')
	root.mainloop()
