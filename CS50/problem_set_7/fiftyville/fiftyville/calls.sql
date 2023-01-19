SELECT caller, receiver, duration
FROM phone_calls
WHERE receiver IN (SELECT phone_number
FROM people
WHERE license_plate IN (SELECT license_plate 
FROM bakery_security_logs 
WHERE year = 2021
AND month = 7
AND day = 28
AND hour > 9
AND hour < 11
AND activity = "exit"))
OR caller IN (SELECT phone_number
FROM people
WHERE license_plate IN (SELECT license_plate 
FROM bakery_security_logs 
WHERE year = 2021
AND month = 7
AND day = 28
AND hour > 9
AND hour < 11
AND activity = "exit"))
AND year = 2021
AND day = 28
AND month = 7
AND duration <= 60;
