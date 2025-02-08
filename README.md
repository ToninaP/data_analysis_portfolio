# data_analysis_portfolio
Welcome to my Data Analysis portfolio! 

Junior researcher @ Cultural data analysis lab (2020-2024), preparing for graduation from a PhD program at Tallinn University. https://cudan.tlu.ee/team/antonina/

This set of projects is created to demonstrate my analytic and technical skills. The portfolio is being regularly updated, so new things are going to be added.


# data
All data used in the project was open access. I am grateful to institutions allowing the enthusiasts like me to play with their datasets.
| Musem name | Country| Data acquisition method | Link |
|----------|----------|----------|----------|
| MET| USA| Open access| https://github.com/metmuseum/openaccess|
| Reina Sofia| Spain| Scraped| https://www.museoreinasofia.es/en/collection/|
| Tate| England| Open access| https://github.com/tategallery/collection|
|Pomidou|France|API|https://www.centrepompidou.fr/en/collections|
|Kiasma|Finland|API|https://www.kansallisgalleria.fi/api/swagger/|
|The Queensland Art Gallery / Gallery of Modern Art (QAGOMA)|Australia|Open Access|https://www.data.qld.gov.au/dataset/qagoma-collection|
|MOT|Japan|API|https://museumcollection.tokyo/en/developer/|
|MOMA|USA|Open access|https://github.com/MuseumofModernArt/collection|
|Whitney|USA|Open access|https://github.com/whitneymuseum/open-access/blob/main/artists.csv|
|SMK|Denmark|API|https://www.smk.dk/en/article/smk-api/|
|National Gallery of Art|USA|Open access|https://github.com/NationalGalleryOfArt/opendata|

# data preparation

Objective: Prepare data for analysis by keeping only relevant data, unifying data types, and variable names. Dealing with missing data and outliers. Extracting numerical data from strings, and unifying string data for classification and visualization. 

Tools: Python (Pandas)

Skills:

Procedure:
https://github.com/ToninaP/data_analysis_portfolio/blob/main/data_cleaning.ipynb

Data dictionary: https://github.com/ToninaP/data_analysis_portfolio/blob/main/data/data_dictionary

# analysis

## exploratory analysis project - comparison across multiple datasets

Objective: to find what kind of art one museum collects, and to determine if the museum supports the development of arts.

Tools: Tableau

Skills: aggregation calculations, changing data types, dual axis charts, filtering, dashboards, stories.

Story about Queensland Art museum:

https://public.tableau.com/app/profile/antonina.korepanova/viz/queensland_exploratory/Story1?publish=yes

Interactive dashboard to explore data of all 11 museums:

https://public.tableau.com/app/profile/antonina.korepanova/viz/museums_17380294803550/Dashboard1?publish=yes


## exploratory analysis project - comparison across multiple datasets

Objective: To find collecting patterns of 11 contemporary arts museums. Media persentage of artworks, aquisition sources, geographical distributions, gender and artists age distributions are the main focal points for the exploration.

Tools: Python (Pandas, Plotly)

Skills: data visualization (subplots, bar charts, pie charts, area charts, histograms, geographical mapping); writing modules, functions, loops, conditionals, lists, dictionaries.

Procedure and results
https://github.com/ToninaP/data_analysis_portfolio/blob/main/exploratory_analysis.ipynb

## descriptive analysis

## statistical analysis

# published articles based on work with data

## Quantifying Collection Lag in European Modern and Contemporary Art Museums
Co-authors: Mar Canet Sola, Ksenia Mukhina, Max Schich.

Objective: To create a measure to calculate the level of support an art museum can give contemporary artists. Find a way to identify museums focused on art presevation vs. creation.

Tools: Python (Pandas, Plotly), Git. 

Skills: Data scraping, data cleaning and preparing for analysis, working with dictionaries, loops, and conditions. Creating subplots, bar charts, area charts, violin plots, and heatmaps. Collaboration using the version control system. 

Publication: https://cudan-museums.github.io/

## Leveraging Existing Online Platforms to Support Knowledge Exchange Between Visual Arts Educators
Co-authors: Cosmo Ligthfoot, Kai Pata.

Objective: Use open access platforms to store research findings with affordances to use the system as a collaborative knowledge co-creation tool.

Tools: Google Sheets, Observable

Skills: data connection, data visualization.

Publication: https://link.springer.com/chapter/10.1007/978-3-031-61678-5_11

Data visualization: https://observablehq.com/d/0feef33fe6bb1305

