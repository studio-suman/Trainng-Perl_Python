select top 10  a.LOAD_DATE,a.DEMAND_GUID,a.PROJECT_CATEGORY from AIR_Creation_21_22 a
join AIR_Creation_20_21_Q4 b
on a.DEMAND_GUID=b.DEMAND_GUID
where a.smu='AMR2' and b.smu='amr2'


select count(*) from AIR_Creation_21_22 a
join AIR_Creation_20_21_Q4 b
--join AIR_Creation_20_21_Q1_Q2_Q3 c
on a.SMU=b.SMU
where a.smu='AMR2' and b.smu='AMR2'


select * from AIR_Creation_21_22
where SMU = 'AMR2'

UNION

select * from AIR_Creation_20_21_Q4
where SMU = 'AMR2'

UNION

select * from AIR_Creation_20_21_Q1_Q2_Q3
where SMU = 'AMR2'

--[PROJ_SAP_BU]

--Renaming Columns

EXEC sp_rename 'AIR_Creation_20_21_Q1_Q2_Q3.PROJ_SAP_BU' , 'SMU', 'COLUMN'
EXEC sp_rename 'AIR_Creation_20_21_Q1_Q2_Q3.PROJ_SAP_VERTICAL', 'SECTOR', 'COLUMN'