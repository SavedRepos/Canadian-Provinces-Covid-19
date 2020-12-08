#!/usr/bin/env python3
#https://github.com/CSSEGISandData/COVID-19.git
#csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv
#csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv
#csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv
#csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv

#UID	iso2	iso3	code3	FIPS	Admin2	Province_State	Country_Region	Lat	Long_	Combined_Key	1/22/20	1/23/20	1/24/20	1/25/20	1/26/20	1/27/20	1/28/20	1/29/20	1/30/20	1/31/20	2002-01-20	2002-02-20	2002-03-20	2002-04-20	2002-05-20	2002-06-20	2002-07-20	2002-08-20	2002-09-20	2002-10-20	2002-11-20	2002-12-20	2/13/20	2/14/20	2/15/20	2/16/20	2/17/20	2/18/20	2/19/20	2/20/20	2/21/20	2/22/20	2/23/20	2/24/20	2/25/20	2/26/20	2/27/20	2/28/20	2/29/20	2003-01-20	2003-02-20	2003-03-20	2003-04-20	2003-05-20	2003-06-20	2003-07-20	2003-08-20	2003-09-20	2003-10-20	2003-11-20	2003-12-20	3/13/20	3/14/20	3/15/20	3/16/20	3/17/20	3/18/20	3/19/20	3/20/20	3/21/20	3/22/20	3/23/20	3/24/20	3/25/20	3/26/20	3/27/20	3/28/20	3/29/20	3/30/20	3/31/20	2004-01-20	2004-02-20	2004-03-20	2004-04-20	2004-05-20	2004-06-20	2004-07-20	2004-08-20	2004-09-20	2004-10-20	2004-11-20	2004-12-20	4/13/20	4/14/20	4/15/20	4/16/20	4/17/20	4/18/20	4/19/20	4/20/20	4/21/20	4/22/20	4/23/20	4/24/20	4/25/20	4/26/20	4/27/20	4/28/20	4/29/20	4/30/20	2005-01-20	2005-02-20	2005-03-20	2005-04-20	2005-05-20	2005-06-20	2005-07-20	2005-08-20	2005-09-20	2005-10-20	2005-11-20	2005-12-20	5/13/20	5/14/20	5/15/20	5/16/20	5/17/20	5/18/20	5/19/20	5/20/20	5/21/20	5/22/20	5/23/20	5/24/20	5/25/20	5/26/20	5/27/20	5/28/20	5/29/20	5/30/20	5/31/20	2006-01-20	2006-02-20	2006-03-20	2006-04-20	2006-05-20	2006-06-20	2006-07-20	2006-08-20	2006-09-20	2006-10-20	2006-11-20	2006-12-20	6/13/20	6/14/20	6/15/20	6/16/20	6/17/20	6/18/20	6/19/20	6/20/20	6/21/20	6/22/20	6/23/20	6/24/20	6/25/20	6/26/20	6/27/20	6/28/20	6/29/20	6/30/20	2007-01-20	2007-02-20	2007-03-20	2007-04-20	2007-05-20	2007-06-20	2007-07-20	2007-08-20	2007-09-20	2007-10-20	2007-11-20	2007-12-20	7/13/20	7/14/20	7/15/20	7/16/20	7/17/20	7/18/20	7/19/20	7/20/20	7/21/20	7/22/20	7/23/20	7/24/20	7/25/20	7/26/20	7/27/20	7/28/20	7/29/20	7/30/20	7/31/20	2008-01-20	2008-02-20	2008-03-20	2008-04-20	2008-05-20	2008-06-20	2008-07-20	2008-08-20	2008-09-20	2008-10-20	2008-11-20	2008-12-20	8/13/20	8/14/20	8/15/20	8/16/20	8/17/20	8/18/20	8/19/20	8/20/20	8/21/20	8/22/20	8/23/20	8/24/20	8/25/20	8/26/20	8/27/20	8/28/20	8/29/20	8/30/20	8/31/20	2009-01-20	2009-02-20	2009-03-20	2009-04-20	2009-05-20	2009-06-20	2009-07-20	2009-08-20	2009-09-20	2009-10-20	2009-11-20	2009-12-20	9/13/20	9/14/20	9/15/20	9/16/20	9/17/20	9/18/20	9/19/20	9/20/20	9/21/20	9/22/20	9/23/20	9/24/20	9/25/20	9/26/20	9/27/20	9/28/20	9/29/20	9/30/20	2010-01-20	2010-02-20	2010-03-20	2010-04-20	2010-05-20	2010-06-20	2010-07-20	2010-08-20	2010-09-20	2010-10-20	2010-11-20	2010-12-20	10/13/20	10/14/20	10/15/20	10/16/20	10/17/20	10/18/20	10/19/20	10/20/20	10/21/20	10/22/20	10/23/20	10/24/20	10/25/20	10/26/20	10/27/20	10/28/20	10/29/20	10/30/20	10/31/20	2011-01-20	2011-02-20	2011-03-20	2011-04-20	2011-05-20	2011-06-20	2011-07-20	2011-08-20	2011-09-20	2011-10-20	2011-11-20	2011-12-20	11/13/20	11/14/20	11/15/20	11/16/20	11/17/20	11/18/20	11/19/20	11/20/20	11/21/20	11/22/20	11/23/20	11/24/20	11/25/20	11/26/20	11/27/20	11/28/20	11/29/20	11/30/20	2012-01-20	2012-02-20	2012-03-20
                                               #Province/State	Country/Region	Lat	Long	1/22/20	1/23/20	1/24/20	1/25/20	1/26/20	1/27/20	1/28/20	1/29/20	1/30/20	1/31/20	2002-01-20	2002-02-20	2002-03-20	2002-04-20	2002-05-20	2002-06-20	2002-07-20	2002-08-20	2002-09-20	2002-10-20	2002-11-20	2002-12-20	2/13/20	2/14/20	2/15/20	2/16/20	2/17/20	2/18/20	2/19/20	2/20/20	2/21/20	2/22/20	2/23/20	2/24/20	2/25/20	2/26/20	2/27/20	2/28/20	2/29/20	2003-01-20	2003-02-20	2003-03-20	2003-04-20	2003-05-20	2003-06-20	2003-07-20	2003-08-20	2003-09-20	2003-10-20	2003-11-20	2003-12-20	3/13/20	3/14/20	3/15/20	3/16/20	3/17/20	3/18/20	3/19/20	3/20/20	3/21/20	3/22/20	3/23/20	3/24/20	3/25/20	3/26/20	3/27/20	3/28/20	3/29/20	3/30/20	3/31/20	2004-01-20	2004-02-20	2004-03-20	2004-04-20	2004-05-20	2004-06-20	2004-07-20	2004-08-20	2004-09-20	2004-10-20	2004-11-20	2004-12-20	4/13/20	4/14/20	4/15/20	4/16/20	4/17/20	4/18/20	4/19/20	4/20/20	4/21/20	4/22/20	4/23/20	4/24/20	4/25/20	4/26/20	4/27/20	4/28/20	4/29/20	4/30/20	2005-01-20	2005-02-20	2005-03-20	2005-04-20	2005-05-20	2005-06-20	2005-07-20	2005-08-20	2005-09-20	2005-10-20	2005-11-20	2005-12-20	5/13/20	5/14/20	5/15/20	5/16/20	5/17/20	5/18/20	5/19/20	5/20/20	5/21/20	5/22/20	5/23/20	5/24/20	5/25/20	5/26/20	5/27/20	5/28/20	5/29/20	5/30/20	5/31/20	2006-01-20	2006-02-20	2006-03-20	2006-04-20	2006-05-20	2006-06-20	2006-07-20	2006-08-20	2006-09-20	2006-10-20	2006-11-20	2006-12-20	6/13/20	6/14/20	6/15/20	6/16/20	6/17/20	6/18/20	6/19/20	6/20/20	6/21/20	6/22/20	6/23/20	6/24/20	6/25/20	6/26/20	6/27/20	6/28/20	6/29/20	6/30/20	2007-01-20	2007-02-20	2007-03-20	2007-04-20	2007-05-20	2007-06-20	2007-07-20	2007-08-20	2007-09-20	2007-10-20	2007-11-20	2007-12-20	7/13/20	7/14/20	7/15/20	7/16/20	7/17/20	7/18/20	7/19/20	7/20/20	7/21/20	7/22/20	7/23/20	7/24/20	7/25/20	7/26/20	7/27/20	7/28/20	7/29/20	7/30/20	7/31/20	2008-01-20	2008-02-20	2008-03-20	2008-04-20	2008-05-20	2008-06-20	2008-07-20	2008-08-20	2008-09-20	2008-10-20	2008-11-20	2008-12-20	8/13/20	8/14/20	8/15/20	8/16/20	8/17/20	8/18/20	8/19/20	8/20/20	8/21/20	8/22/20	8/23/20	8/24/20	8/25/20	8/26/20	8/27/20	8/28/20	8/29/20	8/30/20	8/31/20	2009-01-20	2009-02-20	2009-03-20	2009-04-20	2009-05-20	2009-06-20	2009-07-20	2009-08-20	2009-09-20	2009-10-20	2009-11-20	2009-12-20	9/13/20	9/14/20	9/15/20	9/16/20	9/17/20	9/18/20	9/19/20	9/20/20	9/21/20	9/22/20	9/23/20	9/24/20	9/25/20	9/26/20	9/27/20	9/28/20	9/29/20	9/30/20	2010-01-20	2010-02-20	2010-03-20	2010-04-20	2010-05-20	2010-06-20	2010-07-20	2010-08-20	2010-09-20	2010-10-20	2010-11-20	2010-12-20	10/13/20	10/14/20	10/15/20	10/16/20	10/17/20	10/18/20	10/19/20	10/20/20	10/21/20	10/22/20	10/23/20	10/24/20	10/25/20	10/26/20	10/27/20	10/28/20	10/29/20	10/30/20	10/31/20	2011-01-20	2011-02-20	2011-03-20	2011-04-20	2011-05-20	2011-06-20	2011-07-20	2011-08-20	2011-09-20	2011-10-20	2011-11-20	2011-12-20	11/13/20	11/14/20	11/15/20	11/16/20	11/17/20	11/18/20	11/19/20	11/20/20	11/21/20	11/22/20	11/23/20	11/24/20	11/25/20	11/26/20	11/27/20	11/28/20	11/29/20	11/30/20	2012-01-20	2012-02-20	2012-03-20
