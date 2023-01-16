function updateProduct(selected) {
    if (selected === "expired_products") {
        ajaxFunction("update_expired_products", "PUT", null, function() {alert("Expired products has been update")})
    }
    else if (selected === "specific_product") {
        $(".content-body").empty()
        displayContent("update")
        $(".content-body").append(`
        <form onsubmit="return false">
            <p>Give the informations:</p>
            <input id="productId" type="number" min="1" placeholder="Product ID"><br><br>
            <input id="nameField" type="text" placeholder="Name"><br>
            <input id="descriptionField" type="text" placeholder="Description"><br>
            <input id="perishableField" type="text" placeholder="Perishable"><br>
            <input id="freezableField" type="text" placeholder="Freezable"><br>
            <input id="priceField" type="text" placeholder="Price"><br>
            <input id="expiredField" type="text" placeholder="Expired"><br>
            <input id="validityField" type="date" placeholder="Validity"><br>
            <button id="updateProduct" type="submit">Update Product</button>
        </form>
        `)
    }

    $(document).on("click", "#updateProduct", function() {
        
        let productToUpdate = $("#productId").val()
        let name = $("#nameField").val()
        let description = $("#descriptionField").val()
        let perishable = booleanFixer($("#perishableField").val())
        let freezable = booleanFixer($("#freezableField").val())
        let price
        let expired = booleanFixer($("#expiredField").val())
        let validity = $("#validityField").val()
    
        if ($("#priceField").val() != "") {
            parseFloat($("#priceField").val())
        }
    
        let values = {
            name: name,
            description: description,
            is_perishable: perishable,
            freezable: freezable,
            price: price,
            expired: expired,
            validity: validity
        }
    
        for (key in values) {
            if (values[key] === null || values[key] === undefined || values[key].length < 1 || values[key] < 0) {
                delete values[key]
            }
        }
        ajaxFunction(`update_product/${productToUpdate}`, "PUT", JSON.stringify(values), function() {
            alert(`The product with ID ${productToUpdate} has been updated.`)
        })
    })
}