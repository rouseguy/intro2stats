# Introduction to Statistics

Inspired by Allen Downey's books [Think Stats](http://greenteapress.com/thinkstats/) and [Think Bayes](http://greenteapress.com/thinkbayes/), this is an attempt to learn Statistics using an application-centric programming approach. 

## Objective
Showcase real-life examples and what statistics to use in each of those examples. Almost every book teaches a concept and shows an example. Ultimately, every topic gets treated separately and no holistic view is presented. Here, we would take examples and see how to make sense out of it. 

## Topics covered

* Mean, Median, Mode
* Standard Deviation
* Variance
* Co-variance
* Probability Distribution
* Hypothesis Testing
* t-test, p-value, chi-squared test
* Confidence Intervals
* Confidence levels and Sigificance levels
* Correlation
* Resampling (and uses in Big Data)
* A/B Testing
* A simple linear regression model

## Workshop Plan
We would be using Marijuana prices in various states of the USA, along with demographic data of the USA based on the latest census data

There will be separate ipython notebooks - grouped by topic similarities. *notebooks will be uploaded later*
Some examples include:
* Find sum of people buying weed in a year, by various states.
* Find mean of price in a week/month, by various states.
* Find variance of price in selected states. Find variance of selected states by week of month
* Define distribution. Plot histograms
* Determining outliers (Plots, quantiles, box plots, percentiles) in weed price data
* Continuous distributions(exponential distribution, normal distribution)
* Introduction to Probability
* Hypothesis testing. Check if weed price across states are similar or not. Check for different qualities of weed
* Resampling
* Simple regression model: Predict weed price for the next month. Understand the output and diagnostics
* Introduction to A/B testing: Impact of regulation and deregulation on a couple of states 


## Prerequisites
* Basics of Python. User should know how to write functions; read in a text file(csv, txt, fwf) and parse them; conditional and looping constructs; using standard libraries like os, sys; lists, list comprehension, dictionaries
* It is good to know basics of the following:
    * Numpy
    * Scipy
    * Pandas
    * Matplotlib
    * Seaborn
    * IPython and IPython notebook - Everything here would be an IPython notebook
* Software Requirements
    * Python 2.7
    * git - so that this repo can be cloned :)  
    * virtualenv
    * Libraries from *requirements.txt*

## Optional
Users could choose to install Anaconda, if they want. If using Anaconda or Enthought, please ensure that all libraries listed in the requirements.txt are installed. 

*Note to Windows Users*: Neither of us use Windows. From past workshop experiences, Windows users have faced issues installing the way explained below. It is advisable to install Anaconda and ensure that all the libraries listed in the *requirements.txt* file are installed.  

## Setup Guide

####Clone the repository
    $ git clone https://github.com/rouseguy/intro2stats.git

####Create a virtual environment & activate
    $ cd intro2stats
    $ virtualenv env
    $ source env/bin/activate

####Install reqirements from requirements file
    $ pip install -r requirements.txt

####Note: Make sure you have libraries for png & freetype.
Ubuntu users can install the below

    apt-get install libfreetype6-dev
    apt-get install libpng-dev

###Script to check if installation is fine for the workshop
Please execute the following at the command prompt
    $ python check_env.py

If any library has a `FAIL` message, please install/upgrade that library.
