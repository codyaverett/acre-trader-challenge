create or replace procedure add_todo(
    title varchar(100)
    , details varchar(1000)
    , active boolean
    , username varchar(100)
)
language plpgsql    
as $$
begin

    -- insert the todo
    insert into todo (title, details, active, created_by, updated_by)
    values (title, details, active, username, username);

    commit;
end;$$;

-- Call the procedure
call add_todo('first todo', 'do something', true, 'cody');
call add_todo('second todo', 'no details', true, 'heather');
call add_todo('third todo', 'no details', true, 'joe');
call add_todo('fourth todo', 'no details', true, 'emalee');