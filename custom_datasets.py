from utils import open_file
import numpy as np

palette = None

'''
Make sure to comment and uncomment the correct dataset both in the CONFIG,
and the loader

When using only the SWIR dataset, then you can also change the rgb_bands command
for a false color composite (may not work properly on Linux, at least for me)
'''
CUSTOM_DATASETS_CONFIG = {
         'BLOKK90': {
            'img': 'mosaic_VNIR_b90.hdr',
#            'img': 'mosaic_SWIR_b90_resampled_cubic.hdr',
#            'img': 'mosaic_VNIR_and_SWIR_b90.hdr',
            'gt': 'GT_Blokk90_Poly_Raster.tif',
            'download': False,
            'loader': lambda folder: BLOKK90_loader(folder)
            }
    }

def BLOKK90_loader(folder):
        img = open_file(folder + 'mosaic_VNIR_b90.hdr')[:,:,:-2]
#        img = open_file(folder + 'mosaic_SWIR_b90_resampled_cubic.hdr')[:,:,:-2]
#        img = open_file(folder + 'mosaic_VNIR_and_SWIR_b90.hdr')[:,:,:-2]
        gt = open_file(folder + 'GT_Blokk90_Poly_Raster.tif')
        gt = gt.astype('uint8')
#       RGB bands for VNIR
        rgb_bands = (80, 49, 25)
#       False color composite for SWIR
#        rgb_bands = (220, 130, 50)

        label_values = ["Unclassified",
                        "RedRoof_Strong",
                        "RedRoof_Brown",
                        "Asphalt_Light",
                        "Solar_Panel",
                        "Red_Roof_Tiles",
                        "Black_Rooftop",
                        "Playground_Dark_Blue",
                        "Playground_Light_Blue",
                        "Grass_Healthy",
                        "Roundabout",
                        "Asphalt_Road",
                        "Grass_Unhealthy",
                        "Black_Roof_bd1",
                        "Black_Roof_bd2",
                        "Trees",
                        "Red_Stone",
                        "Asphalt_Darker",
                        "Black_Roof_bd4",
                        "Black_Roof_bd5",
                        "Black_Roof_bd3"]
        ignored_labels = [0]
        return img, gt, rgb_bands, ignored_labels, label_values, palette

