import subprocess
# "hadoop","fs","-ls","/"]
def run_cmd(command):
    output = subprocess.run(command.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if output.returncode == 0:
        print(output.stdout)
    else:
        print(output.stderr)

run_cmd("hadoop fs -ls /")