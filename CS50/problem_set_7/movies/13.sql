SELECT people.name
FROM people JOIN stars ON people.id = stars.person_id
WHERE movie_id in (SELECT movie_id
FROM people JOIN stars ON people.id = stars.person_id
WHERE people.name = "Kevin Bacon" and people.birth = 1958) and people.name != "Kevin Bacon"
GROUP BY people.name






