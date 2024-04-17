import os
import psycopg2

def init_dba():
    conn = psycopg2.connect(
            host="database",
            database="postgres",
            user="postgres",
            password="admin")
            
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS public.themes;')
    cur.execute('CREATE TABLE public.themes (id serial PRIMARY KEY,'
                                            'name varchar (50) NOT NULL,'
                                            'cnt_mess integer NOT NULL);'
                                            )
                                            
    cur.execute('DROP TABLE IF EXISTS public.user;')
    cur.execute('CREATE TABLE public.user (id serial PRIMARY KEY,'
                                            'login varchar (80) NOT NULL,'
                                            'password varchar (90) NOT NULL,'
                                            'carma integer NOT NULL);'
                                            )
                                            
    cur.execute('INSERT INTO public.themes (name, cnt_mess) VALUES (%s, %s)',
                ('Аниме',
                6772)
                )
    cur.execute('INSERT INTO public.themes (name, cnt_mess) VALUES (%s, %s)',
                ('Приколы',
                8054)
                )
    cur.execute('INSERT INTO public.themes (name, cnt_mess) VALUES (%s, %s)',
                ('Рецепты',
                560)
                )
    cur.execute('INSERT INTO public.themes (name, cnt_mess) VALUES (%s, %s)',
                ('Садоводство',
                122)
                )    
                           
    cur.execute('INSERT INTO public.user (login, password, carma) VALUES (%s, %s, %s)',
                ('animeshnik',
                'mikumiku',
                88)
                )
    cur.execute('INSERT INTO public.user (login, password, carma) VALUES (%s, %s, %s)',
                ('babavalya',
                'vnuchok0709',
                5)
                )
    cur.execute('INSERT INTO public.user (login, password, carma) VALUES (%s, %s, %s)',
                ('anonimus',
                'hacktheworld',
                -20)
                )

    conn.commit()
    cur.close()
    conn.close()
init_dba()
