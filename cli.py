import argparse
import json

from chord_bpm_detector.analyze import analyze_audio
from chord_bpm_detector.viz import plot_analysis
from chord_bpm_detector.loader import load_audio

def main():
  parser = argparse.ArgumentParser(description="BPM and chord detection from audio")
  parser.add_argument("audio", help="route to the file")
  parser.add_argument("--plot", metavar="PNG", help="save plot here")
  parser.add_argument("--json", action="store_true", help="JSON export")
  args = parser.parse_args()

  data = analyze_audio(args.audio)
  if args.json:
    print(json.dumps(data, indent=2))
  else:
    for key, value in data.items():
      print(key, value)

  if args.plot is not None:
    y,sr = load_audio(args.audio)
    plot_analysis(y,sr,data,save_path=args.plot)
    print("Plot saved in ", args.plot)

if __name__ == "__main__":
  main()