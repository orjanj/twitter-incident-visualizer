-- Table: public.account

-- DROP TABLE public.account;

CREATE TABLE public.account
(
    account_id serial NOT NULL,
    account_name character(50) COLLATE pg_catalog."default" NOT NULL,
    account_url text COLLATE pg_catalog."default" NOT NULL,
    account_text text COLLATE pg_catalog."default",
    account_reg_date integer DEFAULT 0,
    account_webpage character(255) COLLATE pg_catalog."default",
    account_pic_url character(255) COLLATE pg_catalog."default",
    account_verified boolean,
    CONSTRAINT account_pkey PRIMARY KEY (account_id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.account
    OWNER to tiv;


-- Table: public.geo

-- DROP TABLE public.geo;

CREATE TABLE public.geo
(
    geo_id serial NOT NULL,
    geo_name character(100) COLLATE pg_catalog."default",
    geo_lat integer,
    geo_long integer,
    CONSTRAINT geo_pkey PRIMARY KEY (geo_id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.geo
    OWNER to tiv;


-- Table: public.tweets

-- DROP TABLE public.tweets;

CREATE TABLE public.tweets
(
    tweet_id serial NOT NULL,
    account_id integer NOT NULL,
    tweet_time integer DEFAULT 0,
    tweet_content text COLLATE pg_catalog."default",
    tweet_place character(100) COLLATE pg_catalog."default",
    geo_id integer,
    tweet_hashtags character(255) COLLATE pg_catalog."default",
    CONSTRAINT tweets_pkey PRIMARY KEY (tweet_id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.tweets
    OWNER to tiv;
