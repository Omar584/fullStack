

function validation() {
        
        var username = document.getElementById('uname').value;
        var password = document.getElementById('pass').value;
        var confirmPassword = document.getElementById('cpass').value;
        var email = document.getElementById('em').value;
        var isAdmin = document.getElementById('is_admin').checked;

        if(username.length < 5) {
            document.getElementById('username').innerHTML = 'Username must be at least 5 characters long.' ;
            event.preventDefault(event) ;
        }

        if(username.includes(' ')) {
            document.getElementById('username').innerHTML = 'Username cannot contain spaces.' ;
            return false ;
        }
        if(password.length < 8 ) {
            document.getElementById('password').innerHTML = 'Password must be at least 8 characters long' ;
            return false ;
        }

        if( !/\d/.test(password) ) {
            document.getElementById('password').innerHTML = 'password must contain at least one digit ' ;
            return false ;
        }

        if( !/[!#$%*@]/.test(password)) {
            document.getElementById('passtest').innerHTML = 'please enter one of the following special characters: !, #, $, %, or *' ;
            return false;
        }

        if(password !== confirmPassword) {
            document.getElementById('password').innerHTML = 'Passwords do not match. Please try again.' ;
            return false ;
        }
    }