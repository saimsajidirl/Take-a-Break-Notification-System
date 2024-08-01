import time
from winotify import Notification,audio

 
noti=Notification(app_id="Hey Saim",

                  title="Take A Break",

                  msg="If You Are A Good Boy Then Take A 20 Minutes Break",

                  icon=r"E:\Python\Python Projects\Take a Break Notifcation System\gojo.png"
#for location you have to use the one where  you download it and keeping the code
                  )

noti.add_actions(label="Ok")

noti.set_audio(audio.Default,loop=False)

noti.show()