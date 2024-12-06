SELECT
p.name AS name,
COUNT(c.amount) AS cash_flows,
MIN(c.amount) AS min_cash_flow,
MAX(c.amount) AS max_cash_flow,
ROUND(AVG(c.amount), 2) AS avg_cash_flow

FROM properties p
JOIN cash_flows p
ON p.id =c.property_id
GROUP BY p.name
HAVING AVG(c.amount) > 10000
ORDER BY p.name ASC;