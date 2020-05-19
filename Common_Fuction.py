import subprocess

def execution(cmd_list):
    for i in cmd_list:
        print(i)
        p = subprocess.Popen(["start", "cmd", "/k", 'adb shell '+i], shell=True)
        p_staus = p.wait()
        print(p_staus)