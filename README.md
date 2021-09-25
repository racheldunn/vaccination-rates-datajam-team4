# Vaccination rates and Socioeconomic Status in BC


## Project statement

The goal of this project is to discover if there is a link between vaccination rates and a health region’s socioeconomic status, and if so, whether the socioeconomic status is a driver of vaccination rates.
https://docs.google.com/document/d/1w1clbNlTbzOZwbzDYIOxFFG1UZpAFjclrAZhDFelYCY/

There are three main objectives in this project:
1. Study vaccination rates
2. Study socioeconomic factors 
3. Study the relationship between vaccination rate and low socioeconomic status

## Project team members

Team lead: Rachel Dunn

Mentor: Karab Sze

Team Members:  

- Sangita Mitra 
- Erin Gill
- Melisa Fuentes
- Grace Liu
- Evelyn Liu
- Shrey Grover
- Jeet
<br />

## Data Collection and Preprocessing

## Data Source: 

1. [BC Community Health Data] (http://communityhealth.phsa.ca/CHSAHealthProfiles)
2. COVID-19 Public Health dataset by health authority

## Data Wrangling:
Socioeconomic data were downloaded and formatted using the code in the following notebooks and scripts:
- notebooks/download_socioeco_scvs.ipynb
- notebooks/collate_socioeco_scvs.ipynb
- scripts/rename_socio_df_columns.py

Vaccination data were downloaded and formatted using the code in the following notebook:
- notebooks/vaccination-data-cleaning-exploration.ipynb

Merged both datasets based on the health authority code (4 digits)

## Exploratory Data Analysis (EDA)

1. Performed EDA for fetures related with  

i. Canadian Index of Multiple Deprivation (CIMD) such as situational vulnerability, ethnocultural composition, economic dependency and residential instability <br />
ii. Ethnic identity and language <br />
iii. Household size, detached housing and state of housing <br />
iv. Education and income <br />

2. Analyzed the correlation of features with vaccination rate and identify highly correlated fetures
3. Developed and evaluated a linear regression model with these features

## Project Description

We analyzed the relationahip between vaccination rates and socioeconomic status between 5 health authories in BC. They are -

1. Vancouver Coastal Health
2. Norther Health
3. Interior Health
4. Fraser Health
5. Island Health

## Major Findings 

1. Indigenous communities were negatively correlated with vaccination rates 
2. Percenatge of detached houses negatively correlated with vaccine coverage. 
3. Percentage of Filipino population positively correlated with vaccine coverage whereas percentage of Chinese population negatively correlated with vaccine coverage.
4. The biggest predictor of vaccine coverage is percenatge of population with less than high school education level.

## Discussions

1. Assist health authorities in understanding what factors are driving vaccination rates across subregions.
2. Potentially amend policies based on targeted socioeconomic metrics that correlate with vaccination hesitancy
3. Eventually, ensure vaccine inclusion amongst population of diverse demographics


## Vancouver Datajam 2021 Schedule:

### Main page: https://vancouverdatajam.ca/
#### Event format: 100% online

#### Important dates: 

|Date | Action item |
| - | - |
|Sep 13 - 17 |Participants are let in Discord, teams are formed|
|Sep 18 |[Workshop day!](https://www.vancouverdatajam.ca/workshops) Keynote: Making AI responsible with May Masoud|
|Sep 19 |Project statements are released|
|Sep 19-24 |Teams may work asynchronously (limited help desk support)|
|Sep 25 |Keynote talks, help desk support provided during the day, project submission deadline, career panel. See [speakers](https://www.vancouverdatajam.ca/speakers)|

#### Power up Saturday September 25 - suggested team schedule. All times in PDT

|Time| Action item|
| - | - |
|8:00 - 8:10| Land acknowledgement, opening remarks |
|8:10 - 8:40| Keynote: Role of Statistics in Data Science: Applications in Biomedical Sciences with Prof. Jemila Hamid | 
|8:40 - 9:10| Keynote: How to use the tools of data science to benefit Indigenous peoples and organizations  with Hannes Edinger |
|9:10 -  9:30| Keynote Q&A |
|9:30 | Help desk opens up, teams work on their project |
|9:30 - 10:00| Teams brainstorm tasks for the day|
|12:30 - 13:00| Team check in: share exploratory analysis results |
|15:30 - 16:00| Team check in: teams discuss presentation format and preliminary results|
|16:00 - 16:45| Teams prepare their 5-10 minute presentation, teams ensure all code is documented and stored in GitHub|
|17:00| Project video submission deadline|
|17:30 - 18:30| Project videos released on YouTube. Vote for your favourite team demo!| 
|18:30 - 20:00 | Career panel|
|20:00 - 20:30 | People's Choice Award presented. Closing remarks|