#
# C19Web.py
#
# C19Web is a web application written in Python and using
# Streamlit as the presentation method and Streamlit Share
# make it generally available.
#
# The structure of this program has all the Streamlit code 
# in the main program because of Streamlit requirements.
#

from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil import parser
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
import streamlit as st
import urllib

# from C19WebModel import *
# from C19WebPlotting import *


from streamlit.elements.doc_string import CONFUSING_STREAMLIT_MODULES

st.set_page_config(
    page_title="B.C. Covid-19",
    page_icon="😷",
    layout="centered",
    initial_sidebar_state="auto",
)

# 'country', 'province', 'lastDate'     
# 'latitude', 'longitude'    
# 'dates'        
# 'confirmed', 'confirmedNew', 'confirmedNewMean'
# 'deaths', 'deathsNew', 'deathsNewMean'
index_url_csv  = 'https://jpaulhart.github.io/Index.csv'

# "Date", "Region", "New_Tests", "Total_Tests", "Positivity", "Turn_Around"
bc_tests_url = 'http://www.bccdc.ca/Health-Info-Site/Documents/BCCDC_COVID19_Dashboard_Lab_Information.csv'
# "Reported_Date","HA","Sex","Age_Group","Classification_Reported"
bc_cases_url = 'http://www.bccdc.ca/Health-Info-Site/Documents/BCCDC_COVID19_Dashboard_Case_Details.csv'

