#import asyncpg
##from asyncpg.pool import Pool
#from typing import Union

#from data import config


#class Database:
    #def __init__(self):
       # self.pool: Union[Pool, None] = None

    #async def create(self):
       # self.pool = await asyncpg.create_pool(
           # user=config.DB_USER,
           #host=config.DB_HOST,
           # database=config.DB_NAME
   #     )

   # async def execute(self, command, *args,
                     ## fetch: bool = False,
                      #fetchval: bool = False,
                     #fetchrow: bool = False,
                      #execute: bool = False):
        #async with self.pool.acquire() as connection:
           # connection: Connection
            #async with connection.transaction():
                #if fetch:
                   # result = await connection.fetch(command, *args)
               # elif fetchval:
                  # result = await connection.fetchval(command, *args)
                #elif fetchrow:
                    #result = await connection.fetchrow(command, *args)
               # elif execute:
                   # result = await connection.execute(command, *args)
          #  return result

  #  @staticmethod
   # def format_args(sql, parameters: dict):
     #   sql += 'AND'.join([
      #      f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)
     #   ])

       # return sql, tuple(parameters.values())

   # async def hero_inf(self, name_1):
     #   sql = """SELECT agility_heroe FROM agility_heroes WHERE name_1 = 'Anti-mage'"""
      #  return await self.execute(sql, name_1, fetchrow=True)


import sqlite3


class Database:
    def __init__(self):
        self.__connection = sqlite3.connect('data.db')

    def __query(self, query, commit=False, fetchone = False):
        """Создает запрос к базе данных. commit = True сохраняет таблицу"""
        cursor = self.__connection.cursor()
        if fetchone:
            record = cursor.execute(query).fetchone()
        else:
            record = cursor.execute(query).fetchall()
        if commit:
            self.__connection.commit()
        cursor.close()
        return record

    def hero_inf(self, name1):
        sql = f'SELECT herous FROM agility_heroes WHERE name1 = "{name1}";'
        return  self.__query(sql, fetchone = True)[0]

    def hero_inf2(self, name2):
        sql = f'SELECT herous2 FROM power_heroes WHERE name2 = "{name2}";'
        return  self.__query(sql, fetchone = True)[0]

    def hero_inf3(self, name3):
        sql = f'SELECT herous3 FROM intelligence_heroes WHERE name3 = "{name3}";'
        return  self.__query(sql, fetchone = True)[0]

    def item_inf(self, item1):
        sql = f'SELECT infitem FROM simple_items WHERE item1 = "{item1}";'
        return  self.__query(sql, fetchone = True)[0]

    def item_inf2(self, item2):
        sql = f'SELECT infitem1 FROM discharge1 WHERE item2 = "{item2}";'
        return  self.__query(sql, fetchone = True)[0]

    def item_inf3(self, items3):
        sql = f'SELECT infitems3 FROM collect_items WHERE items3 = "{items3}";'
        return  self.__query(sql, fetchone = True)[0]


