-- sqlite3 profile.db < profile-schema.sql

drop table if exists country;
create table country (
  id integer primary key autoincrement,
  name text not null
);

drop table if exists author;
create table profile (
  id integer primary key autoincrement,
  country_id integer,
  name text not null
);

drop table if exists book;
create table product (
  id integer primary key autoincrement,
  profile_id integer,
  product text not null,
  avg_purchase text
);