select top 100 *  from AIR_Creation_21_22
where DEMAND_guiD='00163E6A60BD1EEBA5C83F8C3B8DC3EE'


update AIR_Creation_21_22
set PROJECT_NAME='NRE-VAL-PJ--SAP-AMS-CAD'
where DEMAND_guiD='00163E6A60BD1EEBA5C83F8C3B8DC3EE'


--NRE-VAL-PJ--SAP-AMS-CAD

select DEMAND_GUID, count(*) as DuplicatesCount
from AIR_Creation_21_22
group by DEMAND_GUID

SELECT count(*) FROM AIR_Creation_21_22
--Deleting duplicate values
; WITH TableBWithRowID AS
(
 SELECT ROW_NUMBER() OVER (PARTITION BY DEMAND_GUID ORDER BY DEMAND_GUID) AS RowID, DEMAND_GUID
  FROM AIR_Creation_21_22
)

DELETE o
FROM TableBWithRowID o
WHERE RowID > 1

SELECT count(*) FROM ZCOP_Q2_21

select * from ZCOP_Q1_21
where SMU = 'BFSI'

select LOAD_DATE, count(*) as DuplicatesCount
from ZCOP_Q4_20
group by LOAD_DATE

--IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[ZCOP_Q4_21]') AND type in (N'U'))
DROP TABLE Users
GO