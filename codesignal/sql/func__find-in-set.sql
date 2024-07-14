
-- https://app.codesignal.com/arcade/db/express-your-creativity/LhRfNbgyBKM3KKBp9

DROP FUNCTION IF EXISTS get_total;
CREATE FUNCTION get_total(items VARCHAR(45)) RETURNS INT DETERMINISTIC
BEGIN
    DECLARE tot INT;
    
    SET tot = (SELECT sum(price) FROM item_prices WHERE FIND_IN_SET(id, REPLACE(items, ';', ',')));
    -- SET tot = (SELECT sum(price) FROM item_prices WHERE items REGEXP CONCAT('(^|;)', CAST(id AS CHAR(50)), '(;|$)'));
  
    RETURN tot;
END;

CREATE PROCEDURE solution()
BEGIN
    SELECT id, buyer, get_total(items) AS total_price
    FROM orders
    ORDER BY id;
END;

