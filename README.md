# Title: Suitability Analysis of Potential Solar Power Farms in Saudi Arabia

| By MUHAMMAD AREEB|
|---------------------------------------------------------------------------------|
| Bachelors of Science in Geographic Information Systems & Technology |
| University of Arizona |
| Course: GIST 498 |
| [officialareeb@outlook.com](mailto:officialareeb@outlook.com) |

### Paper:
[Link to Paper](./SUITABILITY%20ANALYSIS%20OF%20POTENTIAL%20SOLAR%20POWER%20FARMS%20IN%20SAUDI%20ARABIA%20Final%20Draft%204.pdf)


### Storymap:
[Story Map](https://storymaps.arcgis.com/stories/33ddeebd0eaa4903b57454396c3f6cf4)

## SUMMARY

### Description:

This study aims to address the geographical issue of finding the best solar power plant/farm regions in the western provinces of Saudi Arabia. For this, 6 different parameters are being assessed, namely Solar Radiation (PVOUT), Temperature, Distance to Roads, Distance to Transmission Lines, Slope, and Aspect. These are combined with a restriction/constraints layer to create the final output.

### Data Sources:

| **Parameter**                  | **Data Source**                                                              |
|--------------------------------|------------------------------------------------------------------------------|
| Solar PV (Photovoltaic Potential) | [Global Solar Atlas](https://globalsolaratlas.info/download?c=21.575719,31.289063,5)                                                           |
| Temperature                    | [Open-Meteo](https://open-meteo.com/en/docs/historical-weather-api#hourly=&daily=temperature_2m_max,temperature_2m_min,temperature_2m_mean,daylight_duration,sunshine_duration)                                                                   |
| Proximity to Roads             | [MapCruzin](https://mapcruzin.com)                                                                    |
| Proximity to Existing Electric Grid | Offshore Wind Energy Potential Around the East Coast of the Red Sea, KSA  |
| Elevation                      | [USGS EarthExplorer](https://www.usgs.gov/coastal-changes-and-impacts/gmted2010)                                                          |
| Slope                          | [USGS EarthExplorer](https://www.usgs.gov/coastal-changes-and-impacts/gmted2010 ), derived from elevation data                              |
| Aspect                         | [USGS EarthExplorer](https://www.usgs.gov/coastal-changes-and-impacts/gmted2010 ), derived from elevation data                              |

### Methods:

This project aims to conduct a suitability analysis to identify optimal locations for photovoltaic (PV) farms in the western region of Saudi Arabia using the Analytic Hierarchy Process (AHP) and Weighted Overlay algorithms. Six parameters—solar PV potential, temperature, proximity to roads, proximity to the electric grid, elevation, slope, and aspect—are analyzed and ranked on a scale from 1 (least suitable) to 10 (most suitable).

Key datasets include solar PV potential metrics like PVOUT, which is reclassified for suitability analysis, and temperature data interpolated into rasters using Inverse Distance Weighting (IDW). Proximity to infrastructure is calculated using Euclidean distance rasters for road networks and manually georeferenced data for the electric grid. Elevation, slope, and aspect are derived from digital elevation models, with slopes and southern-facing aspects preferred for maximizing solar efficiency.

AHP is employed to assign relative weights to parameters through pairwise comparisons, forming a normalized matrix to prioritize criteria. Constraints, such as urban landscapes, water resources, and dense vegetation, are mapped using Landsat 8 imagery and deep learning models, generating a restricted layer for excluded regions.

The study provides a multi-criteria decision analysis (MCDA) workflow to produce a final suitability map ranking areas from 1 to 10. This analysis supports the strategic planning of PV farm installations in Saudi Arabia, leveraging renewable energy potential while minimizing environmental and infrastructural conflicts.

## Results and Conclusions:

### Suitability Map:

![Suitability Map](./AHP%20Weighted%20Overlay.png)

### Best Suitability Map:

![Best Suitability Map](./Best%20Suitability%20Analysis%20AHP.png)

Looking at the final suitability map, it can be inferred that the best areas for setting up large scale solar plant facilities lie primarily in the northwestern region of Saudi Arabia, with a plentiful regions in the southwest as well.

Assuming only 10% of this area is committed to solar power production, about 10 GW of power can be produced in this region, which is about 87.6 TWh (Terawatt hour) units of energy which is about 90% of the energy consumed in the western provinces of KSA.
