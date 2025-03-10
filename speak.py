import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

print("Enter the word you want to speak ")
s = input()
speaker.Speak(s)
