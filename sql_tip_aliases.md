## 📌 Tip: Join Tables Properly with Aliases
**Category:** Joins  
**Tags:** `JOIN`, `ALIAS`, `READABILITY`

**Example:**
```sql
SELECT o.id, c.name  
FROM orders o  
JOIN customers c ON o.customer_id = c.id
```

**Explanation:**  
Always use aliases when joining tables. It improves readability and prevents column name conflicts.

**Why it matters:**  
It helps the model disambiguate columns, and also makes queries cleaner.