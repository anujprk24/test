from flask import Flask
app = Flask(__name__)
import paramiko
from subprocess import call
from StringIO import StringIO
import subprocess
import os



def list_of_host():

	awscli_command = "ec2-describe-instances -O "AWS_access_key" -W "AWS_secret_key" --filter tag:Name=ABCD | grep 'running' | grep 'INSTAN$
        temp=os.popen(awscli_command).read()
        temp = str(temp).split('\n')
        print temp

def run_command_on_server(server, key_filename, command):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(server, username='ubuntu')
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
        res = ssh_stdout.readlines()
        err =  ssh_stdout.read()
        ssh.close()
        print str(res)
        print str(err)
        return res, err



if __name__ == "__main__":
        list_of_host()
