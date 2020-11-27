#!/usr/bin/env python3

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

import csv
from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil import parser
import json
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import os
import pandas as pd
import streamlit as st
import urllib

from streamlit.elements.doc_string import CONFUSING_STREAMLIT_MODULES

# 'country', 'province', 'lastDate'     
# 'latitude', 'longitude'    
# 'dates'        
# 'confirmed', 'confirmedNew', 'confirmedNewMean'
# 'deaths', 'deathsNew', 'deathsNewMean'
index_url = 'https://jpaulhart.github.io/index.json'

# "Date", "Region", "New_Tests", "Total_Tests", "Positivity", "Turn_Around"
bc_tests_url = 'http://www.bccdc.ca/Health-Info-Site/Documents/BCCDC_COVID19_Dashboard_Lab_Information.csv'
# "Reported_Date","HA","Sex","Age_Group","Classification_Reported"
bc_cases_url = 'http://www.bccdc.ca/Health-Info-Site/Documents/BCCDC_COVID19_Dashboard_Case_Details.csv'

# province, lastDate, latitude, longitude,
# date[], confirmed[], confirmedNew[], confirmedNewMean[], deaths[], deathsNew[], deathsNewMean[]            
base_url = 'https://jpaulhart.github.io'

#-------------------------------------------------------------------------
# Contains a collection or group of countries in one plot 
#-------------------------------------------------------------------------

class Countries():
    def __init__(self, groupName, countryList = []):
        self.groupName = groupName
        self.countryList = countryList
    
#-------------------------------------------------------------------------
# Country class contains all the input data required to produce a plot
#-------------------------------------------------------------------------

class Country():
  def __init__(self, name):
    self.name = name

# #######################################################################################
# Load data
# #######################################################################################

dfIndex = pd.read_json(index_url)

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
    dfOut = dfProv[dfProv['date'] >= out_date]
    return dfOut

# #######################################################################################
# Setup page
# #######################################################################################

def stSetup():
    global selected_provinces
    global time_frame
    global last_date

    st.set_page_config(
        page_title="B.C. Covid-19",
        page_icon="😷",
        layout="centered",
        initial_sidebar_state="auto",
    )

    st.header('Covid-19 Tracker')
    # st.sidebar.subheader('Options')
    # selected_provinces = st.sidebar.multiselect(
    #     'Select province(s):',
    #     provinces,
    #     default=provinces[0]
    # )
    # #print('Provinces:', selected_provinces)
    # time_frame = st.sidebar.selectbox(
    #     'Select the amount of data:',
    #     time_frames
    # )
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
    file_name = f'{prov}.json'.replace(' ', '%20')
    dfProv = pd.read_json(urllib.parse.urljoin(base_url, file_name))
    last_date = dfProv['lastDate'].values[0]
    dfProv = dfProv.sort_values(by=['date'], ascending=False)
    dfProv = df_days(dfProv, last_date, time_frame)
    st.markdown('----')
    st.markdown(f'#### {prov}')
    st.markdown(f'###### Report Date: {last_date}')

    col1, col2 = st.beta_columns(2)
    with col1:
        stProvTable(dfProv)
    with col2:
        stProvGraphs(dfProv)

#-----------------------------------------------------------------------------
# Provincial Stats Graph for specified time span
#-----------------------------------------------------------------------------

def stProvGraphs(dfProv):

    #-------------------------------------------------------------------------
    # Create Confirmed New Plot
    #-------------------------------------------------------------------------

    st.markdown(f'##### New Cases - {time_frame}')

    fig1 = plt.figure(1, figsize=(15, 7))

    plt.title('New Cases - Smoothed', fontsize='large')
    plt.xlabel="Date"
    plt.ylabel="Number"

    #plt.xticks(rotation=45)
    ax = plt.gca()
    #ax.xaxis.set_major_locator(ticker.MultipleLocator(35))

    plt.plot(dfProv['date'], dfProv['confirmedNewMean'], label='New Cases - Smoothed')
    plt.grid()
    st.pyplot(fig1)
    plt.close()

    #-------------------------------------------------------------------------
    # Create Deaths New Plot
    #-------------------------------------------------------------------------

    st.markdown(f'##### New Deaths - {time_frame}')
    
    fig2 = plt.figure(2, figsize=(15, 7))

    plt.title('New Deaths - Smoothed')
    plt.xlabel="Date"
    plt.ylabel="Number"

    #plt.xticks(rotation=45)
    ax = plt.gca()
    #ax.xaxis.set_major_locator(ticker.MultipleLocator(35))

    plt.plot(dfProv['date'], dfProv['deathsNewMean'], label='New Deaths - Smoothed')
    plt.grid()
    st.pyplot(fig2)
    plt.close()
    #if prov == 'British Columbia':
    #stBCCases(dfProv)

