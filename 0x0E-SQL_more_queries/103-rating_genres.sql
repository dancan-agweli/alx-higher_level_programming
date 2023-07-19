--all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT tv_genres.name, SUM(tvshows.rating) AS rating_sum
FROM tv_genres
JOIN tvshows ON tv_genres.id = tvshows.genre_id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;

