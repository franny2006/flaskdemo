create database devopsroles;
use devopsroles;

CREATE TABLE test_table (
  name VARCHAR(20),
  color VARCHAR(10)
);

CREATE TABLE kunden (
  kunde_id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  rolle_id int(11) NOT NULL,
  anrede varchar(20) NOT NULL,
  vorname varchar(50) NOT NULL,
  name varchar(50) NOT NULL,
  strasse varchar(50) NOT NULL,
  plz varchar(7) NOT NULL,
  ort varchar(50) NOT NULL,
  timestamp timestamp NOT NULL DEFAULT current_timestamp()
);


INSERT INTO test_table
  (name, color)
VALUES
  ('dev', 'blue');

INSERT INTO kunden
  (rolle_id, anrede, vorname, name, strasse, plz, ort)
VALUES
  ('1', 'Frau', 'Maria', 'Musterfrau', 'Musterstrasse', '11112', 'Musterstadt');