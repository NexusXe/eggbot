import speech, owobot, subprocess, os, signal

running = False

while True:
    desired_func = input('Type 1 for speech and 2 for normal op. To run 2 async, type 3. To kill realbot, type 4. >>')
    if desired_func == '1':
        speech.speech()
    elif desired_func == '2':
        owobot.owobot()
    elif desired_func == '3':
        proc = subprocess.Popen('python3 eggbot/owobot.py', stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
        running = True
    elif desired_func == '4':
        if running:
            os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
            print('Killed process.')
        else:
            print("Realbot wasn't running!")
    elif desired_func == 'EXIT':
        break
    else:
        print('no bueno bitchboy')