# BU Spark! - Boston Flood Zone Project

## Project mission

The mission of the project is to analyze the flood zones in Boston, and the predicted flood zones in Boston in the next few years. Given that flood zones have increased in Boston, compare them with the implemented green infrastructure to analyze how well they perform to prevent flooding, and in which area the green infrastructure needs to be developed further.

## Steps to duplicate the project

Details of the base project can be found in [Document.ipynb](https://github.com/harrisonahn1129/Spark-Sustainability/blob/main/Document.ipynb)

### Step one: Pull the data from the data sources.
- Pull the data of flood zones first in json file
- Pull the data of hydrography
- Using the geopandas library, overlap the visualization of flood zone and hydrography
- Analyze how hydrography is developed around the flood zone

### Step two: reshape the data in json format.
- From the json data, retrieve fields of the data (types of sewer systems)
- With the fields, make a query to retrieve the metadata

### Step three: Plot the data to compare and analyze
- Using the geopandas library, plot the metadata of the flood zones of different years
- Plot the metadata of the hydrography on top of the flood zone plot with different color
- Analyze how well they overlap each other to understand how well the sewer system is implemented in/around the flood zone

## Extension of the project for students

This is an opportunity to get creative with additional data that you think would tell an interesting story. This extension should be something your team finds compelling. You will create a mid-semester proposal for this extension project that the client will approve. 

### Suggested Extension Topic (from Councilor Bok): 
communities that have been affected by flooding the most and whether the city has allocated resources to these areas (census data)
- How to leverage existing plans for construction and maintenance to improve areas that experience flooding
- Finding the intersection points of planned construction, why you have sidewalks opened for construction already, let’s improve the sidewalk infrastructure for flooding 

### Extension Data Sets
#### [Canopy cover change data](https://data.boston.gov/dataset/canopy-change-assessment-2019-land-cover) (Analyze Boston) (request CSV)
- Can also be part of the extension project - around the flood zones, how green areas are decreasing or increasing over time (If increase = good, if decrease = bad)

#### [311 sidewalk data](https://data.boston.gov/dataset?q=sidewalk&sort=score+desc%2C+metadata_modified+desc) (sidewalk centerline/inventory)
- Need to distinguish whether the damage is from flooding 
- When there’s sidewalks, usually has sewer system under it - comparing that with the flood zones, any sidewalk that has sewer system underneath it and if that's an area that flood zones have overlap - maybe under the sidewalk/road, we can develop sewer system infrastructure/to improve the sewer system 

#### [Capital project budgets for next five years](https://data.boston.gov/dataset/capital-budget) (it says from FY23-27, but only appears 23)
- Specify by kind of development
- Capital budget for sidewalk repair/or related to sidewalk, look at roads damaged by flood and repairing those
- Distinguish it so it only has road or sidewalk 
