import csv, os

os.makedirs('headerRemoved', exist_ok=True) #creates a new folder to save all the modified files

# Loop through every file in the current working directory.
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue    # skip non-csv files

    print('Removing header from ' + csvFilename + '...')