base_url = 'https://jpaulhart.github.io'
# #######################################################################################
# Read data and cache
# #######################################################################################

@st.cache
def read_csv(url):
    fixed_url = url.replace(' ', '%20')
    return pd.read_csv(fixed_url)

# #######################################################################################
# Setup global data
# #######################################################################################

dfIndex = read_csv(index_url_csv)
allCountries = dfIndex['Country'].tolist()
countries = []

provinces = ('British Columbia',
             'Alberta',
             'Saskatchewan',
             'Manitoba',
             'Ontario',
             'Quebec',
             'Newfoundland and Labrador',
             'New Brunswick',
             'Nova Scotia'
             'Prince Edward Island'
            )
selected_provinces = ('British Columbia') 

time_frames = ('All', '1 Week', '2 Weeks', '3 Weeks', '1 Month', '3 Months', '6 Months')
time_frame = 'All'

last_date = ''
dfCanada = pd.read_csv(urllib.parse.urljoin(base_url, 'Canada.csv'))

dfLast = dfCanada.tail(n=1)
last_date = dfLast['Date'].values[0]

dfFirst = dfCanada.head(n=1)
first_date = dfFirst['Date'].values[0]

world_pop = read_csv(urllib.parse.urljoin(base_url, 'WorldPop.csv'))

