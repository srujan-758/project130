import csv
rows=[]
new_row=[]
with open('merged_dataset.csv',"r") as f:
  csvreader=csv.reader(f)
  for row in csvreader:
    if row[5:]=="Luminosity":
      headers=row
      new_row.append(headers)
    else:
      row[5:]=""
      new_row_value=row
      new_row.append(new_row_value)
        
    
with open("final_merged_data.csv", "w",newline='') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerows(new_row)    

