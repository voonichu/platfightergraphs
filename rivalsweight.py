import matplotlib.pyplot as plt
import numpy as np
import json
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# import the data
with open("characterdata.json", "r", encoding="utf-8") as file:
    data = json.load(file)


def main():
    # list of characters for data
    characters = ['gouie', 'slade', 'la reina', 'galvan', 'absa', 'olympia', 'etalus', 'forsburn', 'orcane', 'loxodont', 'clairen', 'maypul', 'fleet', 'kragg', 'wrastor', 'ranno', 'zetterburn']

    # load character data by name from json file
    x = [data[c]['weight'] for c in characters]
    y = [data[c]['hitstun gravity'] for c in characters]
    image_paths = [
        'stock_icons/RoA2_Gouie_Stock.png',
        'stock_icons/RoA2_Slade_Stock.png',
        'stock_icons/RoA2_La_Reina_Stock.png',
        'stock_icons/RoA2_Galvan_Stock.png',
        'stock_icons/RoA2_Absa_Stock.png',
        'stock_icons/RoA2_Olympia_Stock.png',
        'stock_icons/RoA2_Etalus_Stock.png',
        'stock_icons/RoA2_Forsburn_Stock.png',
        'stock_icons/RoA2_Orcane_Stock.png',
        'stock_icons/RoA2_Loxodont_Stock.png',
        'stock_icons/RoA2_Clairen_Stock.png',
        'stock_icons/RoA2_Maypul_Stock.png',
        'stock_icons/RoA2_Fleet_Stock.png',
        'stock_icons/RoA2_Kragg_Stock.png',
        'stock_icons/RoA2_Wrastor_Stock.png',
        'stock_icons/RoA2_Ranno_Stock.png',
        'stock_icons/RoA2_Zetterburn_Stock.png',
    ]

    # stylize background
    plt.style.use('Solarize_Light2')
    
    fig, ax = plt.subplots()
    imscatter(x, y, image_paths, ax=ax)
    # label setting
    ax.set_ylabel('hitstun gravity')
    ax.set_xlabel('weight')
    # axis setting 
    ax.set(xlim=(60, 120), xticks=np.arange(60, 130, 10),
           ylim=(0.5, 1.9), yticks=np.arange(0.5, 2.0, 0.1))
    plt.show()


def imscatter(x, y, images, ax=None, zoom=1, size_px=25):
    if ax is None:
        ax = plt.gca()

    x, y = np.atleast_1d(x, y)
    # import every image individually 
    artists = []
    for x0, y0, img in zip(x, y, images):
        try:
            img = plt.imread(img)
        except TypeError:
            # Likely already an array...
            pass
        # the dragdown stock icons were all different sizes so this makes them uniform
        h, w = img.shape[:2]
        zoom = size_px / max(h, w)    
        
        im = OffsetImage(img, zoom=zoom)
        ab = AnnotationBbox(im, (x0, y0), xycoords='data', frameon=False)
        artists.append(ax.add_artist(ab))

    ax.update_datalim(np.column_stack([x, y]))
    ax.autoscale()
    return artists


main()