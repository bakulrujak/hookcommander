import paramiko
from utils.config import Config

def send_cmd():
	con = paramiko.SSHClient()
	con.load_system_host_keys()
	con.connect(Config.jaguar_addr)
	try:
		e = con.exec_command(Config.jaguar_cmd)
		return 'Executed!'
	except:
		return 'Ops, something went wrong!'
	finally:
		con.close()