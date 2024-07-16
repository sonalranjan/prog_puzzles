
-- https://app.codesignal.com/arcade/db/exotic-dishes/Mxv2EhqjsGs3oPkNG

DROP PROCEDURE IF EXISTS GenerateMonthlyReport;
CREATE PROCEDURE GenerateMonthlyReport()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE qry_name VARCHAR(255);
    DECLARE qry_code VARCHAR(1024);
    DECLARE result_val VARCHAR(1024);

    -- Declare cursor for queries
    DECLARE cur CURSOR FOR SELECT query_name, code FROM queries;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    -- Clear previous report results
    DROP TABLE IF EXISTS report_results;
    CREATE TABLE report_results (
        query_name VARCHAR(200), 
        val VARCHAR(200));
    
    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO qry_name, qry_code;
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Prepare and execute the dynamic query
        SET @dynamic_query = CONCAT('SELECT (', qry_code, ') INTO @res_val');
        PREPARE stmt FROM @dynamic_query;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;

        -- Retrieve the result value
        -- SELECT @res_val INTO result_val;

        -- Insert the result into the report_results table
        INSERT INTO report_results (query_name, val) VALUES (qry_name, @res_val);
    END LOOP;

    CLOSE cur;
    
    -- SET result_val = (SELECT MIN(date_placed) FROM `orders`); 
    -- SELECT 'MIN_ORDER_DATE', result_val;
    
    -- Sort the results by query_name
    -- SELECT * FROM report_results ORDER BY query_name;
	SELECT query_name, val
	FROM report_results
	ORDER BY query_name
	;
END
;

CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	CALL GenerateMonthlyReport();
END
