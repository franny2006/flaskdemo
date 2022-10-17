create database devopsroles;
use devopsroles;


CREATE TABLE kunden (
  kunde_id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  rolle_id int(11) NOT NULL,
  anrede varchar(20) NOT NULL,
  vorname varchar(50) NOT NULL,
  name varchar(50) NOT NULL,
  strasse varchar(50) NOT NULL,
  plz varchar(7) NOT NULL,
  ort varchar(50) NOT NULL,
  geburtsdatum varchar(50) NOT NULL,
  timestamp timestamp NOT NULL DEFAULT current_timestamp()
);

CREATE TABLE kfz (
  kfz_id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  hsn varchar(20) NOT NULL,
  tsn varchar(50) NOT NULL,
  modell varchar(50) NOT NULL,
  wert varchar(50) NOT NULL,
  timestamp timestamp NOT NULL DEFAULT current_timestamp()
);


INSERT INTO kunden
  (rolle_id, anrede, vorname, name, strasse, plz, ort, geburtsdatum)
VALUES
  ('1', 'Frau', 'Maria', 'Musterfrau', 'Musterstrasse', '11111', 'Musterstadt', '01.01.1970');