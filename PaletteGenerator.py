"""
A simple extension that creates color swatches to use as a palette
"""

import inkex
from inkex import Rectangle, Circle
import random


class PaletteGeneratorExtension(inkex.EffectExtension):
    def add_arguments(self, pars):
        pars.add_argument("--n_colors", type=int,
                          help="The number of colors to generate", default=4)
        pars.add_argument("--tab", type=str,
                          help="The selected tab", default="Options")
        pars.add_argument("--palette_type", type=str,
                          help="The type of palette to generate", default="sequential")
        pars.add_argument("--shape", type=str,
                          help="The shape of the swatches", default="square")
        pars.add_argument("--size", type=float,
                          help="The size of the swatches", default=10)

    def effect(self):
        n_colors = self.options.n_colors
        # Create n_colors swatches
        for i in range(n_colors):
            x = -10  # Put the swatches outside the canvas
            y = self.options.size * i * 1.5

            if self.options.shape == "square":
                swatch = Rectangle(x=f'{x - self.options.size/2}', y=f'{y}',
                                   width=f'{self.options.size}', height=f'{self.options.size}')
            elif self.options.shape == "circle":
                swatch = Circle(cx=f'{x}', cy=f'{
                                y + self.options.size/2}', r=f'{self.options.size/2}')
            else:
                raise ValueError("Invalid shape")

            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            swatch.style = f"fill:rgb({red},{green},{blue});stroke:none"
            layer = self.svg.get_current_layer()

            layer.append(swatch)


if __name__ == '__main__':
    PaletteGeneratorExtension().run()
