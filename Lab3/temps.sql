BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `temps` (
	`tdate`	date,
	`ttime`	time,
	`zone`	text,
	`temperature`	numeric
);
INSERT INTO `temps` VALUES ('2020-10-01','18:19:56','kitchen',20.6);
INSERT INTO `temps` VALUES ('2020-10-01','18:20:08','greenhouse',26.3);
INSERT INTO `temps` VALUES ('2020-10-01','18:20:17','garage',18.6);
INSERT INTO `temps` VALUES ('2020-10-02','06:20:23','kitchen',19.5);
INSERT INTO `temps` VALUES ('2020-10-02','06:20:30','greenhouse',15.1);
INSERT INTO `temps` VALUES ('2020-10-02','06:20:36','garage',18.1);
INSERT INTO `temps` VALUES ('2020-10-02','18:20:41','kitchen',21.2);
INSERT INTO `temps` VALUES ('2020-10-02','18:20:51','greenhouse',27.1);
INSERT INTO `temps` VALUES ('2020-10-02','18:20:58','garage',19.1);
COMMIT;
