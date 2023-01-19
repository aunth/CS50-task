SELECT name, phone_number, passport_number FROM people
JOIN (SELECT person_id FROM bank_accounts
WHERE account_number IN (SELECT account_number
FROM atm_transactions
WHERE  transaction_type = "withdraw"
AND month = 7
AND day = 28
AND year = 2021
AND atm_location = "Leggett Street"))
ON people.id = person_id
