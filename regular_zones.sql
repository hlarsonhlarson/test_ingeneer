with REGULARS (ACCOUNTID,ZONENUMBER,START_TIME1,END_TIME1) as (
SELECT f.ACCOUNTID ,f.ZONENUMBER ,DATE(START_TIME/1000,'unixepoch') as START_TIME1 ,
DATE(END_TIME/1000,'unixepoch') as END_TIME1
FROM PARKING p 
INNER JOIN FAVOURIT f 
on f.ACCOUNTID =p.ACCOUNTID 
AND f.ZONENUMBER =p.ZONENUMBER 
WHERE END_TIME1 > '2020-12-31'
AND END_TIME1 < '2021-03-01'
AND START_TIME1 > '2020-12-31'
AND START_TIME1 < '2021-03-01')
SELECT  COUNT(DAY1) as num_days, ACCOUNTID ,ZONENUMBER  FROM (SELECT distinct DAY1,ACCOUNTID ,ZONENUMBER FROM (
	SELECT SUBSTR(START_TIME1 , 5) as DAY1,
	ACCOUNTID ,ZONENUMBER
	FROM REGULARS 
	GROUP by DAY1,ACCOUNTID ,ZONENUMBER 
	UNION ALL 
	SELECT SUBSTR(END_TIME1 , 5) as DAY1,
	ACCOUNTID ,ZONENUMBER
	FROM REGULARS 
	GROUP by DAY1,ACCOUNTID ,ZONENUMBER 
)
)
GROUP by ACCOUNTID ,ZONENUMBER
HAVING num_days > 15
ORDER BY ACCOUNTID ,ZONENUMBER DESC
