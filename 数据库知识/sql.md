### 1、like 与 rlike
- like的内容不是正则，而是通配符，如： `select * from tablename where col like "%jj%"`
- rlike的内容可以是正则，也可以是包含某个字符
    - 正则：`select * from tablename where col rlike "^.*jj\d+$"`
    - 包含某个字符： `SELECT * FROM categories WHERE  Category  RLIKE "or"`  
        只要Category字段的值中包含 `or` 的行，将会被输出
      