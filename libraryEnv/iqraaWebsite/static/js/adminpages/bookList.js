// Adding an event listener to an element with the ID 'addButton'. This sets up a function to run when the 'addButton' is clicked.
document.getElementById('addButton').addEventListener('click', function() {
    // Retrieve the book details from local storage using the key 'bookDetails'.
    // Local storage stores data as strings, so we need to retrieve the string associated with the key 'bookDetails'.
    const storedBookDetails = localStorage.getItem('bookDetails');

    // Parse the JSON string back into an object because local storage can only store strings.
    // This conversion is necessary to easily access the properties of the book object.
    const book = JSON.parse(storedBookDetails);

    // Retrieve the element with the ID 'mainContainer' which will act as the parent for the new content.
    const parentDiv = document.getElementById('mainContainer');

    // Create a new div element. This will be used to display the book details.
    let newDiv = document.createElement('div');
    
    // Set the inner HTML of the new div to include a link, an image, and a div for the book ID.
    // The 'book' object properties are used here to dynamically fill data in the HTML structure.
    newDiv.innerHTML = `
            <a href=""> 
                <img src="${book.image}" alt="${book.name}">
                <div class="bName">ID: ${book.id}</div>
            </a>` ;
    
    // Assign a class name to the new div for styling purposes. This helps in applying specific styles to the container.
    newDiv.className = 'imageContainer';
    newDiv.id = book.id ;

    // Append the newly created div to the 'mainContainer'. This makes the new div visible on the page.
    parentDiv.appendChild(newDiv);

    // Display an alert to the user indicating that the book has been successfully added.
    // This provides immediate feedback that the action was successful.
    window.alert(`book with id ${book.id} is added successfully`);
});



// Adding an event listener to an HTML element with the ID 'deleteButton'. This sets up the function to run when the 'deleteButton' is clicked.
document.getElementById('deleteButton').addEventListener('click', function() {
    // Retrieve the book ID from local storage using the key 'removedBookId'.
    // Local storage is a key-value store, and the data is persisted even after the browser window is closed.
    const bookId = localStorage.getItem('removedBookId');
    
    // Check if the bookId was successfully retrieved and is not null. This is necessary because getItem will return null if the key does not exist.
    if (bookId) {
        // Get the HTML element (div) corresponding to the retrieved book ID. 
        // This assumes that the book ID is used as an ID for a DOM element, allowing direct access.
        let childDiv = document.getElementById(bookId);
        
        // Ensure that the element with the given ID exists in the DOM before attempting any operations on it.
        if (childDiv) {
            // If the element exists, remove it from the document. The remove() method removes the element from the DOM.
            childDiv.remove();
            // Provide feedback to the user through an alert that the operation was successful.
            alert('Book removed successfully!');
        } else {
            // If no element with the specified ID was found in the DOM, alert the user about this issue.
            alert('Error: No element found with the specified ID.');
        }
    } else {
        // If no book ID was found in local storage, alert the user that the necessary information to perform the deletion is missing.
        alert('Error: No book ID found in local storage.');
    }
});

