from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "group" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(10) NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "group";"""


MODELS_STATE = (
    "eJztl19vmzAUxb9KxFMnbVPCkrXaWxrtr7ZkarNp0jRZBhxixdjUNlurju8+XwMxgQSlL1"
    "sX8QSce2xf/+QD4t5LRESYev5Wiiz1Xg3uPY4TYm52C08HHk5TJ4OgccCsM95aAqUlDrUR"
    "V5gpYqSIqFDSVFPBjcozxkAUoTFSHjsp4/QmI0iLmOg1kabw/YeRKY/ILVHVY7pBK0pYtN"
    "MojWBtqyN9l1rtPddvrBFWC1AoWJZwZ07v9FrwrZtyDWpMOJFYE5heywzah+7KbVY7Kjp1"
    "lqLF2piIrHDGdG27AXKah9B8sUTXr5cIeQ8AFAoOcE2ryu4+hhae+aPx+fjixcvxhbHYNr"
    "fKeV4s7cAUAy2e+dLLbR1rXDgsYwfVXltYZ2ss93Ot/A2ypuUm2YpjF9pKcGzdefobcBN8"
    "ixjhsV6bx9Gwg+TX6dXs3fTqbDR8AgsKc/yLUMzLim9LeQ7Hd7WpsQYhwOHmF5YRalWELw"
    "5526XET5oK5ji24GCH0H8Z5y/KhqsVc6t3pjyrHH3I+5CfXMj9Y0LuHw65/5hC/pnIhCpV"
    "AGlFvVbtDHy66+tj38e+j/1jjv2USBqu90W+rHTGHTtPH/VTifpPIqsX+LFprw05xcBPJs"
    "ckfjI5HHmoAXVHGUL1AMKl/QTpjobH/St1/SwNm3TNipoU0d4l/OF6Md9PuDakQTmioR78"
    "HjCqWu+K/4B2B1yAATMnSt2wOtOzT9NvTdyzj4tLC0coHUs7i53g8l9/zPI/0v7mIA=="
)
