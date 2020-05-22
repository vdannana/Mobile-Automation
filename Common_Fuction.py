import subprocess


'''
command_exection funtion execute windows commands in a new command prompt window
input arugumenet cmd_list is list of command to be executed.
'''
def execution(cmd_list):
    for i in cmd_list:
        print(i)
        p = subprocess.Popen(["start", "cmd", "/k", 'adb shell '+i], shell=True)
        p_staus = p.wait()
        print(p_staus)