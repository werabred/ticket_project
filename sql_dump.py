#this will have code to dump sql database tickets_db.
import subprocess



command = "mysqldump --user=flask1 --password=ubuntu tickets_db > tickets_db.sql"
subprocess.call(command, shell=True)

print("dump successful")
