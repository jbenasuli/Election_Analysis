# Election_Analysis

## Project Overview

Perform an audit of a recent congressional election for the Colorado Board of Elections. Use Python to analyze the voting data and generate a report certifying the election results. Demonstrate that Python can successfully automate the audit processes for this election and how it can easily be levered to perform similar analyses and certify other elections in Colorado.

## Resources

- Data Source: election_results.csv
- Software: Python 3.7.9, Visual Studio Code 1.53.0

## Election Audit Results

The analysis of the election shows that:

- There were 369,711 votes cast in the election.

- The vote breakdown for each county in the precinct was:
  - Jefferson County accounted for 10.5% of the total vote with 38,855 votes cast.
  - Denver County accounted for 82.8% of the total vote with 306,055 votes cast.  
  - Arapahoe County accounted for 6.7% of the total vote with 24,801 votes cast.

- Denver County had the largest number of votes.

- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
  - Diana DeGette received 73.8% of the vote and 272,892 votes.
  - Charles Casper Stockham received 3.1% of the vote and 11,606 votes.

- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 votes.

## Election Audit Summary

The flexible nature of this Python code means that it can be fed data for any election, which has the same structure and requires the same analysis. No voting data is hardcoded making this tool agnostic to the  names and quantities of candidates and counties. Regardless of how many candidates and counties are reflected in the voting data, this audit tool will successfully analyze an election results csv file with the same structure and generate a vote count report certifying the given election's results.

The code in the audit tool can easily be modified to analyze locality data other than just county vote data. Below I have outlined two examples of the ways the audit tool script may be modified in order to certify and/or derive different insights into the results of elections held in Colorado.

### 1) Evaluating a locality other than county

If a set of locations other than counties is required to analyze and certify the results of a given election, a different set of locations can be passed to the script in place of county data. If a different type of location is passed, the variables, lists, and dictionaries which refer to county data will need to be renamed to align with the new location data type. Any print statements containing county result specific text will also have to be edited to reflect the change. Additionally if the new location data is populated in a different column than the current county data column, the location data index references in the script will have to be edited accordingly.

### 2) Evaluating additional locality types

For elections of varying sizes held across the state, different location data might be required to best certify and analyze a given election's results. In addition to the ability to swap the county data and analysis to a different location type, new code can be layered on to the existing script to evaluate as many location types as required by the Board's needs.

Using the existing county data code as guideline, new variables, lists and dictionaries for each additional location can be added to the existing script in order for the existing county analysis to be performed at the new locality level. When adding this new additional code, make sure that the new location data column index being called in the script aligns with the new location data in the csv file. Finally, update the print statements to reflect the updated desired output. Once these steps are completed, the updated script will be ready for testing and debugging.
