{{ config(materialized='table') }}

SELECT
  symbol,
  price,
  ts
FROM {{ source('crypto_raw','prices_raw') }}
