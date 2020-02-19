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
import linecache

# Set IDRISI API to variable IDRISI32 so the rest of the script can access Terrset IDRISI API
IDRISI32 = win32com.client.Dispatch('IDRISI32.IdrisiAPIServer')

# Print statement to make sure set up is finished
print "Settings Prepared"

# Set IDRISI working directory path the data folder. If you are using this code, you must update the file path here. 
IDRISI32.SetWorkingDir("C:\Users\eevenden\Documents\Advanced RS\Test_Folder_1")
working_folder = "C:\Users\eevenden\Documents\Advanced RS\Test_Folder_1"

#Set IDRISI Resourse folder. If you are using this code, you must update this pathway to the folder contain your unprocessed data.
IDRISI32.AddResourceDirToProject("C:\Users\eevenden\Documents\Advanced RS\Test_Folder_2")
resource_folder = "C:\Users\eevenden\Documents\Advanced RS\Test_Folder_2"

# Set the script's working directory to same data folder. This script creates several files outside
# of the IDRISI library, and therefore needs a directory as well.
os.chdir("C:\Users\eevenden\Documents\Advanced RS\Test_Folder_2")

# Print statement to ensure working directory is set
print "Working Directory Set"

#################################################################################################################################

### Part 2: Create list of all Raster variables
# Making a list will allow us to batch process all the files in the folder

variables = [f for f in os.listdir(resource_folder) if os.path.isfile(os.path.join(resource_folder, f))]

print variables

#################################################################################################################################

### Part 3: Find file projrections & reproject and resample

#Change TerrSet .rdc file to a .txt file
def change_end_txt(q):
        base = os.path.splitext(q)[0]
        os.rename(q, base + '.txt')
        print "okay"
        
#Change  .txt file to a TerrSet .rdc file 
def change_end_rdc(s):
        base = os.path.splitext(q)[0]
        os.rename(q, base + '.rdc')
        print "okay"

#Search folder and change endings of only .rdc files
for v in variables:
        if v.endswith(".rdc"):
                change_end(v)
                
#Retreive reference system to                
for v in variables:
        if v.endswith(".txt"):
                ref = []
                ogref = linecache.getline(v, 7)
                parse_ref = ' '.join(ogref.split())
                ref = parse_ref.split(' ')
                print ref
                
