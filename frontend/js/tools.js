let server = `localhost:5000`

function returnToDefault() {
    $(".content-body").empty()
    $(".content-body").append(`<p>Press an button to start to testing the program</p>`)
    $(".products").empty()
}

function displayContent(type) {
    $(".content-body").empty()
    clearProducts()
    if (type.toUpperCase() === "CREATE") {
        $(".content-body").append(`
        <p>Insert the informations to create a new product:</p>
        <form onsubmit="return false">
            <input id="nameField" type="text" placeholder="Name"><br>
            <input id="descriptionField" type="text" placeholder="Description"><br>
            <input id="perishableField" type="text" placeholder="Perishable"><br>
            <input id="freezableField" type="text" placeholder="Freezable"><br>
            <input id="priceField" type="text" placeholder="Price"><br>
            <input id="expiredField" type="text" placeholder="Expired"><br>
            <input id="validityField" type="date" placeholder="Validity"><br>
            <button id="createProduct" type="submit">Create Product</button>
        </form>
        `)
    }

    else if (type.toUpperCase() === "READ") {
        $(".content-body").append(`
        <p>Search by:</p>
        <select name="searchType" id="selectType">
            <option value="all">All products</option>
            <option value="id">By id</option>
            <option value="name">By name</option>
            <option value="price">By price</option>
            <option value="maxPrice">By max price</option>
            <option value="minPrice">By min price</option>
            <option value="perishable">By perishable</option>
            <option value="freezable">By freezable</option>
            <option value="validity">By validity</option>
            <option value="expired">By expired</option>
        </select>
        <input id="information" type="text">
        <button onclick="readOptions()">Go</button>
        `)
    }

    else if (type.toUpperCase() === "UPDATE") {
        $(".content-body").append(`
        <p>Select an option:</p>
        <button onclick="updateProduct('specific_product')">Update a specific product</button>
        <button onclick="updateProduct('expired_products')">Update the expired products not updated</button>
        `)
    }

    else if (type.toUpperCase() === "DELETE") {
        $(".content-body").append(`
            <p>Insert the id of the product that you want to delete</p><br>
            <input id="productToDelete" type="number" min="1" placeholder="ID of the product"><button id="deleteBtn">Delete<button>
        `)
    }
}

function clearProducts() {
    $(".products").empty()
}

function booleanFixer(value) {
    if (value.toUpperCase() === "TRUE") {
        return true
    }
    else if (value.toUpperCase() === "FALSE") {
        return false
    }
    return null
}

function displayProduct(name, description, is_perishable, freezable, price, expired, validity) {
    if (!validity) {
        validity = "Don't expire"
    }
    return `<div class="product">
                <ul>
                    <li>Name: ${name}</li>
                    <li>Description: ${description}</li>
                    <li>Is perishable: ${is_perishable}</li>
                    <li>Freezable: ${freezable}</li>
                    <li>Price: ${price}</li>
                    <li>Expired: ${expired}</li>
                    <li>Validity: ${validity}</li>
                </ul>
            </div>`
    
}

function ajaxFunction(route, type, data, successFunction) {
    if (type === "GET") {
        $.ajax({
            url: `http://${server}/${route}`,
            type: `${type}`,
            dataType: "JSON",
            contentType: "application/json",
            success: successFunction,
            error: function(xhr, status, error) {
                alert(`Connection error, check backend. ${xhr.responseText} - ${status} - ${error}`);
            }
        })
    }

    else if (type === "POST" || type === "PUT") {
        $.ajax({
            url: `http://${server}/${route}`,
            type: `${type}`,
            dataType: "JSON",
            contentType: "application/json",
            data: data,
            success: successFunction,
            error: function(xhr, status, error) {
                alert(`Erro na conexão, verifique o backend. ${xhr.responseText} - ${status} - ${error}`);
            }
        })
    }

    else if (type === "DELETE") {
        $.ajax({
            url: `http://${server}/${route}`,
            type: `${type}`,
            dataType: "JSON",
            contentType: "application/json",
            data: data,
            success: successFunction,
            error: function(xhr, status, error) {
                alert(`Erro na conexão, verifique o backend. ${xhr.responseText} - ${status} - ${error}`);
            }
        })
    }
}