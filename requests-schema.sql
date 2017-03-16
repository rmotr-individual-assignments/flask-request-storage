-- sqlite3 requests.db < requests-schema.sql

PRAGMA foreign_keys = ON;

DROP TABLE if exists request;
CREATE TABLE request (
  id INTEGER PRIMARY KEY autoincrement,
  url TEXT NOT NULL,
  method TEXT NOT NULL
);
