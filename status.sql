SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

CREATE TABLE IF NOT EXISTS 'status_codes' (
	'code' int(3) NOT NULL,
	'message' varchar(100) NOT NULL,
	'description' varchar(400) NUT NULL
) ENGINE = HTTPStatusCodes DEFAULT CHARSET = latin1;

ALTER TABLE 'status_codes'
	ADD PRIMARY KEY ('s_no.');