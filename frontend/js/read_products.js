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
                        $(".products").append(displayProduct(p.name, p.description,
                        p.is_perishable, p.freezable, p.price, p.expired, p.validity))
                    }
                else {
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