#-----------------------------------------------------------------------------
# Provincial Stats Table for 8 days
#-----------------------------------------------------------------------------

def stProvTable(dfProv):
        st.markdown(f'##### 10 Days')

        # Table of details for last week 
        cases_data = '<div style="font-size: small">\n'
        cases_data += '<table border=1>\n'
        cases_data += '<tr><th> </th><th colspan=2 style="text-align:center">Cases</th><th colspan=2 style="text-align:center">Deaths</th></tr>\n'
        cases_data += '<tr><th>Date</th><th>Total</th><th>New</th><th>Total</th><th>New</th></tr>\n'
        #cases_data += '| :----- | ----------: | --------: | -----------: | ---------: |\n'
        row_count = 0
        for index, row in dfProv.iterrows():
            date = row['date'] 
            date = date.strftime("%Y-%m-%d")
            confirmed = row['confirmed']
            confirmed = "{:,}".format(confirmed)
            confirmedNew = row['confirmedNew']
            confirmedNew = "{:,}".format(confirmedNew)
            deaths = row['deaths']
            deaths = "{:,}".format(deaths)
            deathsNew = row['deathsNew']
            deathsNew = "{:,}".format(deathsNew)
            cases_data += f'<tr><td nowrap>{date}</td><td style="text-align:right">{confirmed}</td><td style="text-align:right">{confirmedNew}</td><td style="text-align:right">{deaths}</td><td style="text-align:right">{deathsNew}</td></tr>' + '\n'
            row_count += 1
            if row_count >= 10:
                cases_data += '</table>\n'
                cases_data += '</div>\n'
                break
        st.markdown(cases_data, unsafe_allow_html=True)

#-----------------------------------------------------------------------------
# Provincial Stats Table for 7 days
#-----------------------------------------------------------------------------

def stBCCases(dfProv):
    # "Reported_Date","HA","Sex","Age_Group","Classification_Reported"
    case_Url = 'http://www.bccdc.ca/Health-Info-Site/Documents/BCCDC_COVID19_Dashboard_Case_Details.csv'
    dfCase = pd.read_csv(case_Url) 
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
    st.markdown(f'#### Compare Canadian Provinces')
    st.markdown(f'###### Report Date: {last_date}')
    dfal = pd.read_csv(urllib.parse.urljoin(base_url, 'Alberta.csv'))
    dfal['ConfirmedNewPer1M'] = dfal['ConfirmedNewMean'] / prov_pop['AL']
    dfal['DeathsNewPer1M']    = dfal['DeathsNewMean'] / prov_pop['AL']
    dfbc = pd.read_csv(urllib.parse.urljoin(base_url, 'British%20Columbia.csv'))
    dfbc['ConfirmedNewPer1M'] = dfbc['ConfirmedNewMean'] / prov_pop['AL']
    dfbc['DeathsNewPer1M']    = dfbc['DeathsNewMean'] / prov_pop['AL']
    dfon = pd.read_csv(urllib.parse.urljoin(base_url, 'Ontario.csv'))
    dfon['ConfirmedNewPer1M'] = dfon['ConfirmedNewMean'] / prov_pop['AL']
    dfon['DeathsNewPer1M']    = dfon['DeathsNewMean'] / prov_pop['AL']
    dfqu = pd.read_csv(urllib.parse.urljoin(base_url, 'Quebec.csv'))
    dfqu['ConfirmedNewPer1M'] = dfqu['ConfirmedNewMean'] / prov_pop['AL']
    dfqu['DeathsNewPer1M']    = dfqu['DeathsNewMean'] / prov_pop['AL']
    #print(dfal.info())

    col1, col2 = st.beta_columns(2)
    #with col1:

    st.markdown(f'##### New Cases - {time_frame}')

    fig1 = plt.figure(1, figsize=(15, 10))

    #-------------------------------------------------------------------------
    # Create Confirmed New Plot
    #-------------------------------------------------------------------------

    plt.title('Confirmed New Cases per Million', fontsize='medium')
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
    st.pyplot(fig1)
    plt.close()

    #with col2:

    st.markdown(f'##### New Deaths - {time_frame}')

    fig1 = plt.figure(1, figsize=(15, 10))

    #-------------------------------------------------------------------------
    # Create Deaths New Plot
    #-------------------------------------------------------------------------

    plt.title('New Deaths per Million', fontsize='medium')
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
    st.pyplot(fig1)
    plt.close()

