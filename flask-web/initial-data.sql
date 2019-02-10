-- sqlite3 profile.db < initial-data.sql

-- Countries
INSERT INTO country (id, name) VALUES (1, 'United States');
INSERT INTO country (id, name) VALUES (2, 'England');
INSERT INTO country (id, name) VALUES (3, 'Argentina');
INSERT INTO country (id, name) VALUES (4, 'Scotland');

-- Profile
INSERT INTO profile (id, country_id, name) VALUES (1, 1, 'AUG');
INSERT INTO profile (id, country_id, name) VALUES (2, 1, 'MGH');
INSERT INTO profile (id, country_id, name) VALUES (3, 4, 'MZM');
INSERT INTO profile (id, country_id, name) VALUES (4, 3, 'AZM');
