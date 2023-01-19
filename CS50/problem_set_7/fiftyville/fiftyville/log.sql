-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT discription 
FROM crime_scene_reports 
WHERE year = 2021
AND month = 7 
AND day = 28 
AND street = "Humphrey Street";

SELECT name, phone_number, passport_number
FROM people
WHERE license_plate IN (SELECT license_plate 
FROM bakery_security_logs 
WHERE year = 2021
AND month = 7
AND day = 28
AND hour > 9
AND hour < 11
AND activity = "exit");

