const api = "http://127.0.0.1:5000";

window.onload = () => {
    // BEGIN CODE HERE
    document.getElementById('product-form').addEventListener('submit', productFormOnSubmit);
    console.log("Window loaded");
    // END CODE HERE
}

searchButtonOnClick = () => {
    // BEGIN CODE HERE

    // END CODE HERE
}

productFormOnSubmit = (event) => {
    // BEGIN CODE HERE
    event.preventDefault();
    let product = {
        id: "",
        name: document.getElementById("name").value,
        production_year: document.getElementById("year").value,
        price: document.getElementById("price").value,
        color: parseInt(document.getElementById("color").value),
        size: parseInt(document.getElementById("size").value)
    };
    fetch(api + '/add-product', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(product),
    })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch((error) => {
            console.error('Error:', error);
        });
    console.log("Product added");
    // END CODE HERE
}
