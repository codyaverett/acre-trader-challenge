create or replace procedure value_transfer(
   sender int,
   receiver int, 
   amount dec
)
language plpgsql    
as $$
begin
    -- subtracting the amount from the sender's account 
    update account 
    set balance = balance - amount 
    where id = sender;

    -- adding the amount to the receiver's account
    update account 
    set balance = balance + amount 
    where id = receiver;

    commit;
end;$$;

-- Call the procedure
call value_transfer(1, 2, 1000);
