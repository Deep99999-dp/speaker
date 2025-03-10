import win32com.client as win

speaker = win.Dispatch("SAPI.SpVoice")

names_list = ["Deep", "Dp", "Deep9999"]

for name in names_list:
    print("Shoutout to " + name)
    shoutout = f"Shoutout to {name}"
    speaker.Speak(shoutout)

print("Shoutout to all the guys")
speaker.Speak("Shoutout to all the guys")
