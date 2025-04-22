select user_id , concat(ucase(substring(name,1,1)),lcase(substring(name,2,length(name)-1)))as name from users
order by user_id;
