-- Lists the number of records with the same scores
SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESC;
