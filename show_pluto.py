import planetmapper
from planetmapper.kernel_downloader import download_urls
import matplotlib.pyplot as plt
import numpy as np

download_urls(
    'https://naif.jpl.nasa.gov/pub/naif/generic_kernels/lsk/',
    'https://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/',
    # 'https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/de430.bsp',
    'https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/satellites/plu060.bsp',
    # 'https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/satellites/jup365.bsp',
    # 'https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/satellites/sat441.bsp',
    # 'https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/satellites/ura111.bsp',
    # 'https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/satellites/nep097.bsp',
    # 'https://naif.jpl.nasa.gov/pub/naif/JWST/kernels/spk/',
)


body = planetmapper.Body('pluto', '2023-07-01')
# body.add_other_bodies_of_interest('charon')

body.plot_wireframe_radec(show=True,indicate_equator=True)

# fig, [ax_radec, ax_km] = plt.subplots(nrows=2, figsize=(6, 8), dpi=200)
#
# dates = ['2023-07-01 00:00', '2023-07-02 01:00', '2023-07-03 02:00']
# colors = ['r', 'g', 'b']
#
# for date, c in zip(dates, colors):
#     body = planetmapper.Body('pluto', date)
#     # body.add_other_bodies_of_interest('charon')
#     body.plot_wireframe_radec(ax_radec, color=c)
#     body.plot_wireframe_km(ax_km, color=c)
#
#     # Plot some blank data with the correct colour to go on the legend
#     ax_radec.scatter(np.nan, np.nan, color=c, label=date)
#
# ax_radec.legend(loc='upper left')
#
# ax_radec.set_title('Position in the sky')
# ax_km.set_title('Position relative to Jupiter')
#
# fig.tight_layout()
# plt.show()
    
