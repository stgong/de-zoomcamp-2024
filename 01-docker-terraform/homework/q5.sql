SELECT z."Borough"
, SUM(t.total_amount) AS total_fee
FROM PUBLIC.GREEN_TRIPDATA_2019_09 t
LEFT JOIN public.zones z ON t."PULocationID" = z."LocationID"
WHERE DATE(t.LPEP_PICKUP_DATETIME) = '2019-09-18'
GROUP BY 1
ORDER BY total_fee DESC