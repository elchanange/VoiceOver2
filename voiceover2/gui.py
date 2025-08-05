from __future__ import annotations

import tkinter as tk
from tkinter import filedialog, messagebox

from .beep import text_to_beep


class VoiceOverGUI:
    """Simple graphical interface for the VoiceOver2 beep generator."""

    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        master.title("VoiceOver2")

        tk.Label(master, text="Text:").grid(row=0, column=0, sticky="e")
        self.text_entry = tk.Entry(master, width=40)
        self.text_entry.grid(row=0, column=1, columnspan=2, pady=5)

        tk.Label(master, text="Output:").grid(row=1, column=0, sticky="e")
        self.output_var = tk.StringVar(value="output.wav")
        tk.Entry(master, textvariable=self.output_var, width=30).grid(row=1, column=1, pady=5)
        tk.Button(master, text="Browse", command=self._browse_file).grid(row=1, column=2, padx=5)

        tk.Label(master, text="Frequency (Hz):").grid(row=2, column=0, sticky="e")
        self.freq_var = tk.StringVar(value="1000")
        tk.Entry(master, textvariable=self.freq_var, width=10).grid(row=2, column=1, sticky="w", pady=5)

        tk.Label(master, text="Duration (s):").grid(row=3, column=0, sticky="e")
        self.dur_var = tk.StringVar(value="0.1")
        tk.Entry(master, textvariable=self.dur_var, width=10).grid(row=3, column=1, sticky="w", pady=5)

        tk.Button(master, text="Generate", command=self._generate).grid(row=4, column=1, pady=10)

    def _browse_file(self) -> None:
        filename = filedialog.asksaveasfilename(
            defaultextension=".wav", filetypes=[("WAV files", "*.wav")]
        )
        if filename:
            self.output_var.set(filename)

    def _generate(self) -> None:
        text = self.text_entry.get()
        output = self.output_var.get()
        try:
            freq = float(self.freq_var.get())
            duration = float(self.dur_var.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Frequency and duration must be numbers.")
            return
        try:
            path = text_to_beep(text, output, frequency=freq, char_duration=duration)
            messagebox.showinfo("Success", f"Saved to {path}")
        except Exception as exc:  # pragma: no cover - GUI-only error path
            messagebox.showerror("Error", str(exc))


def main() -> None:
    root = tk.Tk()
    VoiceOverGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
