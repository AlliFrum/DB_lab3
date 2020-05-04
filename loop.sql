DECLARE 
    VAR_UNIT UNIT_CASTLE.UNIT_NAME%TYPE;
    VAR_CASTLE UNIT_CASTLE.CASTLE_NAME%TYPE;

BEGIN

    VAR_UNIT := 'UNIT';
    VAR_CASTLE := 'CITY';

    FOR i IN 1..10 LOOP
        INSERT INTO CASTLE (CASTLE_NAME) ---UNIT_CASTLE ссылается на CASTLE
        VALUES (TRIM(VAR_CASTLE) || i);
        INSERT INTO UNIT_CASTLE (
        UNIT_NAME,
        CASTLE_NAME)
        VALUES (
        TRIM(VAR_UNIT) || i,
        TRIM(VAR_CASTLE) || i);
        END LOOP;
END;
    
    