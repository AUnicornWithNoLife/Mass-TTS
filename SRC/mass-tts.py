from gtts import gTTS

print("LOCATION: ")
loc = input()

da = open(loc, "r")
data = da.read().split(",")
da.close()

config = ""

try:
    conf = open(loc + ".conf", "r")
    config = conf.read().split(",")
except:
    print("no config file")

_ = loc.rfind("/")
save = loc[0:_] + "/save/"

print (save)

i = 0

for dat in data:
    tts = gTTS(dat)
    tts.save(save + str(i) + ".mp3")

    i += 1