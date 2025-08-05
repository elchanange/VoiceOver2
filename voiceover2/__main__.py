"""Command line interface for VoiceOver2."""

from __future__ import annotations

import argparse
from pathlib import Path

from .beep import text_to_beep


def main(argv: list[str] | None = None) -> Path:
    parser = argparse.ArgumentParser(description="Generate a beep-based voiceover")
    parser.add_argument("text", help="Text to speak")
    parser.add_argument("-o", "--output", default="output.wav", help="Output WAV file")
    parser.add_argument("-f", "--frequency", type=float, default=1000.0, help="Frequency of beeps in Hz")
    parser.add_argument("-d", "--duration", type=float, default=0.1, help="Duration of each character in seconds")
    args = parser.parse_args(argv)
    return text_to_beep(args.text, args.output, frequency=args.frequency, char_duration=args.duration)


if __name__ == "__main__":
    main()
