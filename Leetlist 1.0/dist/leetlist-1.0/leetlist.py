#!/usr/bin/python
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#Copywrite (c) 2012,2013 Rogue Squadron Technologies
#
#L33tL1st:
# Password List Modification Tool
#
#Authors: 
# Matt "Ronin" Harvey
# Mike "Stockho1m" Mahaffey
#   
# Members of Rogue Squadron
# version 1.0
#
# L33tL1st provides the ability to grow a simple password list
# into a highly effecient password bypass list. It does this 
# by putting simple modifications of stings together, which, 
# together can make a highly effective and efficient password
# bypass list. This tool works best after passive information
# gathering and spydering of key words is complete. Use this
# tool to grow a simple list into a highly dynamic and fully 
# customizable list. 
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



#Libs added 
#===================================================================
import argparse
import sys
import os.path
import string
from string import maketrans
#===================================================================

#Defining main()
def main():
	parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
	description='Leetlist: Password List Modification Tool', 
	add_help='True',
	prog='leetlist',
	epilog='''\
For more information see the man pages. man leetlist
	''')

# Adding arguments
#============================================================================================================================================================
	parser.add_argument('--count', dest='count', metavar='File', nargs="?", type=argparse.FileType('r'), default=sys.stdin, 
			    help="Gives a total count of lines in the user defined file")
	parser.add_argument('--version',  action='version', version='%(prog)s Version: Beta 1.1', help ="Prints version number")
#	parser.add_argument('-V', dest='verbose', action='store_true', help="Enable Verbose Mode (prints to screen and file")
	parser.add_argument('-p', dest='prefix', metavar='[Prefix]', action='store', default='', help="Add a user defined prefix")
	parser.add_argument('-s', dest='suffix', metavar='[Suffix]', action='store', default='', help="Add a user defined suffix")
	parser.add_argument('-C', dest='caps', action='store_true', help="Capitalize the first letter of each word")
	parser.add_argument('-n', dest='subnum', action='store_true', help="Substitute letters with numbers")
	parser.add_argument('-c', dest='subchar', action='store_true', help="Substitute characters with Special Characters")
	parser.add_argument('-1', dest='add_one', action='store_true', help="A quick option to append 1 to the end of the string")
	parser.add_argument('-i', dest='infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help="List to be modified")
	parser.add_argument('-o', dest='outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout,  help="Name of new list to be created")
	args = parser.parse_args()
#==============================================================================================================================================================

#Checking the contents of the Namespace 'args'
#==================================================================
#Debug code:
#	print "Prefix = ", args.prefix
#	print "Suffix = ", args.suffix
#	print "Caps = " , args.caps
#	print "Subnum = ", args.subnum
#	print "Subchar = ", args.subchar
#	print "Infile = ", args.infile
#	print "Outfile = ", args.outfile
#	print "Add_one = ", args.add_one
#	print "Count = ", args.count
#	print "Version = ", args.version
#==================================================================

# if statements
#==================================================================	
	if len(sys.argv)==1:
    		parser.print_help()
    		sys.exit(1)
#==================================================================
	#Capitalizing the first letter
	if args.caps == True:
		def firstLetterCap(n):
			p=n[0:1]
			args.outfile.write(p.upper()+n[1:])
		myline = args.infile.readline()
		while myline:
			firstLetterCap(myline)
			myline = args.infile.readline()
		args.infile.close()
		print "Capitalization of List Successful!"
#=====================================================================
	#Adding Special Character Substitution
	elif args.subchar:
		def charScan(n):
			intable = "aAiIsScC"
			outtable = "@@!!$$(("
			trantable = maketrans(intable, outtable)
			p = myline.translate(trantable)
			args.outfile.write(p)
		myline = args.infile.readline()
		while myline:
			charScan(myline)
			myline = args.infile.readline()
		args.infile.close
		print "Special Character Substitution Successful!"

#=====================================================================
	#Adding Number Substitution
	elif args.subnum:
		def numScan(n):
			intable = "aAeElLoOtT"
			outtable = "4433110077"
			trantable = maketrans (intable, outtable)
			p = myline.translate (trantable)
			args.outfile.write(p)
		myline = args.infile.readline()
		while myline:
			numScan(myline)
			myline = args.infile.readline()
		args.infile.close
		print "Special Number Substitution Successful!"
#=====================================================================
#	#Adding Print Version
#	elif args.version == True:
#		print "\nCurrent Version is: Beta 1.1"
#=====================================================================
	#Adding "1" to the end of the string
	elif args.add_one == True:
		def addingOne(n):
			p = str(n.strip()+"1\n")
			args.outfile.write(p)
		myline = args.infile.readline()
		while myline:
			addingOne(myline)
			myline = args.infile.readline()
		args.infile.close
		print "Adding 1 to List Successful!"
#======================================================================
	#Adding a prefix to the string
	elif args.prefix:
        	s = str(args.prefix)
        	def addprefix(n):
            		p = s + n
            		args.outfile.write(p)
        	myline = args.infile.readline()
        	while myline:
            		addprefix(myline)
            		myline = args.infile.readline()
        	args.infile.close
		print "Adding Prefix to List Successful!"
#======================================================================
    	#Adding a suffix to the string
   	elif args.suffix:
        	s = str(args.suffix)
        	def addsuf(n):
            		p = str(n.strip()+s+"\n")
           		args.outfile.write(p)
        	myline = args.infile.readline()
        	while myline:
            		addsuf(myline)
            		myline = args.infile.readline()
        	args.infile.close
		print "Adding Suffix to List Successful!"
#======================================================================
	#Adding Line count
	elif args.count:
		num = 0
		for line in args.count.xreadlines():
			num += 1
		print "\nTotal Number of Passwords in File: " + str(num) + "\n"
#======================================================================

main()
