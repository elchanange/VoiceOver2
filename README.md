# VoiceOver2

VoiceOver2 is a minimal demonstration project that turns text into a series of
sine-wave beeps and saves the result as a WAV file. It is intentionally simple
and runs entirely offline, using only Python's standard library.

## Features

* Offline generation of WAV files from text
* Command-line interface via `python -m voiceover2` or the `voiceover2` script

## Usage

```bash
python -m voiceover2 "Hello world" -o hello.wav
```

The above command creates `hello.wav` containing short beeps representing each
alphabetical character in the input text.

## Development

Run the test suite with:

```bash
pytest
```
