from cartopy.io import shapereader
import geopandas
import matplotlib.pyplot as plt
import cartopy.crs as ccrs


def plot_french_map(locations=None, title=None, color='red'):
    # get natural earth data (http://www.naturalearthdata.com/)

    # get country borders
    resolution = '10m'
    category = 'cultural'
    name = 'admin_0_countries'

    shpfilename = shapereader.natural_earth(resolution, category, name)

    # read the shapefile using geopandas
    df = geopandas.read_file(shpfilename)

    # restricting to France
    poly = df.loc[df['ADMIN'] == 'France']['geometry'].values[0]

    ax = plt.axes(projection=ccrs.PlateCarree())

    ax.add_geometries(poly, crs=ccrs.PlateCarree(), facecolor='none',
                      edgecolor='0.5')

    # ax.set_extent([5, 16, 46.5, 56], crs=ccrs.PlateCarree())
    plt.title(title)
    ax = plt.axes(projection=ccrs.PlateCarree())

    ax.add_geometries(poly, crs=ccrs.PlateCarree(), facecolor='none',
                      edgecolor='0.5')

    ax.set_ylim(40, 53)
    ax.set_xlim(-5, 10)

    # Add accidents coordinates
    if isinstance(locations, list):
        color = 'red'
        for location in locations:
            location.plot(ax=ax, color=color)
            color = 'blue'
    elif locations is not None:
        locations.plot(ax=ax, color='red')


if __name__ == "__main__":
    plot_french_map()
    plt.show()