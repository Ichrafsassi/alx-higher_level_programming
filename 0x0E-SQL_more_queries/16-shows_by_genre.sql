-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
-- Description
--	If a show doesn’t have a genre, display NULL in the genre column
--	Each record should display: tv_shows.title - tv_genres.name
--	Results must be sorted in ascending order by the show title and genre name
-- 	You can use only one SELECT statement

SELECT tv_shows.title AS title,
	tv_genres.name AS name
FROM tv_show_genres
RIGHT JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
LEFT JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
ORDER BY title, name;
