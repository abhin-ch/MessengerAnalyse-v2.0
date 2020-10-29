'SELECT * from participants'
'SELECT COUNT(content) from messages'
'SELECT SUM(length(content) - length(replace(content, ' ', '')) + 1) from messages'
