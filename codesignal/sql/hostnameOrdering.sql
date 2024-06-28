
-- https://app.codesignal.com/arcade/db/selecting-what-to-select/rpo4gmB8H8tpm5TEJ

CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	WITH split_domains AS (
		SELECT
			id, 
			reverse_dns(hostname) AS rev_dns,
			hostname
		FROM hostnames
		ORDER BY rev_dns
	)
	SELECT id, hostname -- , rev_dns
	FROM split_domains
	ORDER BY rev_dns, id 
	;
END
;

CREATE FUNCTION reverse_dns (s CHAR(255))
RETURNS CHAR(255) DETERMINISTIC
BEGIN
    DECLARE i INT;
    DECLARE s1, s2, s3 CHAR(255);
    SET i = LOCATE('.', s, 1);
    IF i = 0 THEN
        RETURN CONCAT_WS('.', s);
    END IF;
    SET s1 = SUBSTRING_INDEX(s, '.', 1);
	SET s2 = SUBSTRING(s, i+1);
	SET i = LOCATE('.', s2, 1);
    IF i = 0 THEN
        RETURN CONCAT_WS('.', s2, s1);
    END IF;
	SET s3 = SUBSTRING(s2, i+1);
	SET i = LOCATE('.', s2, 1);
	RETURN CONCAT_WS(
		'.', 
		s3, 
		SUBSTRING_INDEX(s2, '.', 1), 
		s1);
END
;
