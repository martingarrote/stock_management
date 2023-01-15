let server = `localhost:5000`

function returnToDefault() {
    $(".content-body").empty()
    $(".content-body").append(`<p>Press an button to start to testing the program</p>`)
}

function progress(type) {
    $(".content-body").empty()
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
            <input id="validityField" type="date" placeholder="Validity"> <button onclick="turnNone()">None</button><br>
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
}

function readOptions() {
    clearProducts()
    let value = $("#selectType").find(":selected").val()
    let information = $("#information").val()
    let route
    if (information.length > 0 || value === "all" || value === "expired") {
        if (value === "all") {
            route = "products"
        }
        else if (value === "id") {
            route = `products/search/id/${information}`
        }
        else if (value === "name") {
            route = `products/search/name/${information}`
        }
        else if (value === "price") {
            route = `products/search/price/${information}`
        }
        else if (value === "maxPrice") {
            route = `products/search/max_price/${information}`
        }
        else if (value === "minPrice") {
            route = `products/search/min_price/${information}`
        }
        else if (value === "perishable") {
            route = `products/search/perishable/${information}`
        }
        else if (value === "freezable") {
            route = `products/search/freezable/${information}`
        }
        else if (value === "validity") {
            route = `products/search/validity/${information}`
        }
        else if (value === "expired") {
            route = `products/search/expired`
        }
        ajaxFunction(route, "GET", null, function (returnContent) {
            if (returnContent.result === "success") {
                console.log(route)
                if (route != `products/search/id/${information}`)
                    for (p of returnContent.details) {
                        console.log(p)
                        $(".products").append(displayProduct(p.name, p.description,
                        p.is_perishable, p.freezable, p.price, p.expired, p.validity))
                    }
                else {
                    console.log("oi")
                    let p = returnContent.details
                    $(".products").append(displayProduct(p.name, p.description,
                        p.is_perishable, p.freezable, p.price, p.expired, p.validity))
                }
            }
        })
    }
    else {
        alert("It is necessary to provide information in the respective field.")
    }
}

function clearProducts() {
    $(".products").empty()
}

function booleanFixer(value) {
    if (value.toUpperCase() === "TRUE") {
        return true
    }
    return false
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
    console.log(route, type, data, successFunction)
    if (type === "GET") {
        $.ajax({
            url: `http://${server}/${route}`,
            type: `${type}`,
            dataType: "JSON",
            contentType: "application/json",
            success: successFunction,
            error: function(xhr, status, error) {
                alert(`Erro na conexão, verifique o backend. ${xhr.responseText} - ${status} - ${error}`);
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