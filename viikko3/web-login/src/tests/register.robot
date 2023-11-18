*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Register With Credentials  zxczxc  897987z987x
    Register Should Succeed

Register With Too Short Username And Valid Password
    Register With Credentials  zx  123123123jn123
    Register Should Fail With Message  Username is too short (min. 3 characters)

Register With Valid Username And Invalid Password
    Register With Credentials  zxcvxcbvxc  asdasdasdasdasd
    Register Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Go To Register Page
    Set Username  aaoujznxczjkzncx
    Set Password  91028412498s
    Input Password  password_confirmation  08xvyx9vc708xvc9
    Submit Credentials
    Register Should Fail With Message  Password and password confirmation do not match

Login After Successful Registration
    Register With Credentials  abc  123123123
    Login With Credentials  abc  123123123
    Main Page Should Be Open

Login After Failed Registration
    Register With Credentials  a  123123123
    Login With Credentials  a  123123123
    Page Should Contain  Invalid username or password


*** Keywords ***
Register With Credentials
    [arguments]  ${username}  ${password}
    go to register page
    set username  ${username}
    set password  ${password}
    set password confirmation  ${password}
    submit credentials

Login With Credentials
    [arguments]  ${username}  ${password}
    Go To Login Page
    set username  ${username}
    set password  ${password}
    Click Button  Login

Register Should Succeed
    Title Should Be  Welcome to Ohtu Application!

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}