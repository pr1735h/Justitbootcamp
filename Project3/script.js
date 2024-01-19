// Define a function to get a random word from a webpage
function getRandomWord(url) {
    // Use jQuery to fetch the webpage content
    $.get(url, function (data) {
        // Split the content into words by spaces and punctuation
        var words = data.split(/[\s,.?!]+/);
        // Get a random index from the array
        var index = Math.floor(Math.random() * words.length);
        // Get the word at that index
        var word = words[index];
        // Store the word as a variable
        var randomWord = word;
        // Do something with the variable, such as displaying it on the page
        $("#random-word").text(randomWord);
    });
}

// Call the function with a webpage URL as an argument
getRandomWord("[1](https://www.lipsum.com/)");
