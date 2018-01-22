#The module retorn a message according to its age
def messageAccordingTheAge(age):
    if age in range(0,13):
        return "child"
    elif age in range(13, 18):
        return "teenager"
    elif age in range(18, 30):
        return "young"
    else:
        return "adult"
