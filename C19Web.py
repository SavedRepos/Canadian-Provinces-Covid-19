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
            )
selected_provinces = ('British Columbia') 

time_frames = ('1 Week', '2 Weeks', '3 Weeks', '1 Month', '3 Months', '6 Months', 'All')
time_frame = ''

last_date = ''
    
# #######################################################################################
# Select days based time_frame
# #######################################################################################

def df_days(dfProv, last_date, time_frame):

    first_date = parser.parse('2020-03-01')
    in_date = parser.parse(last_date)

    if time_frame == time_frames[0]:
        date_after = in_date - relativedelta(weeks=1)
    elif time_frame == time_frames[1]:
        date_after = in_date - relativedelta(weeks=2)
    elif time_frame == time_frames[2]:
        date_after = in_date - relativedelta(weeks=3)
    elif time_frame == time_frames[3]:
        date_after = in_date - relativedelta(months=1)
    elif time_frame == time_frames[4]:
        date_after = in_date - relativedelta(months=3)
    elif time_frame == time_frames[5]:
        date_after = in_date - relativedelta(months=6)
    elif time_frame == time_frames[6]:
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
    st.sidebar.subheader('Options')
    selected_provinces = st.sidebar.multiselect(
        'Select province(s):',
        provinces,
        default=provinces[0]
    )
    #print('Provinces:', selected_provinces)
    time_frame = st.sidebar.selectbox(
        'Select the amount of data:',
        time_frames
    )
    return

# #######################################################################################
# Provincial Stats Graph for specified time span
# #######################################################################################

def stProvGraphs(dfProv):

    #-------------------------------------------------------------------------
    # Create Confirmed New Plot
    #-------------------------------------------------------------------------

    fig1 = plt.figure(1, figsize=(15, 6))

    #plt.title('New Confirmed Cases', fontsize='large')
    plt.xlabel="Date"
    plt.ylabel="Number"

    #plt.xticks(rotation=45)
    ax = plt.gca()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(35))

    plt.bar(dfProv['date'], dfProv['confirmedNewMean'], label='New Cases')
    plt.grid()
    st.pyplot(fig1)
    plt.close()

    #-------------------------------------------------------------------------
    # Create Deaths New Plot
    #-------------------------------------------------------------------------

    fig2 = plt.figure(2, figsize=(15, 6))

    #plt.title('New Deaths')
    plt.xlabel="Date"
    plt.ylabel="Number"

    #plt.xticks(rotation=45)
    ax = plt.gca()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(35))

    plt.bar(dfProv['date'], dfProv['deathsNew'], label='New Deaths')
    plt.grid()
    st.pyplot(fig2)
    plt.close()
    #if prov == 'British Columbia':
    #stBCCases(dfProv)

# #######################################################################################
# Provincial Stats Table for 7 days
# #######################################################################################

def stProvTable(dfProv):
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
            if row_count >= 7:
                cases_data += '</table>\n'
                cases_data += '</div>\n'
                break
        st.markdown(cases_data, unsafe_allow_html=True)


# #######################################################################################
# Provincial Stats Table for 7 days
# #######################################################################################

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

    for prov in selected_provinces:
        file_name = f'{prov}.json'.replace(' ', '%20')
        dfProv = pd.read_json(urllib.parse.urljoin(base_url, file_name))
        last_date = dfProv['lastDate'].values[0]
        dfProv = dfProv.sort_values(by=['date'], ascending=False)
        dfProv = df_days(dfProv, last_date, time_frame)
        st.subheader(f'{prov}   Report Date - {last_date}')

        col1, col2 = st.beta_columns(2)
        with col1:
            st.markdown(f'#### New Cases - {time_frame}')
            stProvGraphs(dfProv)
        with col2:
            st.markdown(f'#### 7 Days')
            stProvTable(dfProv)

# #######################################################################################
# Section 2
#     Graphs - Western Europe
#     Graphs - Eastern Europe
#     Graphs - North Africa
#     Graphs - South America
#     Graphs - Oceana
# #######################################################################################

def stSection2():
    pass


# ############################################################################
# Entry Point
# ############################################################################

stSetup()
stSection1()

