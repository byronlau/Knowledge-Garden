---
title: PostgreSQL对应Mysql中对IP进行转化的操作
number: 34
url: https://github.com/byronlau/Knowledge-Garden/discussions/34
date: 2023-11-02
createdAt: 2023-11-02T03:06:37Z
lastEditedAt: None
updatedAt: 2023-11-02T03:06:39Z
authors: [byronlau]
categories: 
  - DB
labels: []
filename: PostgreSQL对应Mysql中对IP进行转化的操作.md
---

``` sql
-- ip convert int
create or replace function inet_aton(ip text) returns int8 as $$

declare

v int;

res int8 :=0;

i int :=3;

begin

foreach v in array string_to_array(ip,'.') loop

res := res+v*(256^i);

i :=i-1;

end loop;

return res;

end;

$$ language  plpgsql;

-- int convert ip

create or replace function inet_ntoa(ip int8) returns text as $$

declare

res text :='';

begin

res := res || ((ip >> 24) & (2^8-1)::int);

res :=res || '.' || ((ip >> 16) & (2^8-1)::int);

res :=res || '.' || ((ip >> 8) & (2^8-1)::int);

res :=res || '.' || (ip & (2^8-1)::int);

return res;

end;

$$ language  plpgsql;
```



<script src="https://giscus.app/client.js"
    data-repo="byronlau/Knowledge-Garden"
    data-repo-id="R_kgDOKkfaDQ"
    data-mapping="number"
    data-term="34"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        