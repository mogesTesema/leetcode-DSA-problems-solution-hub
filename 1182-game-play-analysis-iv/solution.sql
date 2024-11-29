WITH min_event_date_cte AS (
    SELECT 
        player_id,
        MIN(event_date) AS min_date
    FROM  activity
    GROUP BY player_id
)
SELECT 
    ROUND(
        COALESCE(COUNT(b.player_id), 0) / COUNT(DISTINCT a.player_id), 
        2
    ) AS fraction
FROM activity a
LEFT JOIN activity b 
	ON a.player_id = b.player_id 
		AND DATEDIFF(b.event_date, a.event_date) = 1
JOIN min_event_date_cte m 
	ON a.player_id = m.player_id 
		AND a.event_date = m.min_date;
