SELECT *
FROM atm_transactions
WHERE  transaction_type = "withdraw"
AND month = 7
AND day = 28
AND year = 2021
AND atm_location = "Leggett Street";