-- Counts all shows linked to a genre.

SELECT tv_genres.name
AS genre, COUNT(tv_show_genres.genre_id)
AS show_qty
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id=tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_shows DESC;
