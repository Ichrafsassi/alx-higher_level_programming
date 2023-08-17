-- lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Description
--	Each record should display: tv_shows.title - rating sum
--	Results must be sorted in descending order by the rating
--	You can use only one SELECT statement

SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating -- Query to join tables
FROM tv_shows
JOIN tv_show_ratings
ON tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_shows.title
ORDER BY rating DESC;
