CREATE TABLE CASTLE
(
CASTLE_NAME VARCHAR2 (26 BYTE) NOT NULL
);

CREATE TABLE UNIT(
UNIT_NAME VARCHAR2 (26 BYTE) NOT NULL);

CREATE TABLE UNIT_CASTLE(
UNIT_NAME VARCHAR2 (26 BYTE) NOT NULL,
CASTLE_NAME VARCHAR2 (26 BYTE) NOT NULL
);

CREATE TABLE UNIT_LEVEL(
UNIT_NAME VARCHAR2 (26 BYTE) NOT NULL,
UNIT_LEVEL VARCHAR2 (26 BYTE) NOT NULL);

CREATE TABLE UNIT_INFO(
UNIT_NAME VARCHAR2 (26 BYTE) NOT NULL,
GOLD NUMBER(38,0) NOT NULL,
SPEED NUMBER(38,0) NOT NULL,
ATTACK NUMBER(38,0) NOT NULL);

ALTER TABLE CASTLE ADD CONSTRAINT CASTLE_PK PRIMARY KEY (CASTLE_NAME);
ALTER TABLE UNIT ADD CONSTRAINT UNIT_PK PRIMARY KEY (UNIT_NAME);
ALTER TABLE UNIT_CASTLE ADD CONSTRAINT UNIT_CASTLE_PK PRIMARY KEY (UNIT_NAME);
ALTER TABLE UNIT_LEVEL ADD CONSTRAINT UNIT_LEVEL_PK PRIMARY KEY (UNIT_NAME);
ALTER TABLE UNIT_INFO ADD CONSTRAINT UNIT_INFO_PK PRIMARY KEY (UNIT_NAME);

ALTER TABLE UNIT_CASTLE ADD CONSTRAINT CASTLE_FK FOREIGN KEY (CASTLE_NAME) REFERENCES CASTLE (CASTLE_NAME);
ALTER TABLE UNIT_CASTLE ADD CONSTRAINT UNIT_FK FOREIGN KEY (UNIT_NAME) REFERENCES UNIT (UNIT_NAME);
ALTER TABLE UNIT_CASTLE ADD CONSTRAINT UNIT_CASTLE_INFO_FK FOREIGN KEY (UNIT_NAME) REFERENCES UNIT_INFO (UNIT_NAME);
ALTER TABLE UNIT_CASTLE ADD CONSTRAINT UNIT_CASTLE_LEVEL_FK FOREIGN KEY (UNIT_NAME) REFERENCES UNIT_LEVEL (UNIT_NAME);
ALTER TABLE UNIT_LEVEL ADD CONSTRAINT UNIT_LEVEL_FK FOREIGN KEY (UNIT_NAME) REFERENCES UNIT (UNIT_NAME);
ALTER TABLE UNIT_LEVEL ADD CONSTRAINT UNIT_LEVEL_INFO_FK FOREIGN KEY (UNIT_NAME) REFERENCES UNIT_INFO (UNIT_NAME);
ALTER TABLE UNIT_INFO ADD CONSTRAINT UNIT_INFO_FK FOREIGN KEY (UNIT_NAME) REFERENCES UNIT (UNIT_NAME);