import subprocess
def run_cmd(command):
    output = subprocess.run(command.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if output.returncode == 0:
        print(output.stdout)
    else:
        print(output.stderr)



if __name__ == "__main__":

    commands={"start_hadoop":"start-all.sh","stop_hadoop":"stop-all.sh",
                "version":"hadoop version","mkdir":"hadoop fs -mkdir /",
                "lsr":"hadoop fs -ls -R /","ls":"hadoop fs -ls /",
                "read_file":"hadoop fs -cat /newDataFlair/new.txt"}
    run_cmd(commands["read_file"])
