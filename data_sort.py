import csv
rows=[]
dwarf_stars_mass=[]
dwarf_stars_radiuses=[]
with open('dwarf_stars.csv',"r") as f:
  csvreader=csv.reader(f)
  for row in csvreader:
    dwarf_stars_data=row[1:]
    dwarf_stars_mass_value=dwarf_stars_data[3]
    if dwarf_stars_mass_value != "":
       dwarf_stars_mass_value=float(dwarf_stars_mass_value)*0.000954588
       dwarf_stars_mass.append(dwarf_stars_mass_value)   
  
    dwarf_stars_radius_value=dwarf_stars_data[4]
    if dwarf_stars_radius_value != "":
       dwarf_stars_radius_value=float(dwarf_stars_radius_value)*0.102763
       dwarf_stars_radiuses.append(dwarf_stars_radius_value)

    print(dwarf_stars_mass)   
    print(dwarf_stars_radiuses)    

  

      

    




