-- select all participants
SELECT *, 0 from participants;

-- select number of messages sent
SELECT COUNT(content) from messages;

-- select total sum of words sent
SELECT SUM(length(content) - length(replace(content, ' ', '')) + 1) from messages;

-- select messages by day of year
SELECT content from messages;

-- select messages by day of week

-- select messages by day of week as percentage

-- select messages by day of week grouping by participants

-- https://sqlite.org/lang_datefunc.html

-- SELECT strftime('%Y-%m-%d', 1578405100978 / 1000, 'unixepoch');

-- day of year
SELECT day, count(day)
FROM 
(
    SELECT strftime('%j', timestamp_ms / 1000, 'unixepoch') AS day 

    FROM messages
) GROUP BY day ORDER BY day;

-- day of week 0-sunday
SELECT CASE day
    WHEN '0' THEN 'Sunday'
    WHEN '1' THEN 'Monday'
    WHEN '2' THEN 'Tuesday'
    WHEN '3' THEN 'Wednesday'
    WHEN '4' THEN 'Thursday'
    WHEN '5' THEN 'Friday'
    WHEN '6' THEN 'Saturday'
    END,
    round(count(day)*(100.0) / (SELECT COUNT(timestamp_ms) from messages), 2) as percentage
FROM 
(
    SELECT strftime('%w', timestamp_ms / 1000, 'unixepoch') AS day 

    FROM messages
) GROUP BY day ORDER BY day;


SELECT day, count(day)
FROM 
(
    SELECT strftime('%H', timestamp_ms / 1000, 'unixepoch', 'localtime') AS day 

    FROM messages
) GROUP BY day ORDER BY day;

SELECT day, count(day)
FROM 
(
    SELECT strftime('%Y', timestamp_ms / 1000, 'unixepoch', 'localtime') AS day 

    FROM messages
) GROUP BY day ORDER BY day;