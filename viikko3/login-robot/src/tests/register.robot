*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input New User  kalle  1209470421a
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New User  kalle  10295u509as
    Input New User  kalle  1092412409421z
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input New User  a  01294912414209a
    Output Should Contain  Username is too short (min. 3 characters)

Register With Enough Long But Invalid Username And Valid Password
    Input New User  äääääääääääää  091209138as
    Output Should Contain  Invalid username

Register With Valid Username And Too Short Password
    Input New User  xzoiaoisdj  1235a
    Output Should Contain  Password is too short (min. 8 characters)

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New User  cxzoicoij  aoisjdoiajsdiaojds
    Output Should Contain  Invalid password

*** Keywords ***
Input New User
    [Arguments]    ${name}    ${password}
    Input  new
    Input Credentials  ${name}  ${password}