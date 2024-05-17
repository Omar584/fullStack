


function validation() {
    
    var isValid=true;
    
    

    var username = document.getElementById('uname').value;
    var password = document.getElementById('pass').value;
    var confirmPassword = document.getElementById('cpass').value;
    var email = document.getElementById('em').value;
    var isAdmin = document.getElementById('is_admin').checked;

    if(username.length < 5) {
        document.getElementById('username').innerHTML = 'sjjername must be at leauhqej,krhcj7.';
        isValid = false;
    }
    
    if(password.length < 8 ) {
        document.getElementById('password').innerHTML = 'Password must be at least 8 characters long' ;
        isValid = false;
    }
    if( !/[!#$%*@]/.test(password)) {
        document.getElementById('passtest').innerHTML = 'please enter one of the following special characters: !, #, $, %, or *' ;
        isValid = false;
    }

    if(password !== confirmPassword) {
        document.getElementById('confirmpassword').innerHTML = 'Passwords do not match. Please try again.' ;
        isValid = false;
    }
    // If validations pass, continue with form submissi
    // window.location.href = "{% url 'index' %}";
    return isValid;
}
        
    

    document.querySelector('form').addEventListener('submit', validation);