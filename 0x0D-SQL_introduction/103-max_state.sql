--  displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

SELECT state , max(value) as max_temp FROM temperatures
GROUP BY state ORDER BY state;
