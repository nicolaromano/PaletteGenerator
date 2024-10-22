"""
A simple extension that creates color swatches to use as a palette
"""

import inkex

class PaletteGeneratorExtension(inkex.EffectExtension):    
    def add_arguments(self, pars):
        pars.add_argument("--n_colors", type=int, help="The number of colors to generate", default=4)
        pars.add_argument("--tab", type=str, help="The selected tab", default="Options")

    def effect(self):
        n_colors = self.options.n_colors
        self.msg("Test!")

if __name__ == '__main__':
    PaletteGeneratorExtension().run()
