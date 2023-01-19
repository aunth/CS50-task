SELECT person_id, account_number, creation_year
FROM bank_accounts
WHERE person_id IN (SELECT account_number
FROM atm_transactions
WHERE  transaction_type = "withdraw"
AND month = 7
AND day = 28
AND year = 2021
AND atm_location = "Leggett Street")
AND account_number IN ((SELECT account_number
FROM atm_transactions
WHERE  transaction_type = "withdraw"
AND month = 7
AND day = 28
AND year = 2021
AND atm_location = "Leggett Street"))