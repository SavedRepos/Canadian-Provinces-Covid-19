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

from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil import parser
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
import streamlit as st
import urllib

test_variable = 'Can i see you?'

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

