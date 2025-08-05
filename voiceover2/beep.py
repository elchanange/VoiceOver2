"""Basic text-to-speech by converting characters to sine wave beeps.

This module provides a very small offline text-to-speech implementation that
converts each alphabetical character into a short sine-wave tone. It avoids any
external dependencies and produces a valid WAV file.
"""

from __future__ import annotations

import math
import struct
import wave
from pathlib import Path
from typing import Iterable

SAMPLE_RATE = 44_100
AMP = 16_000  # amplitude for the sine wave
DEFAULT_FREQ = 1_000  # Hz
CHAR_DURATION = 0.1  # seconds


def _sine_wave(frequency: float, frames: int) -> Iterable[bytes]:
    """Generate frames for a sine wave of ``frequency`` and ``frames`` length."""
    for i in range(frames):
        value = int(AMP * math.sin(2 * math.pi * frequency * (i / SAMPLE_RATE)))
        yield struct.pack("<h", value)


def _silence(frames: int) -> Iterable[bytes]:
    """Generate silent frames."""
    silence = struct.pack("<h", 0)
    for _ in range(frames):
        yield silence


def text_to_beep(text: str, output: str | Path, *,
                 frequency: float = DEFAULT_FREQ,
                 char_duration: float = CHAR_DURATION) -> Path:
    """Convert ``text`` to a WAV file of beeps.

    Parameters
    ----------
    text:
        The text to speak. Each alphabetical character produces a short beep;
        other characters produce silence of equal length.
    output:
        Path to the output WAV file.
    frequency:
        Frequency of the beep in Hertz. Default is 1000 Hz.
    char_duration:
        Duration of each character in seconds. Default is 0.1s.

    Returns
    -------
    Path
        Path to the generated WAV file.
    """
    output_path = Path(output)
    frames_per_char = int(char_duration * SAMPLE_RATE)
    with wave.open(str(output_path), "w") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)  # 16-bit
        wav.setframerate(SAMPLE_RATE)
        for char in text:
            if char.isalpha():
                frames = _sine_wave(frequency, frames_per_char)
            else:
                frames = _silence(frames_per_char)
            for frame in frames:
                wav.writeframes(frame)
    return output_path
