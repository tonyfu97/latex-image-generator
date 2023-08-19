#!/usr/bin/env python3

from matplotlib import rc
import matplotlib.pyplot as plt
import sys

def render_latex_formula(formula, file_name='formula.png', font_size=60, dpi=300):
    # Enable LaTeX rendering
    rc('text', usetex=True)
    rc('font', family='serif')

    fig, ax = plt.subplots(figsize=(1, 0.2), dpi=dpi)
    ax.text(0.5, 0.5, f'${formula}$', size=font_size, ha='center', va='center')
    plt.axis('off')

    # Adjust figure size to match text
    fig.canvas.draw()
    bounding_box = ax.get_window_extent(fig.canvas.get_renderer()).transformed(fig.dpi_scale_trans.inverted())
    fig.set_size_inches(bounding_box.width, bounding_box.height)

    plt.savefig(file_name, bbox_inches='tight', pad_inches=0, dpi=dpi)
    plt.close()
    print(f'Image saved as {file_name} in the current directory.')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: latex_img "\\LaTeX formula" [output_filename.png]')
        print('Please provide a LaTeX formula as an argument.')
    else:
        formula = sys.argv[1]
        filename = sys.argv[2] if len(sys.argv) > 2 else 'formula.png'
        render_latex_formula(formula, filename)
