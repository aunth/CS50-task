SELECT movies.title from ratings
JOIN movies on ratings.movie_id = movies.id
JOIN stars on stars.movie_id = movies.id
JOIN people on stars.person_id = people.id
WHERE people.name = "Chadwick Boseman"
LIMIT 5;



