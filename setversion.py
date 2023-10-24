# Python program to set the version.
##############################################


def fileProcess( name, lineFunction ):
	with open( name, 'r' ) as filestream:
		if filestream.closed:
			print(f"file {name} not open.")
			return

		output = ""
		print(f"--- Processing {name} ---------")
		while 1:
			if line := filestream.readline():
				output += lineFunction( line )
			else:
				break
	if not output: return			# basic error checking

	print(f"Writing file {name}")
	with open( name, "w" ) as filestream:
		filestream.write( output );
	
	
def echoInput( line ):
	return line
	

import sys
major = input( "Major: " )
minor = input( "Minor: " )
build = input( "Build: " )

print "Version: " + `major` + "." + `minor` + "." + `build`

#### Write the buildlilith #####

def buildlinuxRule( line ):

	i = line.rfind( "_" )

	if i >= 4 and line[i] == "_" and line[i-2] == "_" and line[i-4] == "_":
		# This is ghetto. Should really use regular expressions.
		i -= 4
		print "buildmicro instance found"
		return line[0:i] + "_" + `major` + "_" + `minor` + "_" + `build` + line[i+6:]
	else:
		return line

fileProcess( "buildmicro", buildlinuxRule )


