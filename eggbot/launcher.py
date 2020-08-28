import speech, owobot, subprocess, os, signal
running = False
while True:
  desired_func = input('Type 1 for speech and 2 for normal op. To run 2 async, type 3. To kill 3, type 4. >>')
  if desired_func == '1':
    speech.speech()
  if desired_func == '2':
    owobot.owobot()
  if desired_func == '3':
    proc = subprocess.Popen('python3 eggbot/owobot.py', stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
    running = True
  if desired_func == '4':
    if running == True:
      os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
      print('Killed process.')
    else:
      print("Realbot wasn't running!")

    
