import sys
import ffmpeg
import traceback

## Input formats:
## audioClipUtil.py in.ext out.ext startTime(seconds)
## audioClipUtil.py in.ext out.ext startTime(seconds) duration(seconds)
def main(argv: list = sys.argv) -> None:
    if len(argv) < 4 or len(argv) > 6:
        sys.exit("Invalid number of parameters.")
    
    try:
        duration = int(argv[4]) if len(argv) == 5 else 30

        ffmpeg.input(argv[1], ss=argv[3], t=duration).audio.output(argv[2]).run()

        print(f"Audio file clip saved at {argv[2]}")
    except Exception:
        traceback.print_exc()

if __name__ == "__main__":
    main()
