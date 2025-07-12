# gui/components/voice_waveform.py

import tkinter as tk
import random
import math

class WaveformWidget(tk.Canvas):
    def __init__(self, master, name="default", **kwargs):
        super().__init__(master, bg="black", width=300, height=100, **kwargs)
        self.name = name
        self.particles = []
        self.animate = True

        self._create_particles()
        self.animate_particles()

    def _create_particles(self):
        for _ in range(30):
            x = random.randint(0, 300)
            y = random.randint(0, 100)
            radius = random.randint(2, 5)
            dx = random.uniform(-1.5, 1.5)
            dy = random.uniform(-1.5, 1.5)

            color = "#ffdd01" if self.name == "wavey" else "#00ffff"

            particle = {
                "id": self.create_oval(x, y, x+radius, y+radius, fill=color, outline=""),
                "x": x,
                "y": y,
                "dx": dx,
                "dy": dy,
                "r": radius
            }
            self.particles.append(particle)

    def animate_particles(self):
        if not self.animate:
            return

        for p in self.particles:
            # Update position
            p["x"] += p["dx"]
            p["y"] += p["dy"]

            # Bounce off walls
            if p["x"] <= 0 or p["x"] + p["r"] >= self.winfo_width():
                p["dx"] *= -1
            if p["y"] <= 0 or p["y"] + p["r"] >= self.winfo_height():
                p["dy"] *= -1

            self.coords(
                p["id"],
                p["x"],
                p["y"],
                p["x"] + p["r"],
                p["y"] + p["r"]
            )

        self.after(30, self.animate_particles)

    def stop_wave(self):
        self.animate = False

    def start_wave(self):
        if not self.animate:
            self.animate = True
            self.animate_particles()
