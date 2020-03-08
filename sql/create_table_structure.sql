create table tweets(
 tweet_id serial primary key not null,
 account_id int not null,
 tweet_time int default 0,
 tweet_content text,
 tweet_place char(100),
 geo_id int,
 tweet_hashtags char(255)
);

create table account(
 account_id serial primary key not null,
 account_name char(50) not null,
 account_url text not null,
 account_text text,
 account_reg_date int default 0,
 account_webpage char(255),
 account_pic_url char(255),
 account_verified boolean
);

create table geo(
 geo_id serial primary key not null,
 geo_name char(100),
 geo_lat int,
 geo_long int
);
