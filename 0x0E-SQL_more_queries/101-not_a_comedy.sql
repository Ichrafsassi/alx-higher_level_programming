--  lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- Description :
--	The tv_genres table contains only one record where name = Comedy (but the id can be different)
--	Each record should display: tv_shows.title
--	Results must be sorted in ascending order by the show title
--	You can use a maximum of two SELECT statement

SELECT tv_shows.title
FROM tv_shows
LEFT JOIN
(
	SELECT tv_shows.title
	FROM tv_shows
     	JOIN tv_show_genres
     	     ON tv_show_genres.show_id = tv_shows.id
     	JOIN tv_genres
     	     ON tv_genres.id = tv_show_genres.genre_id
	WHERE tv_genres.name = "Comedy"
	ORDER BY tv_shows.id
) comedy_shows ON comedy_shows.title = tv_shows.title
WHERE comedy_shows.title is NULL
ORDER BY tv_shows.title;
