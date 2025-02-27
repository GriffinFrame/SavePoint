###
####bash: pip install paramiko
###


import paramiko

def ssh_connect(hostname, username, password, command):
    """Connect to the remote device over SSH and execute a command."""
    try:
        # Initialize SSH client
        client = paramiko.SSHClient()
        
        # add the host key if missing
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        print(f"Connecting to {hostname}...")
        client.connect(hostname, username=username, password=password)

         
        print(f"Executing command: {command}")
        stdin, stdout, stderr = client.exec_command(command)
        
        # Retrieve the output and error if any
        output = stdout.read().decode()
        error = stderr.read().decode()

        
        if output:
            print(f"Output: {output}")
        if error:
            print(f"Error: {error}")
        
        # Close the SSH connection or it will shit out
        client.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Define connection parameters
    hostname = "192.168.0.33"   #can use both .local hostename and local IP
    username = "oluna"  
    password = "5862"  
    command = "brutal_backshots.py" 

    
    ssh_connect(hostname, username, password, command)




