-- intitate database

PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    image TEXT NOT NULL,
    title TEXT NOT NULL,
    material TEXT NOT NULL,
    description TEXT NOT NULL

);

-- add current entries

INSERT INTO posts VALUES(4,'2023-01-13 19:45:45','https://ucarecdn.com/4f483d18-ebd2-473d-a706-2b5dd1823411/','Adding a New Post','Out of the finest stuff','A nice description');
INSERT INTO posts VALUES(5,'2023-01-13 20:20:32','https://ucarecdn.com/9d46e329-7804-4f91-bd33-6ff61aa48011/','A brand new Post','Some Material','And A description    ');
INSERT INTO posts VALUES(7,'2023-01-13 20:45:22','https://ucarecdn.com/6b2a0f89-309a-45ab-8330-7051001a6d90/','Vertical Image','Some Material','Description            ');
INSERT INTO posts VALUES(8,'2023-01-13 22:47:28','https://ucarecdn.com/b101a5f2-4797-4078-b693-3ab020880df3/','A New Post added on the Droplet','Just Bits and Bytes','Fully Ethereal                           ');
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('posts',8);
COMMIT;