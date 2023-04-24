

import os
import shutil
import datetime

# Path to the Downloads folder
downloads_folder = 'C:\\Users\\User\\Downloads'

# Path to the folder to_delete
to_delete_folder = 'C:\\Users\\User\\to_delete'

# Get the current date
current_date = datetime.datetime.now()

# Go through all files in the Downloads folder
for file in os.listdir(downloads_folder):
	# Get the path to the file
	file_path = os.path.join(downloads_folder, file)

	# Get the file's last modified date
	file_date = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))

	# Calculate the difference between the current date and the file's last modified date
	date_difference = current_date - file_date

	# If the file is older than 30 days
	if date_difference.days > 30:
		# Move the file to the to_delete folder
		shutil.move(file_path, to_delete_folder)