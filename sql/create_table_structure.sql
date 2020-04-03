-- Table: public.account

-- DROP TABLE public.account;

CREATE TABLE public.account
(
    account_id integer NOT NULL DEFAULT nextval('account_account_id_seq'::regclass),
    account_name character(255) COLLATE pg_catalog."default" NOT NULL,
    account_url text COLLATE pg_catalog."default" NOT NULL,
    account_text text COLLATE pg_catalog."default",
    account_reg_date character(255) COLLATE pg_catalog."default" DEFAULT 0,
    account_webpage character(255) COLLATE pg_catalog."default",
    account_pic_url character(255) COLLATE pg_catalog."default",
    account_verified boolean,
    account_screen_name character(50) COLLATE pg_catalog."default",
    account_location character(255) COLLATE pg_catalog."default",
    CONSTRAINT account_pkey PRIMARY KEY (account_id),
    CONSTRAINT account_account_name_key UNIQUE (account_name),
    CONSTRAINT account_account_screen_name_key UNIQUE (account_screen_name),
    CONSTRAINT account_account_url_key UNIQUE (account_url)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.account
    OWNER to tiv;


-- Table: public.tweets

-- DROP TABLE public.tweets;

CREATE TABLE public.tweets
(
    tweet_id integer NOT NULL DEFAULT nextval('tweets_tweet_id_seq'::regclass),
    account_id integer NOT NULL,
    tweet_time character(100) COLLATE pg_catalog."default" DEFAULT 0,
    tweet_content text COLLATE pg_catalog."default",
    tweet_place character(100) COLLATE pg_catalog."default",
    tweet_hashtags character(255) COLLATE pg_catalog."default",
    tweet_lat double precision,
    tweet_long double precision,
    CONSTRAINT tweets_pkey PRIMARY KEY (tweet_id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.tweets
    OWNER to tiv;
