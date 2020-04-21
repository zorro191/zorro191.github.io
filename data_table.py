# Python program to convert  
# CSV to HTML Table 
  
  
import pandas as pd 
  
# to read csv file named "samplee" 
city_table = pd.read_csv("WebVisualizations\Resources\cities.csv") 
  
# to save as html file 
# named as "Table" 
city_table.to_html("Table.htm") 
  
# assign it to a  
# variable (string) 
html_file = city_table.to_html()