# GoogleAPIMD5
Script to pull metadata from Google Drive API, including MD5 checksum

Using authentication from Google Quickstart Python script. To run follow authentication instructions written in the Python Code.

Get the ID of the folder you want to scan from by going into Google Drive and copy the folder ID at the end of the URI.

Edit folder_id with your relevant google ID.

The script will generate a CSV file with a list of all files and folders listed underneath the folder you have stated. It will show the MD5, size of file, id and parent id of files and folders. It does not include files or folders which have been sent to the recycle bin. 

The script will also print out the numbers of files and folders included in the selection.

