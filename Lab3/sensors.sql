BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `sensors` (
	`sensorID`	integer,
	`type`	text,
	`zone`	text
);
INSERT INTO `sensors` VALUES (1,'door','kitchen');
INSERT INTO `sensors` VALUES (2,'temperature','kitchen');
INSERT INTO `sensors` VALUES (3,'door','garage');
INSERT INTO `sensors` VALUES (4,'motion','garage');
INSERT INTO `sensors` VALUES (5,'temperature','garage');
COMMIT;
