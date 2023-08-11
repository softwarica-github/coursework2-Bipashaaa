import tkinter as tk
from tkinter import messagebox
import re
import unittest


class IntrusionDetectionSystem:
    def __init__(self):
        self.pattern = re.compile(r'\battack\b', re.IGNORECASE)

    def detect_intrusion(self, input_text):
        return self.pattern.search(input_text) is not None


class IDSApp:
    def __init__(self, root, intrusion_detection):
        self.root = root
        self.root.title("Intrusion Detection System")

        self.label = tk.Label(root, text="Enter your text:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button = tk.Button(root, text="Check", command=self.check_intrusion)
        self.button.pack()

        self.intrusion_detection = intrusion_detection

    def check_intrusion(self):
        input_text = self.entry.get()
        if self.intrusion_detection.detect_intrusion(input_text):
            messagebox.showwarning("Intrusion Detected", "Potential intrusion detected!")
        else:
            messagebox.showinfo("No Intrusion", "No intrusion detected.")


class TestIntrusionDetectionSystem(unittest.TestCase):
    def setUp(self):
        self.ids = IntrusionDetectionSystem()

    def test_detect_intrusion_positive(self):
        text = "This is an attack!"
        result = self.ids.detect_intrusion(text)
        self.assertTrue(result)

    def test_detect_intrusion_negative(self):
        text = "No attack here."
        result = self.ids.detect_intrusion(text)
        self.assertFalse(result)


if __name__ == "__main__":
    intrusion_detection = IntrusionDetectionSystem()

    root = tk.Tk()
    app = IDSApp(root, intrusion_detection)
    root.mainloop()

    unittest.main()
