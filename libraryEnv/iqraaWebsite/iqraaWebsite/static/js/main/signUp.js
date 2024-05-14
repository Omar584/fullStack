

function validation() {
        event.preventDefault(); // Prevent form submission

        var username = document.getElementById('uname').value;
        var password = document.getElementById('pass').value;
        var confirmPassword = document.getElementById('cpass').value;
        var email = document.getElementById('em').value;
        var isAdmin = document.getElementById('is_admin').checked;

        if (username.length < 5) {
            alert('Username must be at least 5 characters long.');
            return false; // Stop form submission
        }

        if (username.includes(' ')) {
            alert('Username cannot contain spaces.');
            return false; // Stop form submission
        }



        if (password.length < 8 ) {
            alert('Password must be at least 8 characters long ');
            return false; // Stop form submission
        }

        if ( !/\d/.test(password) ) {
            alert('password must contain at least one digit ');
            return false; // Stop form submission
        }

        if ( !/[!#$%*@]/.test(password)) {
            alert('please enter one of the following special characters: !, #, $, %, or *');
            return false; // Stop form submission
        }

        if (password !== confirmPassword) {
            alert('Passwords do not match. Please try again.');
            return false; // Stop form submission
        }

        // If validations pass, continue with form submission
        saveUserInfo(event);
    }

function saveUserInfo() {
    var username = document.getElementById('uname').value;
    var password = document.getElementById('pass').value;
    var email = document.getElementById('em').value;
    var isAdmin = document.getElementById('is_admin').checked;

    // Save user info to local storage
    localStorage.setItem('username', username);
    localStorage.setItem('password', password);
    localStorage.setItem('email', email);
    localStorage.setItem('isAdmin', isAdmin ? 'admin' : 'user');

    alert('information saved successfully!');
    // Redirect to login page if needed
     window.location.href = '../../../web-project/index.html';
}