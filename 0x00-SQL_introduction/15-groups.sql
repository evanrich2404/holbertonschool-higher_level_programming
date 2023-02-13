-- lists number of records withe the same score in second_table
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score DESC;
