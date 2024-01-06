import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def create_annotated_path_image(grid, path):
    nrows, ncols = len(grid), 5
    cell_size = 50  # Adjust cell size as needed
    img = Image.new('RGB', (ncols * cell_size, nrows * cell_size), color='white')
    draw = ImageDraw.Draw(img)

    # Use a default font, or replace with a specific font if available
    font = ImageFont.load_default()

    for i in range(nrows):
        for j in range(ncols):
            x, y = j * cell_size, i * cell_size
            text = grid[i][j]
            w, h = draw.textsize(text, font=font)

            # Check if the current position is part of the path
            if path[i][j] not in {'*', ' '}:
                draw.rectangle([x, y, x + cell_size, y + cell_size], fill='lightblue')

            # Draw the text in the center of the cell
            text_x = x + (cell_size - w) / 2
            text_y = y + (cell_size - h) / 2
            draw.text((text_x, text_y), text, fill='black', font=font)

    # Display the image
    plt.imshow(img)
    plt.axis('off')
    plt.show()

# Example usage
grid = [
    "222121221125545442551354433121526425256135462244521145435534754273766414422352566611173565254633655234633532614263351511443421253152344411142",
    "344142321144343113114443312252464244613133242216212561236744564126151267757561763515131375662365415443364352425141212343145112215215511141224",
    "441422133512325311441433351556523126645443151336244236622317413476361435642512671235371314132135121213141141656134432452434133111145144131412",
    "414111443322112341211443226663351133662251644146532727245365327154452744667325663152763177747141424455263212362141122662422552434353241423324",
    "411311212242124523143125243632315541642642262264136337334672477667475611146413273551112743164151522465563322461152132531334335133534542132132"
]
path = [
    "S>>>*****************************************************************************************************************************************",
    "***v*****************************************************************************************************************************************",
    "***v*****************************************************************************************************************************************",
    "***v>****************************************************************************************************************************************",
    "****v****************************************************************************************************************************************"
]

create_annotated_path_image(grid, path)