# Provincial Population
prov_pop = {
    'BC' : 5.071,
    'AL' : 4.371,
    'SA' : 1.174,
    'MB' : 1.369,
    'ON' : 14.57,
    'PQ' : 8.485,
    'NL' : 0.552,
    'NB' : 0.777,
    'NS' : 0.971,
    'PE' : 0.156,
}

# #######################################################################################
# Select days based time_frame
# #######################################################################################

def df_days(dfProv, last_date, time_frame):
    global first_date

    first_date = parser.parse('2020-03-01')
    in_date = parser.parse(last_date)

    if time_frame == time_frames[1]:
        date_after = in_date - relativedelta(weeks=1)
    elif time_frame == time_frames[2]:
        date_after = in_date - relativedelta(weeks=2)
    elif time_frame == time_frames[3]:
        date_after = in_date - relativedelta(weeks=3)
    elif time_frame == time_frames[4]:
        date_after = in_date - relativedelta(months=1)
    elif time_frame == time_frames[5]:
        date_after = in_date - relativedelta(months=3)
    elif time_frame == time_frames[6]:
        date_after = in_date - relativedelta(months=6)
    elif time_frame == time_frames[0]:
        date_after = first_date
    else:
        date_after = first_date

    out_date = date_after.strftime("%Y-%m-%d")
    first_date = out_date
    dfOut = dfProv[dfProv['Date'] >= out_date]
    return dfOut

# #######################################################################################
# Setup page
# #######################################################################################

def stSetup():
    global selected_provinces
    global time_frame
    global first_date
    global last_date
    global countries
    global countries2

    st.header('Covid-19 Tracker')

    # Setup sidebar
    st.sidebar.markdown('## Options')
    st.sidebar.markdown('### Select Time Frame')
    time_frame = st.sidebar.selectbox('Select analysis time period:', time_frames)

    # if st.sidebar.button('add a new group'):
    #     st.sidebar.write('Write a group')

    st.sidebar.markdown('### Select Countries (1)')
    countries = st.sidebar.multiselect('Select countries:', 
                                        allCountries,
                                        ['Canada', 'Italy', 'Spain', 'Portugal', 'Thailand']
                                      )

    st.sidebar.markdown('### Select Countries (2)')
    countries2 = st.sidebar.multiselect('Select countries:', 
                                        allCountries,
                                        ['Morocco','Tunisia','Oman']
                                      )

    st.sidebar.markdown('----')
    st.sidebar.markdown('### About')
    st.sidebar.markdown('The majority of the data used in this application is sourced from the [Johns Hopkins University Center for Systems Science and Engineering (JHU CCSE)](https://data.humdata.org/dataset/novel-coronavirus-2019-ncov-cases).')    
    st.sidebar.markdown('The testing data for British Columbia is from the [BC Centre for Disease Control](http://www.bccdc.ca/Health-Info-Site/Documents/BCCDC_COVID19_Dashboard_Lab_Information.csv)')
    
    return

# #######################################################################################
# Section 1
#     C19BCTable - Table with number of tests, %age of those positive, turn around time
#     Graph of a) confirmed new b) deaths new
#     Graph of province compare
#     Province Summary:
#      - new cases, deaths last 7 days
#      - new tests, positivity last 7 days
#      - Graphs
#      - Sidebar select provinces
# #######################################################################################

