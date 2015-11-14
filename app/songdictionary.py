# Use a switch statement to correlate that value to our code
def getSentValue(value):
        if    ((-1.0 <= value) & (value < -0.8)):
                sentValue = -1.0
        elif  ((-0.8 <= value) & (value < -0.6)):
                sentValue = -0.8
        elif  ((-0.6 <= value) & (value < -0.4)):
                sentValue = -0.6
        elif  ((-0.4 <= value) & (value < -0.2)):
                sentValue = -0.4
        elif  ((-0.2 <= value) & (value <  0.0)):
                sentValue = -0.2
        elif  (( 0.0 <= value) & (value <  0.2)):
                sentValue =  0.0
        elif  (( 0.2 <= value) & (value <  0.4)):
                sentValue =  0.2
        elif  (( 0.4 <= value) & (value <  0.6)):
                sentValue =  0.4
        elif  (( 0.6 <= value) & (value <  0.8)):
                sentValue =  0.6
        else:
                sentValue =  1.0

        return sentValue

# Returns url of song with 
def getSongUrlFromValue(value):
        sentValue = getSentValue(value)
        songdisc = {-1.0 : 'saddest song', 
                -0.8 : 'sadder song',
                -0.6 : 'saddish song',
                -0.4 : 'saddy song',
                -0.2 : 'sad song', 
                 0.0 : 'okay song', 
                 0.2 : 'okayish song',
                 0.4 : 'goodish song',
                 0.6 : 'good song',
                 0.8 : 'happiysh song',
                 1.0 : 'https://songanalysis.blob.core.windows.net/songs/10_happy'} 
        return songdisc[sentValue]