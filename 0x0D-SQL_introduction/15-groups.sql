-- Lists the number of records with the same score.
SELECT score, count(*) AS NUMBER FROM second_table GROUP BY score DESC;