def stSection1():
    global last_date

    prov = 'British Columbia'
    
    file_name = f'{prov}.csv'.replace(' ', '%20')
    dfProv = pd.read_csv(urllib.parse.urljoin(base_url, file_name))
    
    dfTests = pd.read_csv(bc_tests_url)
    dfTable = dfTests.copy() 
    dfTable['New_Positives'] = dfTable['New_Tests'] * (dfTable['Positivity'] / 100)

    dfTable = dfTable.groupby('Date').agg({'New_Tests': 'sum', 'New_Positives': 'sum', 'Positivity': 'mean', 'Turn_Around': 'mean'})
    dfTable = dfTable.sort_values('Date', ascending=False)
    dfTable = pd.merge(dfProv, dfTable, on=['Date'], how='outer')
    dfTable = dfTable.replace(np.nan,0)
    print(dfTable.tail(n=10))
    #dfLast = dfProv.tail(n=1)
    #last_date = dfLast['Date'].values[0]
    dfProv = df_days(dfProv, last_date, time_frame)
    dfProv = dfProv.sort_values(by=['Date'], ascending=True)

    st.markdown(f'###### Report Date: {last_date}')
    st.markdown(f'###### Reporting time frame: {time_frame} ({first_date} - {last_date})')
    st.markdown('## ')

    #st.markdown('----')
    st.markdown(f'#### {prov}')
    #st.markdown(f'###### Report Date: {last_date}')

    col1, col2 = st.beta_columns(2)
    #with col1:
    stProvTable(dfTable)
    st.markdown('## ')
    #with col2:
    stProvGraphs(dfProv)

#-----------------------------------------------------------------------------
# Provincial Stats Graph for specified time span
#-----------------------------------------------------------------------------

def stProvGraphs(dfProv):

    #-------------------------------------------------------------------------
    # Create Confirmed New Plot
    #-------------------------------------------------------------------------
    col1, col2 = st.beta_columns(2)
    with col1:

        #st.markdown(f'##### New Cases')

        fig1 = plt.figure(1, figsize=(8, 5))

        plt.title('New Cases - Smoothed', fontsize='large')
        plt.xlabel="Date"
        plt.ylabel="Number"

        #plt.xticks(rotation=45)
        ax = plt.gca()
        ax.xaxis.set_major_locator(ticker.MultipleLocator(100))

        plt.plot(dfProv['Date'], dfProv['ConfirmedNewMean'], label='New Cases - Smoothed')
        plt.grid(b=True, which='major')
        st.pyplot(fig1)
        plt.close()

    #-------------------------------------------------------------------------
    # Create Deaths New Plot
    #-------------------------------------------------------------------------

    with col2:
        #st.markdown(f'##### New Deaths')
        
        fig2 = plt.figure(2, figsize=(8, 5))

        plt.title('New Deaths - Smoothed')
        plt.xlabel="Date"
        plt.ylabel="Number"

        #plt.xticks(rotation=45)
        ax = plt.gca()
        ax.xaxis.set_major_locator(ticker.MultipleLocator(100))

        plt.plot(dfProv['Date'], dfProv['DeathsNewMean'], label='New Deaths - Smoothed')
        plt.grid(b=True, which='major')
        st.pyplot(fig2)
        plt.close()
        #if prov == 'British Columbia':
        #stBCCases(dfProv)

#-----------------------------------------------------------------------------
# Provincial Stats Table
#-----------------------------------------------------------------------------

def stProvTable(dfProv):
    
        #st.markdown(f'##### 10 Days')

        # Table of details for last week 
        cases_data = '<div style="font-size: small">\n'
        cases_data += '<table border=1>\n'
        cases_data += '<tr><th> </th><th colspan=2 style="text-align:center">Cases</th><th colspan=2 style="text-align:center">Deaths</th><th colspan=4 style="text-align:center">Testing</th></tr>\n'
        cases_data += '<tr><th>Date</th><th>Total</th><th>New</th><th>Total</th><th>New</th><th>New</th><th>Positives</th><th>% Pos.</th><th>Hours</th></tr>\n'
        #cases_data += '| :----- | ----------: | --------: | -----------: | ---------: |\n'
        row_count = 0
        dfSorted = dfProv.sort_values(['Date'], ascending=False)
        for index, row in dfSorted.iterrows():
            date = row['Date'] 
            confirmed = row['Confirmed']
            confirmed = "{:,}".format(confirmed)
            confirmedNew = row['ConfirmedNew']
            confirmedNew = "{:,}".format(confirmedNew)
            deaths = row['Deaths']
            deaths = "{:,}".format(deaths)
            deathsNew = row['DeathsNew']
            deathsNew = "{:,}".format(deathsNew)
            #New_Tests  New_Positives  Positivity  Turn_Around
            newTests = row['New_Tests']
            newTests = "{:,.0f}".format(newTests)
            newPositives = row['New_Positives']
            newPositives = "{:,.0f}".format(newPositives)
            positivity = row['Positivity']
            positivity = "{:.1f}".format(positivity)
            turnAround = row['Turn_Around']
            turnAround = "{:.1f}".format(turnAround)
            cases_data += f'<tr>'
            cases_data += f'<td nowrap>{date}</td><td style="text-align:right">{confirmed}</td>'
            cases_data += f'<td style="text-align:right">{confirmedNew}</td>'
            cases_data += f'<td style="text-align:right">{deaths}</td>'
            cases_data += f'<td style="text-align:right">{deathsNew}</td>'
            cases_data += f'<td style="text-align:right">{newTests}</td>'
            cases_data += f'<td style="text-align:right">{newPositives}</td>'
            cases_data += f'<td style="text-align:right">{positivity}%</td>'
            cases_data += f'<td style="text-align:right">{turnAround}</td>'
            cases_data += f'</tr>' + '\n'
            row_count += 1
            if row_count >= 10:
                cases_data += '</table>\n'
                cases_data += '</div>\n'
                break
        st.markdown(cases_data, unsafe_allow_html=True)

