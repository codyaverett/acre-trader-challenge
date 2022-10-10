CREATE PROCEDURE deactivate_unpaid_accounts()
LANGUAGE SQL
AS $$
  UPDATE accounts SET active = false WHERE balance < 0;
$$;

-- CALL deactivate_unpaid_accounts();
