const api = "http://127.0.0.1:5000";

window.onload = () => {
    // BEGIN CODE HERE
    document.getElementById('product-form').addEventListener('submit', productFormOnSubmit);
    document.getElementById('search-button').addEventListener('click', searchButtonOnClick);
    // END CODE HERE
}

searchButtonOnClick = () => {
    // BEGIN CODE HERE
    const search_name = document.getElementById('search').value;
    const query = '/search?name=' + encodeURIComponent(search_name);
    let results = document.getElementById('search-results');
    fetch(api + query, {
        method: 'GET',
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            let new_row = results.insertRow(0);
            for (let i = 0; i < data.length; i++) {
                let new_cell = new_row.insertCell(i);
                new_cell.innerHTML = data[i];
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });

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
