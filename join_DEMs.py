import arcpy 

# Merge the rasters
arcpy.management.MosaicToNewRaster(
    input_rasters="10n030e_20101117_gmted_med075.tif;30n030e_20101117_gmted_med075.tif",
    output_location=r"C:\Users\areeb\Documents\GIST 498\Saudi Elevation\Saudi Solar Proper\Saudi Solar Proper.gdb",
    raster_dataset_name_with_extension="Saudi_DEM",
    coordinate_system_for_the_raster='GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]',
    pixel_type="16_BIT_UNSIGNED",
    cellsize=None,
    number_of_bands=1,
    mosaic_method="LAST",
    mosaic_colormap_mode="FIRST"
)

# Extract by layer to clip the raster to the Saudi borders.
with arcpy.EnvManager(scratchWorkspace=r"C:\Users\areeb\Documents\GIST 498\Saudi Elevation\Saudi Solar Proper\Saudi Solar Proper.gdb"):
    out_raster = arcpy.sa.ExtractByMask(
        in_raster="Saudi_DEM",
        in_mask_data="saudi_shp",
        extraction_area="INSIDE",
        analysis_extent='34.5727645185677 16.3709577486013 55.6375647381222 32.1213479617391 GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]'
    )
    out_raster.save(r"C:\Users\areeb\Documents\GIST 498\Saudi Elevation\Saudi Solar Proper\Saudi Solar Proper.gdb\Saudi_DEM_Clip")

# Reclassifying based on VALUE from 1-9.
# with arcpy.EnvManager(scratchWorkspace=r"C:\Users\areeb\Documents\GIST 498\Saudi Elevation\Saudi Solar Proper\Saudi Solar Proper.gdb"):
#     out_raster = arcpy.sa.Reclassify(
#         in_raster="Saudi_DEM_Clip",
#         reclass_field="Value",
#         remap="0 298 1;298 596 2;596 894 3;894 1192 4;1192 1490 5;1490 1788 6;1788 2086 7;2086 2384 8;2384 2682 9;2682 2980 10",
#         missing_values="DATA"
#     )
#     out_raster.save(r"C:\Users\areeb\Documents\GIST 498\Saudi Elevation\Saudi Solar Proper\Saudi Solar Proper.gdb\Saudi_DEM_Reclass")

with arcpy.EnvManager(outputCoordinateSystem='GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]', cellSize=0.0025, scratchWorkspace=r"C:\Users\areeb\Documents\GIST 498\Saudi Elevation\Saudi Solar Proper\Saudi Solar Proper.gdb"):
    out_raster = arcpy.sa.Reclassify(
        in_raster="Saudi_DEM_Clip",
        reclass_field="Value",
        remap="0 298 1;298 596 2;596 894 3;894 1192 4;1192 1490 5;1490 1788 6;1788 2086 7;2086 2384 8;2384 2682 9;2682 2980 10",
        missing_values="DATA"
    )
    out_raster.save(r"C:\Users\areeb\Documents\GIST 498\Saudi Elevation\Saudi Solar Proper\Saudi Solar Proper.gdb\Saudi_DEM_Reclass")