#-----------------------------------------------------------------------------
# Provincial Stats Table
#-----------------------------------------------------------------------------

def stBCCases(dfProv):
    # "Reported_Date","HA","Sex","Age_Group","Classification_Reported"
    case_Url = 'http://www.bccdc.ca/Health-Info-Site/Documents/BCCDC_COVID19_Dashboard_Case_Details.csv'
    dfCase = pd.read_csv(case_Url) 
    dfCase = df_days(dfCase, last_date, time_frame)
    dfCase['Year_Month'] = dfCase['Reported_Date'].map(lambda reported_date: reported_date[0:7])
    dfCase = dfCase.sort_values(by=['Reported_Date', 'HA'])

    dfCrosstab = pd.crosstab(index=dfCase['Reported_Date'], columns=dfCase['HA'])
    dfCrosstab.plot(kind='barh')
    reportTitle = 'BC Lab Diagnosed Cases by Health Authority'
    plt.title(reportTitle, fontsize=10)
    fig3 = plt.figure(3, figsize=(15, 6))
    st.pyplot(fig3)

# #######################################################################################
# Section 2
#     Provincial compare
# #######################################################################################

def stSection2():
    global last_date

    st.markdown('----')
    st.markdown(f"#### Compare Canada's Largest Provinces")
    #st.markdown(f'###### Report Date: {last_date}')
    dfal = pd.read_csv(urllib.parse.urljoin(base_url, 'Alberta.csv'))
    dfal = df_days(dfal, last_date, time_frame)
    dfal['ConfirmedNewPer1M'] = dfal['ConfirmedNewMean'] / prov_pop['AL']
    dfal['DeathsNewPer1M']    = dfal['DeathsNewMean'] / prov_pop['AL']
    dfbc = pd.read_csv(urllib.parse.urljoin(base_url, 'British%20Columbia.csv'))
    dfbc = df_days(dfbc, last_date, time_frame)
    dfbc['ConfirmedNewPer1M'] = dfbc['ConfirmedNewMean'] / prov_pop['AL']
    dfbc['DeathsNewPer1M']    = dfbc['DeathsNewMean'] / prov_pop['AL']
    dfon = pd.read_csv(urllib.parse.urljoin(base_url, 'Ontario.csv'))
    dfon = df_days(dfon, last_date, time_frame)
    dfon['ConfirmedNewPer1M'] = dfon['ConfirmedNewMean'] / prov_pop['AL']
    dfon['DeathsNewPer1M']    = dfon['DeathsNewMean'] / prov_pop['AL']
    dfqu = pd.read_csv(urllib.parse.urljoin(base_url, 'Quebec.csv'))
    dfqu = df_days(dfqu, last_date, time_frame)
    dfqu['ConfirmedNewPer1M'] = dfqu['ConfirmedNewMean'] / prov_pop['AL']
    dfqu['DeathsNewPer1M']    = dfqu['DeathsNewMean'] / prov_pop['AL']
    #print(dfal.info())

    col1, col2 = st.beta_columns(2)

    #-------------------------------------------------------------------------
    # Create Confirmed New Plot
    #-------------------------------------------------------------------------

    with col1:

        #st.markdown(f'##### New Cases')

        fig1 = plt.figure(1, figsize=(8, 5))

        plt.title('Confirmed New Cases per Million', fontsize='large')
        plt.xlabel="Date"
        plt.ylabel="Number"

        #plt.xticks(rotation=45)
        ax = plt.gca()
        ax.xaxis.set_major_locator(ticker.MultipleLocator(75))

        #plt.plot(dfPr['date'], dfProv['confirmedNewMean'], label='New Cases - Smoothed')
        plt.plot(dfal['Date'], dfal['ConfirmedNewPer1M'], label='Alberta')
        plt.plot(dfbc['Date'], dfbc['ConfirmedNewPer1M'], label='British Columbia')
        plt.plot(dfon['Date'], dfon['ConfirmedNewPer1M'], label='Ontario')
        plt.plot(dfqu['Date'], dfqu['ConfirmedNewPer1M'], label='Quebec')

        # Add a legend
        plt.legend(['Alberta', 'British Columbia', 'Ontario', 'Quebec'])
        plt.grid(b=True, which='major')
        st.pyplot(fig1)
        plt.close()

    #-------------------------------------------------------------------------
    # Create Deaths New Plot
    #-------------------------------------------------------------------------

    with col2:

        #st.markdown(f'##### New Deaths')

        fig1 = plt.figure(1, figsize=(8, 5))

        plt.title('New Deaths per Million', fontsize='large')
        plt.xlabel="Date"
        plt.ylabel="Number"

        #plt.xticks(rotation=45)
        ax = plt.gca()
        ax.xaxis.set_major_locator(ticker.MultipleLocator(75))

        #plt.plot(dfPr['date'], dfProv['confirmedNewMean'], label='New Cases - Smoothed')
        plt.plot(dfal['Date'], dfal['DeathsNewPer1M'], label='Alberta')
        plt.plot(dfbc['Date'], dfbc['DeathsNewPer1M'], label='British Columbia')
        plt.plot(dfon['Date'], dfon['DeathsNewPer1M'], label='Ontario')
        plt.plot(dfqu['Date'], dfqu['DeathsNewPer1M'], label='Quebec')

        # Add a legend
        plt.legend(['Alberta', 'British Columbia', 'Ontario', 'Quebec'])
        plt.grid(b=True, which='major')
        st.pyplot(fig1)
        plt.close()

