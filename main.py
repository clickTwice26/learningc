import os
import json
from datetime import datetime
from random import randint
from shutil import copyfile
from sys import argv, exit
working_dir = os.getcwd()
config_data = json.load(open(working_dir+"/config.json", "r"))
#print(config_data)
console_inputs = argv

def currentTime(wdm="both"):
	now = datetime.now()
	dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
	if wdm == "date":
		date = dt_string.split(" ")[0]
		return date
	elif wdm == "time":
		time = dt_string.split(" ")[1]
		return time
	elif wdm == "filename":
		dt_string = dt_string.replace("/","_")
		dt_string = dt_string.replace(":", "_")
		dt_string = dt_string.replace(" ", "_")
		return dt_string
	else:
		return dt_string
def cout(comment):
	error_list = ["failed", "error", "unsuccessful", "problem", "fix"]
	error_check = any(item in comment for item in error_list)

	if error_check is True:
		prefix = "[X]"
	else:
		prefix = "[+]"
	print(f"{prefix}-> {comment}")
class Program:
	def __init__(self, session, session_comment=None):
		self.__session = session
		self.__session_comment = session_comment


	def log(self, comment, consoleOut=False):
		consoleOutStr = f"[cOut] [{comment}]"
		log_data = f"[cOut-{self.__session}] [{currentTime()}] {comment}"
		if config_data["consoleOut"] == "True":
			print(consoleOutStr)
		if config_data["consoleLog"] == "True":
			with open(working_dir+"/console_log.txt", "a") as console_logger:
				console_logger.write(log_data+"\n")
				console_logger.close()

		#log_overflow_checker
	def log_overflow_fix(self):
		log_limit = config_data["console_log_limit"]
		try:
			current_log_amount = len(open("console_log.txt", "r").read().splitlines())
		except FileNotFoundError:
			current_log_amount = 0
		print("Console_logs_amount: ",current_log_amount)
		print("Global_log_limit: ", log_limit)
		if current_log_amount > int(log_limit):
			print("Log_Overflowed")
			#print("Log_getting_backedup")
			try:
				copyfile("console_log.txt", f"{working_dir}/backups/console_log_{currentTime('filename')}.txt")
				os.remove(working_dir+"/console_log.txt")
				cout("Log Backed Up Successfull")
			except Exception as error:
				cout("Log Backup Failed")
				try:
					cout("Trying to fix the problem")
					os.mkdir(working_dir+"/backups")

					copyfile("console_log.txt", f"{working_dir}/backups/console_log_{currentTime('filename')}.txt")
					os.remove(working_dir+"/console_log.txt")

				except Exception as error:
					cout(error)
	def __str__(self):
		return "Don't use without"

	def gitcommit(self, commit_name):
		os.system(f"cd {working_dir} && git add .")
		os.system(f"cd {working_dir} && git commit -m '{commit_name}_{self.__session}'")
	def gitpush(self, branch_name="default"):
		if branch_name == "default":
			cout("No branch selected to push")
			cout("default branch selected-> 'master'")
			os.system(f"git push -u origin master")
		else:
			os.system(f"git push -u origin {branch_name}")
	def console_input_manage(self,)
session_code = randint(10000, 309000)
mains = Program(session_code)
#mains.log("testing")
#mains.log("testing_2")
print(console_inputs)











mains.log_overflow_fix()


