BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `weather` (
	`City`	text,
	`Temp`	text,
	`Humidity`	text,
	`Pressure`	numeric,
	`wind`	numeric
);
COMMIT;
