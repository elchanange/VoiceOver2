import sys
import wave
from pathlib import Path

# Ensure package root is importable even when PYTHONSAFEPATH is enabled
sys.path.append(str(Path(__file__).resolve().parents[1]))

from voiceover2 import text_to_beep


def test_text_to_beep(tmp_path: Path) -> None:
    output = tmp_path / "voice.wav"
    text_to_beep("abc", output)
    assert output.exists()
    with wave.open(str(output), "rb") as wav:
        assert wav.getnchannels() == 1
        assert wav.getframerate() == 44_100
        frames = wav.getnframes()
        # Expect 3 characters * 0.1s * 44100 frames ~= 13230
        assert 13_000 < frames < 14_000
