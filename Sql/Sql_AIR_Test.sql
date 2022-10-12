select e.DEMAND_ID, e.DEM_END_DATE, e.DEMAND_GUID from AIR_Creation_20_21_Q1_Q2_Q3 e join AIR_Creation_20_21_Q4 f 
on e.DEMAND_GUID=f.DEMAND_GUID

select DEMAND_ID, DEM_END_DATE from AIR_Creation_20_21_Q4