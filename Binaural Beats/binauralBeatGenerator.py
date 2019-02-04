from AccelBrainBeat.brainbeat.binaural_beat import BinauralBeat

def main():

    brain_beat = BinauralBeat()

    f1, f2 = input("What frequencies would you like? ").split()
    timer = int(input("How long would you like to listen? "))
    brain_beat.play_beat(
        frequencys=(f1, f2),
        play_time= timer,
        volume=0.1)

main()
