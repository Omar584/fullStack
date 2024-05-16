

<<<<<<< Updated upstream
function validation() {
        
        var username = document.getElementById('uname').value;
        var password = document.getElementById('pass').value;
        var confirmPassword = document.getElementById('cpass').value;
        var email = document.getElementById('em').value;
        var isAdmin = document.getElementById('is_admin').checked;

        if(username.length < 5) {
            document.getElementById('username').innerHTML = 'Username must be at least 5 characters long.' ;
            event.preventDefault();
        }

        if(username.includes(' ')) {
            document.getElementById('username').innerHTML = 'Username cannot contain spaces.' ;
            event.preventDefault();
        }
        if(password.length < 8 ) {
            document.getElementById('password').innerHTML = 'Password must be at least 8 characters long' ;
            event.preventDefault();
        }

        if( !/\d/.test(password) ) {
            document.getElementById('password').innerHTML = 'password must contain at least one digit ' ;
            event.preventDefault();
        }

        if( !/[!#$%*@]/.test(password)) {
            document.getElementById('passtest').innerHTML = 'please enter one of the following special characters: !, #, $, %, or *' ;
            event.preventDefault();
        }

        if(password !== confirmPassword) {
            document.getElementById('password').innerHTML = 'Passwords do not match. Please try again.' ;
            event.preventDefault();
        }

<<<<<<< HEAD
        if (password !== confirmPassword) {
            alert('Passwords do not match. Please try again.');
            return false; // Stop form submission
        }

        // If validations pass, continue with form submission
        // window.location.href = "{% url 'index' %}";
=======
>>>>>>> 0e047f615692777d4ee10bb9bc677f6102e07c93
    }
=======
function validation(event) { 
    var username = document.getElementById('uname').value; 
    var password = document.getElementById('pass').value; 
    var confirmPassword = document.getElementById('cpass').value; 
 
    if(username.length < 5) { 
        document.getElementById('uname').innerHTML = 'Username must be at least 5 characters long.'; 
        return false; 
    } 
 
    if(username.includes(' ')) { 
        document.getElementById('uname').innerHTML = 'Username cannot contain spaces.'; 
        return false; 
    } 
 
    if(password.length < 8 ) { 
        document.getElementById('pass').innerHTML = 'Password must be at least 8 characters long'; 
        return false; 
    } 
 
    if( !/\d/.test(password) ) { 
        document.getElementById('pass').innerHTML = 'Password must contain at least one digit'; 
        return false; 
    } 
 
    if( !/[!#$%*@]/.test(password)) { 
        document.getElementById('pass').innerHTML = 'Please enter one of the following special characters: !, #, $, %, or *'; 
        return false; 
    } 
 
    if(password !== confirmPassword) { 
        document.getElementById('pass').innerHTML = 'Passwords do not match. Please try again.'; 
        return false; 
    } 
 
    return true; 
} 
>>>>>>> Stashed changes
