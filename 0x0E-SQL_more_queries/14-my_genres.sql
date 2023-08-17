-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
-- Description :
--	The tv_shows table contains only one record where title = Dexter (but the id can be different)
--	Each record should display: tv_genres.name
--	Results must be sorted in ascending order by the genre name
--	You can use only one SELECT statement

SELECT tv_genres.name AS name
FROM tv_show_genres
INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
INNER JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id
	AND tv_shows.title = 'Dexter'
ORDER BY name;
