-- script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT tv_shows.title, GROUP_CONCAT(tv_show_genres.genre_id ORDER BY tv_show_genres.genre_id) AS genres
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
GROUP BY tv_shows.id, tv_shows.title
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;