
-- https://app.codesignal.com/arcade/db/time-river-revisited/G9zoZjTzk6JpJGFbd
-- alarmClocks

CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	WITH RECURSIVE dategen AS (
		SELECT input_date AS d
		FROM userInput
		UNION ALL 
		SELECT d + INTERVAL '7' DAY AS d
		FROM dategen
		WHERE YEAR(d + INTERVAL '7' DAY) = YEAR(d)
		
	) 
	SELECT d AS alarm_date
	FROM dategen
	ORDER BY alarm_date ASC
	;
END
