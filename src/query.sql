-- select all participants
SELECT * from participants;

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
) GROUP BY day ORDER BY day ;

-- day of week 0-sunday
SELECT day, count(day)
FROM 
(
    SELECT strftime('%w', timestamp_ms / 1000, 'unixepoch') AS day 

    FROM messages
) GROUP BY day ORDER BY day ;