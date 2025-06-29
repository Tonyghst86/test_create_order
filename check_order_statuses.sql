-- 1. Запрос для получения количества заказов в доставке по каждому курьеру
SELECT
    c.login,
    COUNT(o.id) AS orders_in_delivery
FROM
    "Couriers" c
LEFT JOIN
    "Orders" o ON c.id = o."courierId"
    AND o."inDelivery" = true
GROUP BY
    c.login;

-- 2. Запрос для проверки статусов всех заказов
SELECT
    track,
    CASE
        WHEN finished = true THEN 2
        WHEN cancelled = true THEN -1
        WHEN "inDelivery" = true THEN 1
        ELSE 0
    END AS status
FROM
    "Orders";

