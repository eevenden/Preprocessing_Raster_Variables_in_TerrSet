# -*- coding: utf-8 -*-

####################################################################################################################################
#
# Author: Emily Evenden
# Title: Processing Raster Variables in Terrset
# February 19, 2020
#
####################################################################################################################################

### Part 1: Directory Set Up
#
# This sets up the directories used in the code
# Imports Windows Python client
import win32com.client

# Import operating system interface. This allows Python to interact with the Windows operating system.
import os

# Set IDRISI API to variable IDRISI32 so the rest of the script can access Terrset IDRISI API
IDRISI32 = win32com.client.Dispatch('IDRISI32.IdrisiAPIServer')

# Print statement to make sure set up is finished
print "Settings Prepared"

# Set IDRISI working directory path the data folder. If you are using this code, you must update the file path here. 
IDRISI32.SetWorkingDir("C:\Users\EEvenden\Documents\Python\Final Project\Data\Prep_1")

# Set the script's working directory to same data folder. This script creates several files outside
# of the IDRISI library, and therefore needs a directory as well.
os.chdir("C:\Users\EEvenden\Documents\Python\Final Project\Data\Prep_1")

# Print statement to ensure working directory is set
print "Working Directory Set"

#################################################################################################################################

### Part 2: Create list of all Raster variables
# Making a list will allow us to batch process all the files in the folder

variables = [f for f in os.listdir(path) if os.path.isfile( os.path.join(path, f) )]

#################################################################################################################################

### Part 3: Find file projrection & reproject and resample

for v in variables:
	if file is path + ".rdc"
		f = open(v + ".RDC")
		ogref= f.readlines(12)
		f.close()

	IDRISI32.RunModule('PROJECT','1*v*ogref*("reproject_" + v)*(GA State Plane)

#ex. e.g., "project x 1*island1*latlong*island2*utm-3s*19*42*23*48*640*480*0*1" - need extent image. background value, and which transformation