# #######################################################################################
# Section 3
#     United States
# #######################################################################################

def stSection3():
    global last_date

    st.markdown('----')
    st.markdown(f'#### United States')

    col1, col2 = st.beta_columns(2)

    with col1:

        fig1 = plt.figure(1, figsize=(8, 5))

        plt.title('New Confirmed Cases', fontsize='large')
        plt.xlabel="Date"
        plt.ylabel="Number"

        #plt.xticks(rotation=45)
        ax = plt.gca()
        ax.xaxis.set_major_locator(ticker.MultipleLocator(75))

        dfCountry = dfIndex[dfIndex['Country'] == 'US']
        file_name = dfCountry['File'].values[0]
        file_url = urllib.parse.urljoin(base_url, file_name)
        df = pd.read_csv(file_url)
        plt.plot(df['Date'], df['ConfirmedNewMean'], label=df['Country'])

        # Add a legend
        # plt.legend(countries)
        plt.grid(b=True, which='major')
        st.pyplot(fig1)
        plt.close()

    with col2:
        fig1 = plt.figure(1, figsize=(8, 5))

        plt.title('New Deaths', fontsize='large')
        plt.xlabel="Date"
        plt.ylabel="Number"

        #plt.xticks(rotation=45)
        ax = plt.gca()
        ax.xaxis.set_major_locator(ticker.MultipleLocator(75))

        for cty in countries:
            dfCountry = dfIndex[dfIndex['Country'] == 'US']
            file_name = dfCountry['File'].values[0]
            file_url = urllib.parse.urljoin(base_url, file_name)
            df = pd.read_csv(file_url)
            plt.plot(df['Date'], df['DeathsNewMean'], label=df['Country'])

        # Add a legend
        # plt.legend(countries)
        plt.grid(b=True, which='major')
        st.pyplot(fig1)
        plt.close()