# #######################################################################################
# Section 3
#     Other countries
# #######################################################################################

def stSection3():
    global last_date

    st.markdown('----')
    st.markdown(f'#### Countries')
    st.markdown(f'###### Report Date: {last_date}')

    allGroups = createGroups()

    for group in allGroups:
        plotGroup(group)


#-------------------------------------------------------------------------
# Create groups of countries for plotting
#-------------------------------------------------------------------------

def createGroups():

    # North America
    canada = Country('Canada')
    mexico = Country('Mexico')
    usa = Country('US')
    am = [canada, mexico, usa]

    northAmerica = Countries('North America', am)

    # Western Europe
    france = Country('France')
    italy = Country('Italy')
    portugal = Country('Portugal')
    spain = Country('Spain')
    we = [france, italy, portugal, spain]

    westernEurope = Countries('Western Europe', we)

    # Eastern Europe
    bosnia = Country('Bosnia and Herzegovina')
    bulgaria = Country('Bulgaria')
    croatia = Country('Croatia')
    serbia = Country('Serbia')
    ee = [bosnia, bulgaria, croatia, serbia]

    easternEurope = Countries('Eastern Europe', ee)

    # Eastern Med
    albania = Country('Albania')
    cyprus = Country('Cyprus')
    greece = Country('Greece')
    turkey = Country('Turkey')
    em = [albania, cyprus, greece, turkey]

    easternMed = Countries('Eastern Med', em)


    # North Africa
    algeria = Country('Algeria')
    morocco = Country('Morocco')
    oman = Country('Oman')
    tunisia = Country('Tunisia')
    na = [algeria, morocco, oman, tunisia]

    northAfrica = Countries('North Africa', na)

    # South America
    argentina = Country('Argentina')
    bolivia = Country('Bolivia')
    chile = Country('Chile')
    uruguay = Country('Uruguay')
    sa = [argentina, bolivia, chile, uruguay]

    southAmerica = Countries('South America', sa)

    # Oceana
    australia = Country('Australia')
    newZealand = Country('New Zealand')
    oc = [australia, newZealand]

    oceana = Countries('Oceana', oc)

    # Asia
    thailand = Country('Thailand')
    vietnam = Country('Vietnam')
    se = [thailand, vietnam]

    asia = Countries('Asia', se)

    allGroups = [northAmerica, westernEurope, easternEurope, easternMed, northAfrica, southAmerica, oceana, asia]

    return allGroups

#-------------------------------------------------------------------------
# Plot a group of countries
#-------------------------------------------------------------------------

def plotGroup(countryGroup):
    global last_date

    plotFileName = countryGroup.groupName.replace(' ', '-')
    #plotPath = outputPngDir + '/' + plotFileName + '.png'

    #print('Plotting', countryGroup.groupName, 'to', plotPath)
    
    #plt.clf()
    fig1 = plt.figure(1, figsize=(15, 5))
    reportTitle = countryGroup.groupName + ' Confirmed New Cases - Smoothed'
    fig1.suptitle(reportTitle, fontsize=14)

    subPlotRows = 1
    subPlotCols = len(countryGroup.countryList)
    subPlotIndex = 0
    
    for country in countryGroup.countryList:
        subPlotIndex += 1

        df = getDfForCountry(country.name)

        ax = fig1.add_subplot(subPlotRows, subPlotCols, subPlotIndex)

        plt.title(country.name, fontsize='small', va='bottom')
        plt.xlabel="Date"
        plt.ylabel="Number"

        ax.xaxis.set_major_locator(ticker.MultipleLocator(120))

        ax.set_ylim(bottom=0, auto=True)
        plt.plot(df['Date'], df['ConfirmedNewMean'], label='New Confirmed')
        #plt.plot(country.df['date'], country.df['confirmedTenDayAverage'], label='10 Day Average', color='red')
        
    st.pyplot(fig1)
    plt.close(fig1)

#-------------------------------------------------------------------------
# Get dataframe for a country
#-------------------------------------------------------------------------

def getDfForCountry(countryName):
    global last_date

    country = countryName.replace(' ', '%20')
    df = pd.read_csv(urllib.parse.urljoin(base_url, f'{country}.csv'))

    return df

# ############################################################################
# Entry Point
# ############################################################################

stSetup()
stSection1()
stSection2()
stSection3()



