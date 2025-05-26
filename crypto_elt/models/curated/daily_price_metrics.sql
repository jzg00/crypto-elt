{{ config(materialized='table') }}

with staged as (
  select * from {{ ref('prices') }}
)

select
  symbol,
  date_trunc('day', ts) as date,
  avg(price) as avg_price,
  min(price) as min_price,
  max(price) as max_price
from staged
group by 1, 2