
TESTUSER='testuser'
TESTPASSWORD='commonpassword'
# Base64 encoded string of 'testuser:commonpassword'
BASIC_AUTH='dGVzdHVzZXI6Y29tbW9ucGFzc3dvcmQ='

# create a map of two values
declare -a GET
GET['todos']=''
GET['todolists']=''

declare -a POST
POST['todos']='{"title":"test todo","description":"test description","completed":false,"todolist":1}'
POST['todolists']='{"title":"test todolist","description":"test description"}'

declare -a PUT
PUT['todos']='{"title":"test todo","description":"test description","completed":true,"todolist":1}'
PUT['todolists']='{"title":"test todolist","description":"test description"}'

declare -a DELETE
DELETE['todos']=''
DELETE['todolists']=''

# MAp over the keys of the GET map
for key in "${!GET[@]}"
do
    echo "GET $key"
done

# List all key value pairs in the GET map
for key in "${GET[@]}"
do
    echo "GET $key"
done

# curl \
#     --verbose \
#     -H "Content-Type: application/json" \
#     -H "Accept: application/json" \
#     -H "Authorization: Basic $BASIC_AUTH" \
#     'http://127.0.0.1:9001/api/v1/todos/'
