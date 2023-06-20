python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt

Дальше в pgAdmin 4 создаём базу данных, дальше создём столбцы, вот sql код столбцов:
1) CREATE TABLE IF NOT EXISTS public.cart
(
    id integer NOT NULL DEFAULT nextval('cart_id_seq'::regclass),
    user_id integer,
    CONSTRAINT cart_pkey PRIMARY KEY (id),
    CONSTRAINT cart_user_id_fkey FOREIGN KEY (user_id)
        REFERENCES public.users (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.cart
    OWNER to postgres;

2) CREATE TABLE IF NOT EXISTS public.cart_flower
(
    id integer NOT NULL DEFAULT nextval('cart_flower_id_seq'::regclass),
    cart_id integer,
    flower_id integer,
    quantity integer NOT NULL,
    CONSTRAINT cart_flower_pkey PRIMARY KEY (id),
    CONSTRAINT cart_flower_cart_id_fkey FOREIGN KEY (cart_id)
        REFERENCES public.cart (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT cart_flower_flower_id_fkey FOREIGN KEY (flower_id)
        REFERENCES public.flowers (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.cart_flower
    OWNER to postgres;

3) CREATE TABLE IF NOT EXISTS public.delivery
(
    id integer NOT NULL DEFAULT nextval('delivery_id_seq'::regclass),
    cart_flower_id integer,
    address character varying(300) COLLATE pg_catalog."default",
    postal_code character varying(30) COLLATE pg_catalog."default",
    CONSTRAINT delivery_pkey PRIMARY KEY (id),
    CONSTRAINT delivery_cart_flower_id_fkey FOREIGN KEY (cart_flower_id)
        REFERENCES public.cart_flower (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.delivery
    OWNER to postgres;

4) CREATE TABLE IF NOT EXISTS public.flowers
(
    id integer NOT NULL DEFAULT nextval('flowers_id_seq'::regclass),
    flower character varying(50) COLLATE pg_catalog."default" NOT NULL,
    description text COLLATE pg_catalog."default",
    quantity integer,
    price numeric(9,2) NOT NULL,
    CONSTRAINT flowers_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.flowers
    OWNER to postgres;

5) CREATE TABLE IF NOT EXISTS public.image_flower
(
    id integer NOT NULL DEFAULT nextval('image_flower_id_seq'::regclass),
    url character varying(255) COLLATE pg_catalog."default",
    flower_id integer,
    CONSTRAINT image_flower_pkey PRIMARY KEY (id),
    CONSTRAINT image_flower_flower_id_fkey FOREIGN KEY (flower_id)
        REFERENCES public.flowers (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

6) CREATE TABLE IF NOT EXISTS public.users
(
    id integer NOT NULL DEFAULT nextval('users_id_seq'::regclass),
    username character varying(30) COLLATE pg_catalog."default" NOT NULL,
    password character varying(50) COLLATE pg_catalog."default" NOT NULL,
    name character varying(20) COLLATE pg_catalog."default",
    email character varying(150) COLLATE pg_catalog."default",
    CONSTRAINT users_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.users
    OWNER to postgres;

Дальше в файле configBD.py внести в переменные все нужные значения, которые там указаны
