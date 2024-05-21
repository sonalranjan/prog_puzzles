
-- https://app.codesignal.com/arcade/db/join-us-at-the-table/FJsQ38t6MDWXsCuLP
-- localCalendar

CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT
		t1.event_id AS event_id,
		DATE_FORMAT(t1.date + INTERVAL t2.timeshift MINUTE, CONCAT("%Y-%m-%d ", IF(t2.hours = 24, "%H:%i", "%h:%i %p"))) AS formatted_date
	FROM `events` AS t1
	INNER JOIN settings AS t2
	ON t1.user_id = t2.user_id
	ORDER BY event_id ASC
	;
END