# #######################################################################################
# Section 4
#     Other Countries
# #######################################################################################

def stSection4():
    global last_date

    st.markdown('----')
    st.markdown(f'#### Countries (1)')

    col1, col2 = st.beta_columns(2)

    with col1:

        fig1 = plt.figure(1, figsize=(8, 5))

        plt.title('New Confirmed Cases', fontsize='large')
        plt.xlabel="Date"
        plt.ylabel="Number"

        #plt.xticks(rotation=45)
        ax = plt.gca()
        ax.xaxis.set_major_locator(ticker.MultipleLocator(75))

        for cty in countries:
            dfCountry = dfIndex[dfIndex['Country'] == cty]
            file_name = dfCountry['File'].values[0]
            file_url = urllib.parse.urljoin(base_url, file_name)
            df = pd.read_csv(file_url)
            plt.plot(df['Date'], df['ConfirmedNewMean'], label=df['Country'])

        # Add a legend
        plt.legend(countries)
        plt.grid(b=True, which='major')
        st.pyplot(fig1)
        plt.close()

    with col2:
        fig1 = plt.figure(1, figsize=(8, 5))

        plt.title('New Deaths', fontsize='large')
        plt.xlabel="Date"
        plt.ylabel="Number"

        #plt.xticks(rotation=45)
        ax = plt.gca()
        ax.xaxis.set_major_locator(ticker.MultipleLocator(75))

        for cty in countries:
            dfCountry = dfIndex[dfIndex['Country'] == cty]
            file_name = dfCountry['File'].values[0]
            file_url = urllib.parse.urljoin(base_url, file_name)
            df = pd.read_csv(file_url)
            plt.plot(df['Date'], df['DeathsNewMean'], label=df['Country'])

        # Add a legend
        plt.legend(countries)
        plt.grid(b=True, which='major')
        st.pyplot(fig1)
        plt.close()

# #######################################################################################
# Section 5
#     Other Countries
# #######################################################################################

def stSection5():
    global last_date

    st.markdown('----')
    st.markdown(f'#### Countries (2)')

    col1, col2 = st.beta_columns(2)

    with col1:

        fig1 = plt.figure(1, figsize=(8, 5))

        plt.title('New Confirmed Cases', fontsize='large')
        plt.xlabel="Date"
        plt.ylabel="Number"

        #plt.xticks(rotation=45)
        ax = plt.gca()
        ax.xaxis.set_major_locator(ticker.MultipleLocator(75))

        for cty in countries2:
            dfCountry = dfIndex[dfIndex['Country'] == cty]
            file_name = dfCountry['File'].values[0]
            file_url = urllib.parse.urljoin(base_url, file_name)
            df = pd.read_csv(file_url)
            plt.plot(df['Date'], df['ConfirmedNewMean'], label=df['Country'])

        # Add a legend
        plt.legend(countries2)
        plt.grid(b=True, which='major')
        st.pyplot(fig1)
        plt.close()

    with col2:
        fig1 = plt.figure(1, figsize=(8, 5))

        plt.title('New Deaths', fontsize='large')
        plt.xlabel="Date"
        plt.ylabel="Number"

        #plt.xticks(rotation=45)
        ax = plt.gca()
        ax.xaxis.set_major_locator(ticker.MultipleLocator(75))

        for cty in countries2:
            dfCountry = dfIndex[dfIndex['Country'] == cty]
            file_name = dfCountry['File'].values[0]
            file_url = urllib.parse.urljoin(base_url, file_name)
            df = pd.read_csv(file_url)
            plt.plot(df['Date'], df['DeathsNewMean'], label=df['Country'])

        # Add a legend
        plt.legend(countries2)
        plt.grid(b=True, which='major')
        st.pyplot(fig1)
        plt.close()

#-------------------------------------------------------------------------
# Get dataframe for a country
#-------------------------------------------------------------------------

def getDfForCountry(countryName):
    global last_date

    country = countryName.replace(' ', '%20')
    df = pd.read_csv(urllib.parse.urljoin(base_url, f'{country}.csv'))
    df = df_days(df, last_date, time_frame)

    return df

# ############################################################################
# Entry Point
# ############################################################################

def main():
    stSetup()
    stSection1()
    stSection2()
    stSection3()
    stSection4()
    stSection5()

if __name__ == '__main__':
    main()

